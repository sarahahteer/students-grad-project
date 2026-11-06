"""
سكربت تهيئة قاعدة البيانات وإنشاء الحساب الإداري الأساسي
"""
import os
from flask import Flask
from database import db, User

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'archaeology_vault.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'setup-secret-key-1234'

db.init_app(app)

with app.app_context():
    print("[*] إنشاء الجداول بالهيكل الأمني الجديد...")
    db.create_all()
    print("[+] تم إنشاء الجداول بنجاح.")

    admin = User(
        username='admin',
        full_name='System Administrator',
        email='admin@archaeology.vault',
        role='Admin',
        academic_affiliation='Security Operations Center',
        is_active=True
    )
    admin.set_password('Admin@2026Secure!')
    db.session.add(admin)
    db.session.commit()
    print("[+] تم إنشاء حساب المدير بنجاح.")