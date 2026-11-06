from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='User')  # Admin, Researcher, User
    academic_affiliation = db.Column(db.String(150), default="Independent")
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    failed_login_attempts = db.Column(db.Integer, default=0, nullable=False)

    records = db.relationship('ArchaeologicalRecord', backref='owner', lazy=True, cascade="all, delete-orphan")
    logs = db.relationship('SecurityLog', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role == 'Admin'

    def is_researcher(self):
        return self.role == 'Researcher'

    def is_regular_user(self):
        return self.role == 'User'


class ArchaeologicalRecord(db.Model):
    __tablename__ = 'archaeological_records'

    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.String(64), unique=True, nullable=False, index=True)
    artifact_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    historical_period = db.Column(db.String(100), nullable=False)
    discovery_location = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_public = db.Column(db.Boolean, default=False, nullable=False)

    upload_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    stored_filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_format = db.Column(db.String(10), nullable=False)
    file_size_bytes = db.Column(db.Integer, nullable=False)
    sha256_hash = db.Column(db.String(64), nullable=False, index=True)
    integrity_status = db.Column(db.String(20), default='VERIFIED', nullable=False)

    integrity_checks = db.relationship('IntegrityCheck', backref='record', cascade="all, delete-orphan", lazy=True)


class SecurityLog(db.Model):
    __tablename__ = 'security_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    username = db.Column(db.String(50), nullable=True)
    event_type = db.Column(db.String(50), nullable=False, index=True)
    description = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)
    status = db.Column(db.String(20), default='SUCCESS', nullable=False)


class IntegrityCheck(db.Model):
    __tablename__ = 'integrity_checks'

    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey('archaeological_records.id'), nullable=False)
    checked_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    checked_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    original_hash = db.Column(db.String(64), nullable=False)
    recalculated_hash = db.Column(db.String(64), nullable=False)
    result = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.String(255), nullable=True)

    checker = db.relationship('User', backref='performed_checks')


class SuspiciousActivity(db.Model):
    __tablename__ = 'suspicious_activities'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    activity_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=False)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    severity = db.Column(db.String(20), default='MEDIUM', nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)
    is_resolved = db.Column(db.Boolean, default=False, nullable=False)