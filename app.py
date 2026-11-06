"""
Ancient Heritage Digital Museum
Cybersecurity for Digital Archaeological Collections
Academic Graduation Project
"""

import os
import hashlib
from flask import Flask, render_template, flash, redirect, url_for, session, request
from translations import TRANSLATIONS

app = Flask(__name__)

# مفتاح الجلسة المشفر
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "ancient-mesopotamia-heritage-secret-key-2026")


@app.before_request
def setup_default_language():
    """
    جعل اللغة العربية هي اللغة الافتراضية للموقع
    Default: Arabic (RTL)
    """
    if "lang" not in session:
        session["lang"] = "ar"
    session["dir"] = "rtl" if session["lang"] == "ar" else "ltr"


@app.context_processor
def inject_museum_context():
    """حقن أدوات الترجمة والاتجاهات في كافة القوالب"""
    lang = session.get("lang", "ar")
    text_dir = session.get("dir", "rtl")

    def t(key, default=""):
        return TRANSLATIONS.get(lang, {}).get(key, default or key)

    return {
        "t": t,
        "current_lang": lang,
        "current_dir": text_dir,
        "alt_lang": "en" if lang == "ar" else "ar"
    }


@app.route("/set-language/<lang>")
def set_language(lang):
    """التبديل الفوري بين العربية والإنجليزية مع الحفاظ على الصفحة الحالية"""
    if lang in ["ar", "en"]:
        session["lang"] = lang
        session["dir"] = "rtl" if lang == "ar" else "ltr"

    referrer = request.referrer
    if referrer and referrer.startswith(request.host_url):
        return redirect(referrer)
    return redirect(url_for("home"))


@app.route("/")
def home():
    """بهو المتحف الرئيسي"""
    return render_template("dashboard.html")


@app.route("/archive")
def archive():
    """معرض المقتنيات الأثرية الرافدينية مع بيانات SHA-256 التشفيرية"""
    is_ar = session.get("lang", "ar") == "ar"

    # مقتنيات أثرية حقيقية مستوحاة من حضارة بلاد الرافدين
    mesopotamian_records = [
        {
            "id": "MESO-BAB-001",
            "title": "مسلة قوانين حمورابي - النقش البابلي الشامخ" if is_ar else "Stele of Hammurabi - High-Density Bas-Relief",
            "period": "العصر البابلي القديم (1750 ق.م)" if is_ar else "Old Babylonian Period (c. 1750 BCE)",
            "category": "مسلات حجرية ونقوش" if is_ar else "Stone Stelae & Inscriptions",
            "date": "2024-02-11",
            "format": "TIFF 64-bit / RAW",
            "hash_preview": "7a3b4c12d8e9f00123456789abcdef0123456789abcdef0123456789abcdef01",
            "status": "status_verified",
            "icon_type": "tablet"
        },
        {
            "id": "MESO-ASY-002",
            "title": "تمثال اللاماسو الحارس - قصر آشوربانيبال في نينوى" if is_ar else "Colossal Winged Bull (Lamassu) - Palace of Ashurbanipal",
            "period": "الإمبراطورية الآشورية الحديثة (700 ق.م)" if is_ar else "Neo-Assyrian Empire (c. 700 BCE)",
            "category": "نحت حجري فائق الضخامة" if is_ar else "Colossal Stone Sculpture",
            "date": "2024-05-18",
            "format": "OBJ / Point Cloud",
            "hash_preview": "3c91e4a68f0b12d789012345abcdef0123456789abcdef0123456789abcdef02",
            "status": "status_verified",
            "icon_type": "lamassu"
        },
        {
            "id": "MESO-SUM-003",
            "title": "لوح ملحمة كلكامش (اللوح الحادي عشر - الطوفان)" if is_ar else "Epic of Gilgamesh (Tablet XI - Flood Story)",
            "period": "عصر فجر السلالات السومرية / نينوى" if is_ar else "Early Sumerian / Nineveh Library",
            "category": "ألواح طينية مسمارية" if is_ar else "Cuneiform Clay Tablet",
            "date": "2024-08-04",
            "format": "TIFF Lossless / 3D Mesh",
            "hash_preview": "9f82d1b4a5c6e70123456789abcdef0123456789abcdef0123456789abcdef03",
            "status": "status_verified",
            "icon_type": "cuneiform"
        },
        {
            "id": "MESO-UR-004",
            "title": "قيثارة أور الذهبية الذهبية - مقابر أور الملكية" if is_ar else "Golden Lyre of Ur - Royal Cemetery of Ur",
            "period": "عصر فجر السلالات الثالث (2550 ق.م)" if is_ar else "Early Dynastic III (c. 2550 BCE)",
            "category": "معادن أثرية ومسكوكات" if is_ar else "Ancient Precious Metals",
            "date": "2025-01-12",
            "format": "Multispectral / DNG",
            "hash_preview": "e4f5a6b7c8d9e00123456789abcdef0123456789abcdef0123456789abcdef04",
            "status": "status_verified",
            "icon_type": "lyre"
        }
    ]
    return render_template("archive.html", records=mesopotamian_records)


@app.route("/verify")
def verify_placeholder():
    """مسار فحص السلامة التشفيرية"""
    flash(TRANSLATIONS[session.get("lang", "ar")]["msg_verify_placeholder"], "verified")
    return redirect(url_for("archive"))


@app.route("/login")
def login_placeholder():
    """مسار بوابة الدخول"""
    flash(TRANSLATIONS[session.get("lang", "ar")]["msg_login_placeholder"], "bronze")
    return redirect(url_for("home"))
@app.route("/security-lab")
def security_lab_portal():
    """
    بوابة ربط آمنة تعرض فهرس المختبر الأمني وتوجه إلى
    خادم PHP المعزول محلياً (http://127.0.0.1:8000)
    """
    lab_url = "http://127.0.0.1:8000"
    return render_template("security_lab.html", lab_url=lab_url)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
  