"""
سكربت تهيئة قاعدة البيانات وإنشاء الحساب الإداري الأساسي
"""
import os
from flask import Flask
from database import db, User
from security import log_security_event

def initialize_database():
    app = Flask(__name__)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'archaeology_vault.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'setup-secret-key-1234'
    
    db.init_app(app)

    with app.app_context():
        # إنشاء كافة الجداول المحددة في database.py
        print("[*] جارٍ إنشاء جداول قاعدة البيانات...")
        db.create_all()
        print("[+] تم إنشاء الجداول بنجاح.")

        # التحقق مما إذا كان حساب المسؤول موجوداً مسبقاً
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            print("[*] إنشاء الحساب الإداري الافتراضي الأول...")
            admin = User(
                username='admin',
                full_name='System Administrator',
                email='admin@archaeology.vault',
                role='Admin',
                is_active=True
            )
            # تعيين كلمة مرور أمنية مشفرة
            admin.set_password('Admin@2026Secure!')
            db.session.add(admin)
            db.session.commit()
            print("[+] تم إنشاء حساب المسؤول بنجاح:")
            print("    Username: admin")
            print("    Password: Admin@2026Secure!")
        else:
            print("[i] حساب المسؤول موجود مسبقاً.")

if __name__ == '__main__':
    initialize_database()