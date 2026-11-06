import hashlib
from functools import wraps
from flask import abort, request, redirect, url_for
from flask_login import current_user
from database import db, SecurityLog, SuspiciousActivity

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'tif', 'tiff', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def calculate_file_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def log_security_event(event_type, description, status="SUCCESS", user=None):
    try:
        active_user = user if user else (current_user if current_user.is_authenticated else None)
        user_id = active_user.id if active_user else None
        username = active_user.username if active_user else "ANONYMOUS"
        ip_addr = request.remote_addr if request else "127.0.0.1"

        log_entry = SecurityLog(
            user_id=user_id,
            username=username,
            event_type=event_type,
            description=description,
            ip_address=ip_addr,
            status=status
        )
        db.session.add(log_entry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[SECURITY LOG ERROR]: {e}")

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        if not current_user.is_admin():
            log_security_event(
                event_type="UNAUTHORIZED_ACCESS",
                description=f"User '{current_user.username}' attempted to access admin page: {request.path}",
                status="DANGER"
            )
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def enforce_record_data_isolation(record, require_write=False):
    if current_user.is_admin():
        return True
    if record.user_id == current_user.id:
        return True
    if not require_write and record.is_public:
        return True

    log_security_event(
        event_type="IDOR_VIOLATION_ATTEMPT",
        description=f"User '{current_user.username}' attempted unauthorized access to record ID {record.id}",
        status="DANGER"
    )
    abort(403)