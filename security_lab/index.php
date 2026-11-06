<?php
/**
 * Isolated Security Laboratory Portal
 * Ancient Heritage Digital Museum - Security Lab
 * Running on local isolated PHP server (127.0.0.1:8000)
 */
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: SAMEORIGIN");
?>
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بوابة المختبر الأمني المعزول | Cybersecurity Laboratory</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="lab_style.css">
</head>
<body>

    <header class="lab-header">
        <div class="lab-container header-flex">
            <div>
                <h1 class="lab-title">&#9884; المختبر الأمني للتطبيقات الأثرية</h1>
                <p class="lab-subtitle">Educational Web Application Security Laboratory • Isolated Testing Environment</p>
            </div>
            <a href="http://127.0.0.1:5000" class="btn-return">&larr; العودة للموقع الرئيسي (Flask)</a>
        </div>
    </header>

    <main class="lab-container">
        
        <!-- قسم ثغرات PHP الخلفية -->
        <section id="php-section" class="lab-section">
            <div class="section-title-wrap">
                <h2>1. ثغرات الواجهة الخلفية (PHP Server-Side Vulnerabilities)</h2>
                <span class="tag-badge">Backend Flaws</span>
            </div>

            <div class="lab-grid">
                <!-- SQL Injection -->
                <div class="vuln-card">
                    <span class="vuln-severity high">High Severity</span>
                    <h3>حقن الاستعلامات (SQL Injection)</h3>
                    <p>استغلال عدم استخدام استعلامات مهيأة (Prepared Statements) للوصول إلى سجلات أثرية محجوبة.</p>
                    <div class="card-links">
                        <a href="php/vulnerable/sqli_vulnerable.php" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="php/patched/sqli_patched.php" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- Reflected XSS -->
                <div class="vuln-card">
                    <span class="vuln-severity medium">Medium Severity</span>
                    <h3>البرمجة العابرة للمواقع (Reflected XSS)</h3>
                    <p>طباعة مدخلات البحث في الأرشيف دون تعقيم HTML Entity Encoding في الخادم.</p>
                    <div class="card-links">
                        <a href="php/vulnerable/reflected_xss_vulnerable.php" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="php/patched/reflected_xss_patched.php" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- IDOR -->
                <div class="vuln-card">
                    <span class="vuln-severity high">High Severity</span>
                    <h3>تجاوز الصلاحيات المباشر (IDOR)</h3>
                    <p>الوصول إلى وثائق تنقيب سرية بمجرد تغيير رقم المعرف <code>?record_id=</code> في الرابط.</p>
                    <div class="card-links">
                        <a href="php/vulnerable/idor_vulnerable.php" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="php/patched/idor_patched.php" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- CSRF -->
                <div class="vuln-card">
                    <span class="vuln-severity medium">Medium Severity</span>
                    <h3>تزوير الطلبات عبر المواقع (CSRF)</h3>
                    <p>تعديل حالة السجل الأثري دون التحقق من وجود رمز مضاد للتزوير (Anti-CSRF Token).</p>
                    <div class="card-links">
                        <a href="php/vulnerable/csrf_vulnerable.php" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="php/patched/csrf_patched.php" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- Path Traversal -->
                <div class="vuln-card">
                    <span class="vuln-severity critical">Critical Severity</span>
                    <h3>اجتياز المسارات (Path Traversal)</h3>
                    <p>قراءة ملفات النظام أو التكوين الداخلي عبر تمرير <code>../../</code> في اسم الملف المطلوب.</p>
                    <div class="card-links">
                        <a href="php/vulnerable/path_traversal_vulnerable.php" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="php/patched/path_traversal_patched.php" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- قسم ثغرات JavaScript الأمامية -->
        <section id="js-section" class="lab-section">
            <div class="section-title-wrap">
                <h2>2. ثغرات الواجهة الأمامية (JavaScript Client-Side Flaws)</h2>
                <span class="tag-badge">Client-Side Flaws</span>
            </div>

            <div class="lab-grid">
                <!-- DOM XSS -->
                <div class="vuln-card">
                    <span class="vuln-severity medium">Medium Severity</span>
                    <h3>DOM-Based XSS عبر innerHTML</h3>
                    <p>حقن نصوص برمجية في واجهة المستعرض عبر تفريغ مدخلات الوسم مباشرة دون تنقية.</p>
                    <div class="card-links">
                        <a href="javascript/vulnerable/dom_xss_vulnerable.html" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="javascript/patched/dom_xss_patched.html" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- Prototype Pollution -->
                <div class="vuln-card">
                    <span class="vuln-severity high">High Severity</span>
                    <h3>تلويث النماذج الأولية (Prototype Pollution)</h3>
                    <p>التلاعب بخصائص كائنات JavaScript الأساسية لترقية صلاحية باحث عادي إلى مسؤول.</p>
                    <div class="card-links">
                        <a href="javascript/vulnerable/prototype_pollution_vulnerable.html" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="javascript/patched/prototype_pollution_patched.html" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>

                <!-- Client-Side Storage Flaw -->
                <div class="vuln-card">
                    <span class="vuln-severity medium">Medium Severity</span>
                    <h3>التخزين غير الآمن في المتصفح (Insecure Storage)</h3>
                    <p>حفظ مفاتيح الجلسة أو بيانات حساسة داخل LocalStorage مما يعرضها للسرقة عند حدوث XSS.</p>
                    <div class="card-links">
                        <a href="javascript/vulnerable/client_storage_vulnerable.html" class="btn-vuln" target="_blank">&#9888; النسخة المصابة (Vulnerable)</a>
                        <a href="javascript/patched/client_storage_patched.html" class="btn-patch" target="_blank">&#10004; النسخة المحمية (Patched)</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- قسم تقارير الاختبارات الأمنية -->
        <section class="lab-section">
            <div class="section-title-wrap">
                <h2>3. تقارير الفحص والتقييم الأمني (Security Assessment Reports)</h2>
                <span class="tag-badge">Documentation</span>
            </div>
            <div class="reports-box">
                <ul>
                    <li><a href="reports/sql_injection_report.md" target="_blank">&#128196; تقرير اختبار ومعالجة حقن الاستعلامات (SQLi Assessment Report)</a></li>
                    <li><a href="reports/xss_vulnerabilities_report.md" target="_blank">&#128196; تقرير فحص ومعالجة ثغرات البرمجة العابرة للمواقع (XSS Report)</a></li>
                    <li><a href="reports/idor_access_control_report.md" target="_blank">&#128196; تقرير فحص كسر التحكم بالوصول والـ IDOR (Access Control Report)</a></li>
                    <li><a href="reports/comprehensive_security_assessment.md" target="_blank">&#128196; التقرير الأمني الجامعي الشامل لمنظومة الأرشيف (Comprehensive Security Audit)</a></li>
                </ul>
            </div>
        </section>

    </main>

</body>
</html>