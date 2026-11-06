"""
نظام إدارة وحماية الأرشيف الأثري الرقمي
الملف: tests/test_security.py
الوصف: اختبارات عملية آلية للأمان وعزل البيانات ومنع هجمات IDOR باستخدام Pytest
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app
from database import db, User, ArchaeologicalRecord

@pytest.fixture
def client():
    test_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_vault.db'))
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{test_db_path}'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        # تنظيف وإنشاء الجداول بالأعمدة الجديدة
        db.drop_all()
        db.create_all()

        # إنشاء المستخدم أحمد (User)
        user_ahmed = User(
            id=1, 
            username="ahmed", 
            full_name="Ahmed Ali", 
            email="ahmed@vault.local", 
            role="User",
            academic_affiliation="Independent"
        )
        user_ahmed.set_password("Ahmed@1234")
        db.session.add(user_ahmed)

        # إنشاء الباحث علي (Researcher)
        researcher_ali = User(
            id=2, 
            username="ali", 
            full_name="Ali Hassan", 
            email="ali@vault.local", 
            role="Researcher",
            academic_affiliation="Baghdad Heritage Institute"
        )
        researcher_ali.set_password("Ali@1234")
        db.session.add(researcher_ali)

        # إنشاء مدير النظام (Admin)
        admin = User(
            id=3, 
            username="admin_super", 
            full_name="System Admin", 
            email="admin@vault.local", 
            role="Admin",
            academic_affiliation="National Cyber Directorate"
        )
        admin.set_password("Admin@1234")
        db.session.add(admin)

        db.session.commit()

        # ملف أثري خاص بأحمد (User ID = 1)
        record_ahmed = ArchaeologicalRecord(
            id=101,
            record_id="REC-AHMED-01",
            artifact_name="Ur Vase",
            category="Pottery",
            historical_period="Sumerian",
            discovery_location="Ur",
            user_id=1,
            is_public=False,
            stored_filename="file1.png",
            original_filename="vase.png",
            file_format="png",
            file_size_bytes=1024,
            sha256_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )

        # بحث أثري خاص بالباحث علي (Researcher ID = 2)
        record_ali = ArchaeologicalRecord(
            id=102,
            record_id="REC-ALI-02",
            artifact_name="Babylon Tablet",
            category="Cuneiform",
            historical_period="Babylonian",
            discovery_location="Babylon",
            user_id=2,
            is_public=False,
            stored_filename="file2.pdf",
            original_filename="tablet.pdf",
            file_format="pdf",
            file_size_bytes=2048,
            sha256_hash="ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
        )

        db.session.add_all([record_ahmed, record_ali])
        db.session.commit()

    with app.test_client() as client:
        yield client

    # تنظيف قاعدة بيانات الاختبار بعد الانتهاء
    with app.app_context():
        db.session.remove()
        db.drop_all()
    if os.path.exists(test_db_path):
        try:
            os.remove(test_db_path)
        except Exception:
            pass

def login_helper(client, username, password):
    return client.post('/login', data={'username': username, 'password': password}, follow_redirects=True)

# 1. اختبار: المستخدم لا يستطيع مشاهدة لوحة الأدمن (403 Forbidden)
def test_regular_user_cannot_access_admin_panel(client):
    login_helper(client, 'ahmed', 'Ahmed@1234')
    response = client.get('/admin/dashboard')
    assert response.status_code == 403

# 2. اختبار: الباحث لا يستطيع مشاهدة لوحة الأدمن (403 Forbidden)
def test_researcher_cannot_access_admin_panel(client):
    login_helper(client, 'ali', 'Ali@1234')
    response = client.get('/admin/dashboard')
    assert response.status_code == 403

# 3. اختبار IDOR: المستخدم أحمد لا يستطيع مشاهدة السجل الخاص بالباحث علي عند تلاعب الرابط
def test_user_cannot_view_researcher_private_file(client):
    login_helper(client, 'ahmed', 'Ahmed@1234')
    response = client.get('/record/102')
    assert response.status_code == 403

# 4. اختبار IDOR: الباحث علي لا يستطيع مشاهدة السجل الخاص بالمستخدم أحمد
def test_researcher_cannot_view_user_private_file(client):
    login_helper(client, 'ali', 'Ali@1234')
    response = client.get('/record/101')
    assert response.status_code == 403

# 5. اختبار منع الحذف غير المصرح به: أحمد لا يستطيع حذف سجل علي
def test_user_cannot_delete_other_user_file(client):
    login_helper(client, 'ahmed', 'Ahmed@1234')
    response = client.post('/record/102/delete')
    assert response.status_code == 403

# 6. اختبار: المستخدم يستطيع مشاهدة سجله الخاص بصورة طبيعية (200 OK)
def test_user_can_access_own_file(client):
    login_helper(client, 'ahmed', 'Ahmed@1234')
    response = client.get('/record/101')
    assert response.status_code == 200

# 7. اختبار: الأدمن يستطيع مراجعة السجلات والتفاصيل ضمن صلاحياته الرقابية (200 OK)
def test_admin_can_access_records_and_dashboard(client):
    login_helper(client, 'admin_super', 'Admin@1234')
    dashboard_res = client.get('/admin/dashboard')
    assert dashboard_res.status_code == 200
    record_res = client.get('/record/101')
    assert record_res.status_code == 200

# 8. اختبار: منع التلاعب بالدور أثناء إنشاء الحساب (Role Escalation Prevention)
def test_user_cannot_register_as_admin(client):
    client.post('/register', data={
        'full_name': 'Hacker Man',
        'username': 'attacker',
        'email': 'attacker@vault.local',
        'role': 'Admin',
        'affiliation': 'DarkWeb',
        'password': 'Password@123',
        'confirm_password': 'Password@123'
    })
    with app.app_context():
        user = User.query.filter_by(username='attacker').first()
        assert user is not None
        assert user.role == 'User'