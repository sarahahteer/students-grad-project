"""
نظام إدارة وحماية الأرشيف الأثري الرقمي
الملف: translations.py
الوصف: محرك الترجمة الثنائية (عربي / إنجليزي)
"""

TRANSLATIONS = {
    'ar': {
        # العامة وعناصر النظام
        'app_title': 'منظومة حماية الأرشيف الأثري الرقمي',
        'sub_title': 'نظام أمني لإدارة وتأمين وحفظ التراث الرقمي',
        'switch_lang': 'English',
        'lang_code': 'en',
        'direction': 'rtl',
        'home': 'الرئيسية',
        'login': 'تسجيل الدخول',
        'register': 'إنشاء حساب جديد',
        'logout': 'تسجيل الخروج',
        'status_online': 'النظام محمي ومشفر',
        
        # بوابات النظام
        'portal_user': 'بوابة الباحثين والمستخدمين',
        'portal_admin': 'لوحة الإدارة والتحكم الأمني',

        # شريط تنقل المستخدم
        'nav_user_dashboard': 'لوحتي الشخصية',
        'nav_archive': 'الأرشيف الأثري',
        'nav_my_uploads': 'مرفوعاتي الأثرية',
        'nav_profile': 'ملفي التعريفي',

        # شريط تنقل المسؤول
        'nav_admin_dashboard': 'لوحة تحكم المسؤول',
        'nav_user_management': 'إدارة المستخدمين',
        'nav_archive_management': 'إدارة الأرشيف',
        'nav_file_integrity': 'سلامة الملفات (SHA-256)',
        'nav_security_logs': 'السجلات الأمنية',
        'nav_suspicious': 'الأنشطة المشبوهة',
        'nav_backups': 'النسخ الاحتياطي',

        # شاشات الدخول والتسجيل
        'login_title': 'تسجيل الدخول للنظام الأمني',
        'login_subtitle': 'يرجى إدخال بيانات الاعتماد للوصول المشفر',
        'username': 'اسم المستخدم',
        'password': 'كلمة المرور',
        'confirm_password': 'تأكيد كلمة المرور',
        'full_name': 'الاسم الكامل',
        'email': 'البريد الإلكتروني',
        'role': 'نوع الحساب',
        'role_researcher': 'باحث أثري (Researcher)',
        'role_viewer': 'مستعرض / قارئ (Viewer)',
        'login_btn': 'تسجيل الدخول الآمن',
        'register_btn': 'إنشاء الحساب',
        'have_account': 'لديك حساب بالفعل؟ سجل دخولك',
        'no_account': 'ليس لديك حساب؟ أنشئ حساباً جديداً',
        
        # رسائل التنبيه
        'invalid_credentials': 'اسم المستخدم أو كلمة المرور غير صحيحة.',
        'account_disabled': 'تم تعطيل هذا الحساب من قبل مدير النظام لدواعٍ أمنية.',
        'login_success': 'تم تسجيل الدخول بنجاح. أهلاً بك!',
        'logout_success': 'تم تسجيل الخروج وتأمين الجلسة بنجاح.',
        'reg_success': 'تم إنشاء الحساب بنجاح، يمكنك الآن تسجيل الدخول.',
        'user_exists': 'اسم المستخدم أو البريد الإلكتروني مسجل بالفعل.',
        'pass_mismatch': 'كلمات المرور غير متطابقة.',
        'access_denied': 'غير مصرح لك بالوصول إلى هذه الصفحة (تم قيد المحاولة أمنياً).',

        # لوحة المؤشرات
        'welcome': 'مرحباً بك',
        'system_overview': 'نظرة عامة على الأمان والأرشفة',
        'total_records': 'إجمالي السجلات الأثرية',
        'verified_files': 'ملفات سليمة ومحققة (SHA-256)',
        'compromised_files': 'ملفات متلاعب بها أو مخترقة',
        'recent_logs': 'أحدث السجلات الأمنية',
        'security_status': 'حالة النظام الأمني',
        'secure_state': 'محمي ومستقر',
        'compromised_state': 'تنبيه: يوجد انتهاك لسلامة البيانات',
        'sha_hash': 'بصمة SHA-256',
        'view_details': 'عرض التفاصيل',
    },
    'en': {
        # General & System
        'app_title': 'Cybersecurity for Digital Archaeological Collections',
        'sub_title': 'Secure Digital Heritage Preservation & Integrity System',
        'switch_lang': 'العربية',
        'lang_code': 'ar',
        'direction': 'ltr',
        'home': 'Home',
        'login': 'Sign In',
        'register': 'Create Account',
        'logout': 'Sign Out',
        'status_online': 'System Encrypted & Protected',

        # Portals
        'portal_user': 'User & Researcher Portal',
        'portal_admin': 'Admin Security Control Panel',

        # User Navigation
        'nav_user_dashboard': 'My Dashboard',
        'nav_archive': 'Digital Archive',
        'nav_my_uploads': 'My Uploads',
        'nav_profile': 'My Profile',

        # Admin Navigation
        'nav_admin_dashboard': 'Admin Dashboard',
        'nav_user_management': 'User Management',
        'nav_archive_management': 'Archive Management',
        'nav_file_integrity': 'File Integrity (SHA-256)',
        'nav_security_logs': 'Security Logs',
        'nav_suspicious': 'Suspicious Activities',
        'nav_backups': 'Backup Management',

        # Auth screens
        'login_title': 'Secure System Authentication',
        'login_subtitle': 'Enter your credentials for encrypted system access',
        'username': 'Username',
        'password': 'Password',
        'confirm_password': 'Confirm Password',
        'full_name': 'Full Name',
        'email': 'Email Address',
        'role': 'Account Role',
        'role_researcher': 'Archaeological Researcher',
        'role_viewer': 'Viewer / Reader',
        'login_btn': 'Secure Sign In',
        'register_btn': 'Register Account',
        'have_account': 'Already have an account? Sign In',
        'no_account': 'Do not have an account? Register now',

        # Flash messages
        'invalid_credentials': 'Invalid username or password.',
        'account_disabled': 'This account has been disabled by security administrators.',
        'login_success': 'Logged in successfully. Welcome!',
        'logout_success': 'Session terminated safely.',
        'reg_success': 'Account created successfully. You may now log in.',
        'user_exists': 'Username or email already exists.',
        'pass_mismatch': 'Passwords do not match.',
        'access_denied': 'Access denied: You lack sufficient security clearance.',

        # Dashboard
        'welcome': 'Welcome',
        'system_overview': 'Security & Archive Overview',
        'total_records': 'Total Archaeological Records',
        'verified_files': 'Verified Files (SHA-256)',
        'compromised_files': 'Compromised / Altered Files',
        'recent_logs': 'Recent Security Logs',
        'security_status': 'Security Status',
        'secure_state': 'Secured & Stable',
        'compromised_state': 'Alert: Integrity Breach Detected',
        'sha_hash': 'SHA-256 Hash',
        'view_details': 'View Details',
    }
}

def get_text(lang, key):
    """جلب النص المترجم بحسب اللغة المحددة مع استرجاع نص بديل إذا لم يتوفر"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['ar']).get(key, key)