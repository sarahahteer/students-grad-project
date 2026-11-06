"""
Localization Catalog for Ancient Heritage Digital Museum
Cybersecurity for Digital Archaeological Collections
Default Language: Arabic (RTL) | Secondary: English (LTR)
"""

TRANSLATIONS = {
    "ar": {
        # الهوية والعلامة التجارية
        "museum_name": "متحف التراث الرقمي",
        "museum_sub": "الأمن السيبراني للمجموعات الأثرية والرافدينية",
        "portal_badge": "منصة الحفظ الرقمي والتحصين السيبراني",

        # التنقل
        "nav_home": "بهو المتحف",
        "nav_archive": "المعرض الأثري",
        "nav_verify": "فحص سلامة SHA-256",
        "nav_security": "قلعة الحماية",
        "nav_about": "عن المنصة والأطروحة",
        "nav_login": "بوابة الباحثين",
        "nav_admin": "لوحة الحاكم (الأدمن)",
        "lang_switch_label": "English",

        # رسائل النظام
        "msg_verify_placeholder": "محرك فحص السلامة التشفيرية المباشر جاهز للاختبار في المعرض الأثري.",
        "msg_login_placeholder": "بوابة المصادقة وتحديد أدوار الباحثين مؤمنة وتعمل ضمن بروتوكولات RBAC.",

        # الواجهة الترحيبية (Hero)
        "hero_badge": "مشروع تخرج نوعي • حماية التراث الحضاري العراقي والرافديني",
        "hero_title": "متحف بلاد الرافدين الرقمي الآمن",
        "hero_subtitle": "صون النقوش المسمارية واللقى التاريخية عبر التشفير السيبراني المتقدم",
        "hero_desc": "منظومة سيبرانية متحفية تعتمد خوارزميات التجزئة SHA-256، وحجرات التخزين المعزولة، والتحكم الصارم بالوصول (RBAC) لحماية أرشيف التراث الأثري من التلاعب، التزوير، والتلف الرقمي الصامت.",
        "btn_explore_museum": "دخول المعرض الأثري",
        "btn_security_protocol": "ميثاق الأمن السيبراني",

        # إحصائيات المعرض والمتحف
        "stats_heading": "السجل الأرشيفي للمتحف",
        "stats_tag": "مؤشرات المستودع الأثري",
        "stats_subtext": "إحصائيات فورية توثق المقتنيات الرقمية المودعة ومطابقتها للبصمات التشفيرية الأصلية.",
        "stat_total_records": "إجمالي المقتنيات الموثقة",
        "stat_total_sub": "أصول أثرية مفهرسة ومحمية",
        "stat_cuneiform": "الألواح والنقوش المسمارية",
        "stat_cuneiform_sub": "مسوحات ثلاثية وتوثيق عالي الدقة",
        "stat_manuscripts": "المخطوطات والوثائق",
        "stat_manuscripts_sub": "سجلات الحفريات والخرائط التاريخية",
        "stat_integrity_rate": "نسبة السلامة التشفيرية",
        "stat_integrity_sub": "مطابقة تامة لبصمة SHA-256",

        # أجنحة المجموعات المتحفية
        "collections_heading": "أجنحة المقتنيات التاريخية",
        "collections_subtext": "تصنيف علمي دقيق لحفظ وتوثيق الآثار وفق أحدث المعايير الدولية للأرشفة الرقمية.",
        "wing_1_title": "الألواح الطينية المسمارية",
        "wing_1_desc": "نصوص سومرية وبابلية، وسجلات تجارية وملحمية ممسوحة بتقنيات القياس التصويري المجهري (Photogrammetry).",
        "wing_1_format": "الأصول: RAW, TIFF, OBJ 3D",
        "wing_2_title": "النقوش والمسلات الآشورية",
        "wing_2_desc": "مسوحات السطوح الحجرية وجداريات نمرود ونينوى وتفاصيل نحت الثيران المجنحة (اللاماسو).",
        "wing_2_format": "الأصول: Point Cloud, RTI Scans",
        "wing_3_title": "سجلات التنقيب الأثري",
        "wing_3_desc": "دفاتر الحفريات الأصلية لبعثات أور وبابل ونفر، والخرائط الطبوغرافية لمواضع التنقيب التاريخية.",
        "wing_3_format": "الأصول: PDF/A-2b, TIFF Lossless",
        "wing_4_title": "المخطوطات والمسكوكات التاريخية",
        "wing_4_desc": "مسكوكات فجر السلالات والعهد البابلي والمخطوطات النادرة المحفوظة بأبعادها الطيفية الكاملة.",
        "wing_4_format": "الأصول: Multispectral, DNG",

        # بطاقات الأمن السيبراني
        "security_heading": "قلعة التحصين والأمن السيبراني",
        "security_subtext": "طبقات الحماية الصارمة المستوحاة من أسوار نينوى وبابل المنيعة لتأمين البيانات الأثرية الحساسة.",
        "sec_sha_title": "البصمة التشفيرية الثابتة (SHA-256)",
        "sec_sha_desc": "توليد بصمة رياضية ذات 256 بت لكل قطعة أثرية عند إيداعها. أي تغيير ولو بمقدار بت واحد في صورة اللوح المسماري يكشف العبث فوراً ويطلق إنذار عدم التطابق.",
        "sec_rbac_title": "إدارة الوصول وفق الأدوار (RBAC)",
        "sec_rbac_desc": "عزل صلاحيات الزوار العامين عن الباحثين المنقبين وأمناء المتحف. لا يمكن لأي مستخدم غير مخول تعديل السجلات أو الوصول لإحداثيات المواقع غير المنقبة.",
        "sec_vault_title": "الخزنة الرقمية المعزولة (Isolated Vault)",
        "sec_vault_desc": "تخزين الملفات الأثرية في خادم معزول خارج المسار العام لصفحات الويب، مع تنقية شاملة لأسماء الملفات وفحص التواقيع الثنائية (Magic Bytes) لمنع البرمجيات الخبيثة.",
        "sec_audit_title": "سجل الوقائع غير القابل للتلاعب",
        "sec_audit_desc": "تدوين كل عملية تصفح، فحص بصمة، تحميل، أو تسجيل دخول في سجل تدقيق محمي زمنياً لضمان المساءلة المؤسسية وتتبع أي نشاط مريب.",

        # السياق الأكاديمي ومثلث الحماية
        "about_badge": "الأطروحة والهدف الأكاديمي",
        "about_heading": "حماية ذاكرة الإنسانية في بلاد الرافدين",
        "about_p1": "تعرضت الآثار العراقية عبر العصور للنهب والتدمير، وأصبحت الوثائق والسجلات الرقمية هي الحصن الأخير لحفظ الهوية الوطنية والتاريخ الإنساني العالمي.",
        "about_p2": "إن اختراق مستودع أثري رقمي ليس مجرد حادث أمني اعتيادي، بل هو تهديد بهدم الدليل التاريخي، وتزوير مصدرية القطع لتسهيل تهريبها، وتدمير هوية الشعوب.",
        "cia_title": "تطبيق مثلث الحماية السيبرانية (CIA Triad)",
        "cia_conf_label": "السرية (Confidentiality):",
        "cia_conf_desc": "حجب إحداثيات المواقع الاستكشافية العذراء لمنع عصابات سرقة الآثار من نبشها وتخريبها.",
        "cia_integ_label": "السلامة (Integrity):",
        "cia_integ_desc": "استخدام بصمات SHA-256 لإثبات أن صورة اللوح الطيني وسجل فك شفرته المسمارية لم يتعرضا لأي تحريف.",
        "cia_avail_label": "التوافر (Availability):",
        "cia_avail_desc": "ضمان استمرارية عمل منصة الحفظ الرقمي للمراكز البحثية والجامعات على مدار العقود القادمة.",

        # صفحة المعرض الأثري
        "archive_badge": "المستودع الأثري المؤمن • فهرس المقتنيات",
        "archive_title": "سجل المقتنيات الأثرية المحمية",
        "archive_desc": "استعراض الأصول التراثية المودعة، وبيانات الوصف الفوقية (Metadata)، والبصمات التشفيرية المعتمدة لكل أصل أثري.",
        "archive_notice_title": "بروتوكول السلامة التشفيرية نشط:",
        "archive_notice_text": "يتم مطابقة بصمة SHA-256 آلياً للتأكد من عدم تعرض الأصول لأي تشويه أو تلاعب رقمي.",
        "btn_verify_item": "فحص البصمة الآن",
        "btn_upload_artifact": "إيداع مقتنى أثري جديد",
        "table_heading": "المقتنيات المفهرسة",
        "table_status_label": "نظام المراقبة:",
        "table_status_active": "يعمل بنشاط (حماية فورية)",
        "th_id": "رمز المقتنى الأثري",
        "th_preview": "المعاينة",
        "th_desc": "اسم ووصف الأصل التراثي",
        "th_period": "العصر التاريخي",
        "th_format": "صيغة الملف",
        "th_hash": "بصمة SHA-256 الرسمية",
        "th_status": "حالة السلامة التشفيرية",
        "status_verified": "سليم ومطابق 100%",
        "status_warning": "قيد التحقق",

        # الفوتر
        "footer_desc": "نظام سيبراني متقدم لحفظ وتأمين الأرشيف الأثري وتراث بلاد الرافدين ضد التهديدات الرقمية والهجمات السيبرانية والتلف الصامت.",
        "footer_wings": "أجنحة المتحف الرقمي",
        "footer_link_cuneiform": "جناح الألواح المسمارية",
        "footer_link_assyrian": "جناح النقوش الآشورية",
        "footer_link_excavations": "سجلات الحفريات والتنقيب",
        "footer_link_threats": "مصفوفة التهديدات السيبرانية",
        "footer_security_statement": "الميثاق الأمني للمتحف",
        "footer_security_text": "مشروع تخرج نوعي في تخصص الأمن السيبراني. صُممت جميع العمليات التشفيرية لحماية أصول التراث الوطني والإنساني.",
        "footer_copy": "© 2026 متحف التراث الرقمي | الأمن السيبراني للمجموعات الأثرية. جميع الحقوق البحثية محفوظة.",
        "footer_system_status": "حالة المنظومة: الحصن السيبراني نشط • SHA-256 مفعّل"
    },
    "en": {
        # Brand & Museum
        "museum_name": "Ancient Heritage Museum",
        "museum_sub": "Cybersecurity for Archaeological Collections",
        "portal_badge": "Digital Preservation & Cryptographic Fortress",

        # Navigation
        "nav_home": "Museum Grand Hall",
        "nav_archive": "Heritage Gallery",
        "nav_verify": "SHA-256 Verification",
        "nav_security": "Cyber Fortress",
        "nav_about": "About & Thesis",
        "nav_login": "Researcher Portal",
        "nav_admin": "Curator Console",
        "lang_switch_label": "العربية",

        # Messages
        "msg_verify_placeholder": "Cryptographic Integrity engine is operational in the Heritage Gallery.",
        "msg_login_placeholder": "Researcher authentication and RBAC gateways are secured and ready.",

        # Hero
        "hero_badge": "Academic Cybersecurity Project • Mesopotamian Heritage Defense",
        "hero_title": "Mesopotamian Digital Fortress",
        "hero_subtitle": "Preserving Cuneiform Tablets & Historical Relics via Advanced Cryptography",
        "hero_desc": "A museum-grade digital preservation fortress leveraging SHA-256 hashing algorithms, isolated archival vaults, and strict Role-Based Access Control (RBAC) to safeguard historical records against digital tampering, illicit forgery, and silent bit decay.",
        "btn_explore_museum": "Explore Relic Gallery",
        "btn_security_protocol": "Security Architecture",

        # Stats
        "stats_heading": "Museum Repository Registry",
        "stats_tag": "Archival Repository Metrics",
        "stats_subtext": "Live metrics tracking certified historical assets and their cryptographic baselines.",
        "stat_total_records": "Cataloged Heritage Assets",
        "stat_total_sub": "Preserved and encrypted items",
        "stat_cuneiform": "Cuneiform Clay Tablets",
        "stat_cuneiform_sub": "3D photogrammetric captures",
        "stat_manuscripts": "Historical Field Journals",
        "stat_manuscripts_sub": "Excavation logs and maps",
        "stat_integrity_rate": "Integrity Certification",
        "stat_integrity_sub": "Exact SHA-256 matches",

        # Wings
        "collections_heading": "Curated Museum Wings",
        "collections_subtext": "Scientific taxonomy engineered to preserve diverse categories of ancient human evidence.",
        "wing_1_title": "Cuneiform Clay Tablets",
        "wing_1_desc": "Sumerian and Babylonian administrative and literary tablets captured with micro-photogrammetric scanning.",
        "wing_1_format": "Assets: RAW, TIFF, OBJ 3D",
        "wing_2_title": "Assyrian Stone Reliefs",
        "wing_2_desc": "High-density surface scans of palace wall friezes and colossal Lamassu gatekeeper sculptures.",
        "wing_2_format": "Assets: Point Cloud, RTI Scans",
        "wing_3_title": "Excavation Field Logs",
        "wing_3_desc": "Original journals from Ur, Babylon, and Nippur expeditions, including stratigraphy registries.",
        "wing_3_format": "Assets: PDF/A-2b, TIFF Lossless",
        "wing_4_title": "Ancient Coins & Artifacts",
        "wing_4_desc": "Early Dynastic artifacts and rare coinages preserved under calibrated multispectral bands.",
        "wing_4_format": "Assets: Multispectral, DNG",

        # Security Framework
        "security_heading": "Cybersecurity Architecture",
        "security_subtext": "Impenetrable defensive layers inspired by the fortified walls of ancient Nineveh and Babylon.",
        "sec_sha_title": "SHA-256 Cryptographic Baseline",
        "sec_sha_desc": "Generates a unique 256-bit cryptographic digest upon relic deposition. A change in a single bit immediately triggers an integrity alert and isolates the asset.",
        "sec_rbac_title": "Role-Based Access Control (RBAC)",
        "sec_rbac_desc": "Separates public researchers from field archaeologists and chief curators. Conceals unexcavated geospatial coordinates from unauthenticated eyes.",
        "sec_vault_title": "Isolated Digital Vault",
        "sec_vault_desc": "Storage outside the public web root with filename sanitization, UUID mapping, and binary magic-byte inspection to defeat weaponized polyglot files.",
        "sec_audit_title": "Immutable Forensic Audit Trail",
        "sec_audit_desc": "Timestamped telemetry logging every view, hash verification, download, and login attempt to guarantee strict academic accountability.",

        # About / CIA
        "about_badge": "Academic Research Thesis",
        "about_heading": "Protecting the Memory of Mesopotamian Civilization",
        "about_p1": "Mesopotamian relics have endured millennia of physical peril. Digital twins—3D point clouds, field notebooks, and lossless imagery—are now the primary safeguard of human heritage.",
        "about_p2": "A cyber intrusion into an archaeological repository is not merely an IT outage; it is an existential threat aimed at altering historical provenance and facilitating antiquities trafficking.",
        "cia_title": "The CIA Triad in Cultural Heritage",
        "cia_conf_label": "Confidentiality:",
        "cia_conf_desc": "Shielding unexcavated site coordinates to prevent illicit looting and tomb raiding.",
        "cia_integ_label": "Integrity:",
        "cia_integ_desc": "Employing SHA-256 cryptographic baselines to prove historical documents remain untouched.",
        "cia_avail_label": "Availability:",
        "cia_avail_desc": "Ensuring continuous, uninterrupted scholarly access for generations of researchers.",

        # Archive
        "archive_badge": "Secure Archival Gallery • Preserved Assets",
        "archive_title": "Authenticated Archaeological Catalog",
        "archive_desc": "Browse preserved Mesopotamian records, metadata classifications, and cryptographic checksum fingerprints.",
        "archive_notice_title": "Cryptographic Integrity Active:",
        "archive_notice_text": "Real-time SHA-256 baseline verification is active across all cataloged historical records.",
        "btn_verify_item": "Verify Digest",
        "btn_upload_artifact": "Deposit Archaeological Asset",
        "table_heading": "Cataloged Artifacts",
        "table_status_label": "Surveillance:",
        "table_status_active": "Active Defense Protocol",
        "th_id": "Artifact Catalog ID",
        "th_preview": "Relic Specimen",
        "th_desc": "Artifact Title & Context",
        "th_period": "Historical Epoch",
        "th_format": "Digital Format",
        "th_hash": "SHA-256 Hash Digest",
        "th_status": "Integrity Status",
        "status_verified": "VERIFIED (Intact)",
        "status_warning": "Auditing",

        # Footer
        "footer_desc": "An advanced academic cybersecurity platform engineered to protect Mesopotamian heritage records against digital tampering, provenance forgery, and silent bit decay.",
        "footer_wings": "Preservation Wings",
        "footer_link_cuneiform": "Cuneiform Tablet Wing",
        "footer_link_assyrian": "Assyrian Relic Wing",
        "footer_link_excavations": "Field Excavation Logs",
        "footer_link_threats": "Cyber Threat Matrix",
        "footer_security_statement": "Security Assurance",
        "footer_security_text": "Cybersecurity Graduation Project. All cryptographic workflows are engineered for national and global cultural heritage protection.",
        "footer_copy": "© 2026 Ancient Heritage Digital Museum | Cybersecurity for Digital Archaeological Collections.",
        "footer_system_status": "System Status: Cyber Citadel Online • SHA-256 Active"
    }
}