from flask import Flask, render_template, request, jsonify
import sqlite3
import re
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
load_dotenv()

import os

SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("EMAIL_USER")
app = Flask(__name__)
DB_PATH = "portfolio.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            email      TEXT NOT NULL,
            subject    TEXT,
            message    TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name    = (data.get("name", "") or "").strip()
    email   = (data.get("email", "") or "").strip()
    subject = (data.get("subject", "") or "").strip()
    message = (data.get("message", "") or "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "Name, email, and message are required."}), 400

    if not is_valid_email(email):
        return jsonify({"success": False, "error": "Please enter a valid email address."}), 400

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
            (name, email, subject, message)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"success": False, "error": "Something went wrong. Please try again."}), 500

    try:
        msg = MIMEMultipart()
        msg["From"]    = SENDER_EMAIL
        msg["To"]      = RECEIVER_EMAIL
        msg["Subject"] = f"New Portfolio Message from {name}"

        body = f"""
You received a new message from your portfolio website!

Name    : {name}
Email   : {email}
Subject : {subject or 'No subject'}

Message:
{message}

---
Sent from your portfolio contact form.
        """
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print(f"Email sent for message from {name}")

    except Exception as e:
        print(f"Email sending failed: {e}")

    return jsonify({"success": True, "message": "Thank you! I'll get back to you soon."})


@app.route("/api/projects", methods=["GET"])
def get_projects():
    projects = [
        {
            "id": 1,
            "title": "Virtual Shopping Assistant",
            "emoji": "🛒",
            "tagline": "AI-powered shopping with voice & text interactions",
            "description": (
                "A full-stack web app where users can search for products using "
                "natural language — either by typing or speaking. The app gives "
                "personalized recommendations and remembers what you were looking for."
            ),
            "real_world_use": (
                "Imagine browsing an online store and asking: Show me red shoes under 2000. "
                "This app does exactly that — making shopping faster and smarter."
            ),
            "features": [
                "Voice & text search using Web Speech API",
                "AI-style product recommendations based on user query",
                "RESTful Node.js backend with clean, modular routes",
                "MySQL database with normalized schema and optimized queries",
                "Session management to remember user preferences"
            ],
            "tech_stack": ["React.js", "Node.js", "MySQL", "REST API", "Web Speech API", "CSS3"],
            "category": "Full Stack",
            "github": "https://github.com/sruthimedavarapu",
            "demo": "#"
        },
        {
            "id": 2,
            "title": "Fake Account Detector",
            "emoji": "🔍",
            "tagline": "ML system that detects fraudulent social media accounts",
            "description": (
                "A machine learning application that analyzes a social media account's "
                "behaviour — posting patterns, follower ratios, and profile completeness — "
                "to predict whether it is genuine or fake, in real time."
            ),
            "real_world_use": (
                "Social media platforms like Instagram or Twitter use similar systems "
                "to remove bot accounts. This project demonstrates that exact concept "
                "using real ML techniques."
            ),
            "features": [
                "Ensemble ML model combining Random Forest + Logistic Regression",
                "Feature engineering pipeline analyzing 20+ account signals",
                "Real-time anomaly detection for sudden activity spikes",
                "Data preprocessing with Pandas (handling missing values, encoding)",
                "Model evaluation with Accuracy, Precision, Recall, F1-Score"
            ],
            "tech_stack": ["Python", "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "Jupyter"],
            "category": "Machine Learning",
            "github": "https://github.com/sruthimedavarapu",
            "demo": "#"
        },
        {
            "id": 3,
            "title": "Student Result Management System",
            "emoji": "📊",
            "tagline": "Web app to manage and display student marks & grades",
            "description": (
                "A simple but complete CRUD web application built with Flask and SQLite. "
                "Teachers can add student results, and students can view their grades "
                "through a clean dashboard."
            ),
            "real_world_use": (
                "Schools and colleges need systems to manage thousands of student records. "
                "This project shows you can build that — end to end — from database to UI."
            ),
            "features": [
                "Add, edit, delete, and view student records",
                "Automatic grade calculation (A, B, C based on marks)",
                "Search student by name or roll number",
                "SQLite database with proper schema design",
                "Responsive UI built with plain HTML, CSS, JavaScript"
            ],
            "tech_stack": ["Python", "Flask", "SQLite", "HTML5", "CSS3", "JavaScript"],
            "category": "Full Stack",
            "github": "https://github.com/sruthimedavarapu",
            "demo": "#"
        }
    ]

    return jsonify({"success": True, "projects": projects})


if __name__ == "__main__":
    init_db()
    print("Database initialized")
    print("Starting server at http://127.0.0.1:5000")
    app.run(debug=True)