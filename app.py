"""
Digital Archaeological Archive - Phase 1
Academic Graduation Project: Cybersecurity for Digital Archaeological Collections

Phase 1 Scope: Front-end presentation, navigation, and prototype archive views.
Security systems (SHA-256 integrity checks, authentication, upload sanitization)
are designated as planned modules and will be integrated in Phase 2.
"""

import os
from flask import Flask, render_template, flash, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Basic secret key for session handling and flash messages in local development.
# In production or later phases, this should be loaded securely from an environment variable.
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "academic-dev-key-phase1-only")


@app.route("/")
def home():
    """
    Renders the primary project homepage and dashboard overview.
    Displays project objectives, demonstration metrics, and planned security features.
    """
    return render_template("dashboard.html")


@app.route("/archive")
def archive():
    """
    Renders the archive demonstration catalog.
    Displays sample heritage records to preview layout and metadata architecture.
    """
    # Sample records designed to show how metadata and integrity hashes will display
    sample_records = [
        {
            "id": "ARC-2026-001",
            "title": "Excavation Site Trench Alpha - Stratigraphy Photograph",
            "category": "Archaeological Photograph",
            "date": "2024-03-15",
            "format": "TIFF (Lossless)",
            "hash_preview": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "status": "Demonstration Record"
        },
        {
            "id": "ARC-2026-002",
            "title": "Field Survey Notebook #4 - Late Bronze Age Ceramics",
            "category": "Historical Document",
            "date": "2023-11-02",
            "format": "PDF/A-1b",
            "hash_preview": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
            "status": "Demonstration Record"
        },
        {
            "id": "ARC-2026-003",
            "title": "Inscribed Limestone Stela - High-Resolution Surface Scan",
            "category": "Digital Heritage Asset",
            "date": "2025-01-20",
            "format": "OBJ / Texture Map",
            "hash_preview": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
            "status": "Demonstration Record"
        },
        {
            "id": "ARC-2026-004",
            "title": "Cuneiform Tablet Fragment - Analytical Micro-Photogrammetry",
            "category": "Archaeological Photograph",
            "date": "2024-08-09",
            "format": "RAW / DNG",
            "hash_preview": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
            "status": "Demonstration Record"
        }
    ]
    return render_template("archive.html", records=sample_records)


@app.route("/verify")
def verify_placeholder():
    """
    Placeholder route for the SHA-256 cryptographic verification utility.
    Informs visitors that this module is scheduled for Phase 2 implementation.
    """
    flash("The Cryptographic Integrity Verification engine is under active development for Phase 2.", "info")
    return redirect(url_for("home"))


@app.route("/login")
def login_placeholder():
    """
    Placeholder route for the user authentication and role-based access module.
    """
    flash("User Authentication and Role-Based Access Control (RBAC) will be integrated in Phase 2.", "info")
    return redirect(url_for("home"))


if __name__ == "__main__":
    # Runs the local development server with debug mode enabled for local testing
    app.run(host="127.0.0.1", port=5000, debug=True)