# 🌐 Sruthi Medavarapu — Portfolio Website

A clean, professional portfolio website built with **Flask (Python)**, **SQLite**, **HTML**, **CSS**, and **JavaScript**.

---

## 📁 Folder Structure

```
sruthi_portfolio/
│
├── app.py                  ← Flask backend (main file to run)
├── requirements.txt        ← Python packages list
├── portfolio.db            ← SQLite database (auto-created on first run)
│
├── templates/
│   └── index.html          ← Main HTML page (Flask serves this)
│
└── static/
    ├── css/
    │   └── style.css       ← All styles and responsive design
    └── js/
        └── main.js         ← JavaScript (animations, API calls, form)
```

---

## 🚀 How to Run (Step by Step)

### Step 1 — Make sure Python is installed
```bash
python --version
# Should show Python 3.8 or higher
```

### Step 2 — Open a terminal and go to the project folder
```bash
cd sruthi_portfolio
```

### Step 3 — Install Flask
```bash
pip install -r requirements.txt
```
> If you get an error, try: `pip3 install flask`

### Step 4 — Run the app
```bash
python app.py
```

### Step 5 — Open your browser
Go to: **http://127.0.0.1:5000**

That's it! 🎉 Your portfolio is live locally.

---

## 🗄️ How the Database Works

- The SQLite database file (`portfolio.db`) is created automatically the first time you run `python app.py`.
- When someone submits the contact form, their message is saved in the `contacts` table.
- You can open this file with any SQLite browser (like **DB Browser for SQLite** — free app) to view messages.

To check messages via terminal:
```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('portfolio.db')
rows = conn.execute('SELECT * FROM contacts').fetchall()
for r in rows: print(r)
conn.close()
"
```

---

## 🌍 APIs in this Project

| Method | URL | What it does |
|--------|-----|--------------|
| GET | `/` | Serves the main HTML page |
| GET | `/api/projects` | Returns all projects as JSON |
| POST | `/api/contact` | Saves contact form submission to SQLite |

---

## 💬 INTERVIEW QUESTIONS & ANSWERS

These are common questions you'll get when showing this portfolio:

---

### Q1: "Can you walk me through your portfolio project?"

**Your answer:**
> "Sure! My portfolio is a full-stack web application. The frontend is built with HTML, CSS, and JavaScript — it's fully responsive and has sections for my skills, projects, and a contact form. The backend is Flask, a Python web framework. I used SQLite as the database to store contact form submissions. The projects are loaded dynamically using a REST API — the JavaScript fetches JSON from `/api/projects` and builds the cards on the page."

---

### Q2: "Why did you use Flask instead of Django?"

**Your answer:**
> "For a portfolio site, Flask is a great fit because it's lightweight and beginner-friendly. It doesn't come with a lot of built-in things you don't need, so it's easier to understand what each part does. Django would be more appropriate for a larger app with complex models and authentication."

---

### Q3: "What is a REST API? Where did you use it?"

**Your answer:**
> "A REST API is a way for the frontend (browser) to communicate with the backend (server) using standard HTTP methods like GET and POST. In my project, I have two API endpoints: `/api/projects` which returns project data as JSON, and `/api/contact` which receives the form data and saves it to the database."

---

### Q4: "Why did you use SQLite and not MySQL?"

**Your answer:**
> "SQLite is serverless — it stores everything in a single file and needs no installation or configuration. It's perfect for development and small projects like a portfolio. For a production app with many users, I would migrate to MySQL or PostgreSQL."

---

### Q5: "How does the contact form work?"

**Your answer:**
> "When the user fills the form and clicks Send, the JavaScript intercepts the submit event — preventing the default page reload. It collects the form values and sends them as a JSON POST request to `/api/contact` using the `fetch()` API. Flask receives the data, validates it (checks for empty fields and valid email format), then saves it to the SQLite database using parameterized queries to prevent SQL injection."

---

### Q6: "What is SQL injection and how did you prevent it?"

**Your answer:**
> "SQL injection is when an attacker puts SQL code into a form field to manipulate your database. I prevented it by using parameterized queries — instead of putting user input directly into the SQL string, I use placeholders `?` and pass the values separately. SQLite then treats the input as data, not as SQL code."

---

### Q7: "What does `debug=True` mean in Flask?"

**Your answer:**
> "When `debug=True`, Flask shows detailed error messages in the browser, and automatically restarts the server when I change the code. This is helpful during development. I would set `debug=False` in production so error details aren't exposed to users."

---

### Q8: "Can you explain your Virtual Shopping Assistant project?"

**Your answer:**
> "It's a full-stack web application where users can search for products using voice or text. I built the frontend with React.js and used the Web Speech API for voice input. The backend is Node.js with RESTful routes handling product search and session management. The database is MySQL with a normalized schema — I designed the tables with proper foreign keys and wrote optimized queries with JOINs. The project demonstrates end-to-end development: from database design to the UI."

---

## 🎯 Tips Before Your Interview

1. **Run the project** and keep it open in your browser — be ready to show it.
2. **Know every line** — if you can't explain a section, simplify it first.
3. **Mention real-world relevance** — "This is similar to how Amazon uses recommendation systems."
4. **Talk about what you'd add next** — "Next, I'd add user login and email notifications."
5. **GitHub** — push this to your GitHub profile before interviews.

---

*Built with 💛 Flask · SQLite · HTML · CSS · JavaScript*
