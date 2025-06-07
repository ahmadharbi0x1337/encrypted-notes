# Encrypted Notes App (E_Notes)

A **secure, bilingual, and self-hostable note-taking application** built for the [CS50x Final Project](https://cs50.harvard.edu/college/2025/fall/), with a focus on:

- End-to-end encrypted note storage (using Fernet symmetric encryption)
- Clean, responsive UI using Bootstrap
- Arabic ↔ English toggle support
- Dark mode toggle for accessibility
- Dockerized for simple deployment anywhere

---

## 🌐 Live & Demo
### You can see me demonstration of the app in the following video: [Demo](https://youtu.be/Gb7nPGLdrG8)
### You can run the app locally with Python or self-host it via Docker. 

---

## 🚀 Features Overview

| Feature                   | Description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| 🛡️ End-to-End Encryption  | Notes are encrypted client-side before storing in the database using Fernet |
| 🔐 Authentication         | Users can register, log in, and manage their own encrypted notes            |
| 💡 Dark Mode              | Toggle dark/light themes using a persistent button                          |
| 🌍 Arabic Language        | Fully translated UI with right-to-left layout                               |
| 📦 Dockerized App         | Simple deployment using Docker containers                                   |
| 📋 CRUD Notes             | Create, edit, delete encrypted notes per user                               |

---

## 🧰 Technologies Used

| Layer       | Tech Stack                              |
| ----------- | --------------------------------------- |
| Backend     | Flask (Python)                          |
| Frontend    | HTML, Bootstrap 5, Font Awesome         |
| Database    | SQLite (via SQLAlchemy ORM)             |
| Auth        | Flask-Login, bcrypt                     |
| Encryption  | `cryptography.fernet`                   |
| Environment | `python-dotenv` (for loading .env vars) |
| Language    | JavaScript (for RTL + i18n + toggles)   |
| Deployment  | Docker                                  |

---

## 📁 Project Structure

/encrypted_notes/

├── app/

│ ├── __init__.py # Flask factory, extension setup

│ ├── auth.py # Login, logout, registration logic

│ ├── notes.py # Note CRUD routes

│ ├── models.py # SQLAlchemy models for User & Note

│ ├── crypto.py # Fernet-based encryption logic

│ ├── templates/ # HTML (Jinja2) templates

│ │ ├── layout.html

│ │ ├── login.html

│ │ ├── register.html

│ │ ├── notes.html

│ │ ├── create_note.html

│ │ └── edit_note.html

│ ├── static/

│ │ ├── css/styles.css # UI/UX + dark mode

│ │ ├── js/main.js # Dark mode + navbar logic

│ │ ├── js/language-toggle.js # i18n toggle logic

│ │ └── lang/translations.json # Arabic/English labels

├── config.py # App config (SECRET_KEY, DB URI)

├── run.py # App entry point

├── Dockerfile # Build instructions for deployment

├── requirements.txt # Python dependencies (incl. python-dotenv)

├── .env.example # Example environment vars (you now have it!)

├── README.md # ✅ Full usage and deployment instructions

├── utils/

| └── generate_master_key.py # Creates Fernet key (optional helper)

---

## ⚙️ Setup Instructions

### 🐍 Run Locally (Python 3.12+)

```bash
# 1. Clone the repo
$ git clone https://github.com/yourname/enotes
$ cd enotes

# 2. Create a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Generate a Fernet key
$ python utils/generate_master_key.py > .env

# 5. Run the Flask app
$ flask run
```

Then visit: `http://localhost:5000`

---

### 🐳 Run with Docker

```bash
# Build the image
$ docker build -t encrypted-notes-app .

# Run it (make sure you have .env in the root directory)
$ docker run --env-file .env -p 5000:5000 encrypted-notes-app
```

> ⚠️ **Note:** This assumes you have a `.env` file with the following variables:
> 
> ```env
> SECRET_KEY=your-secret
> FERNET_KEY=your-generated-fernet-key
> ```
> 
> See `.env.example` for the required format.

Then open: `http://localhost:5000`

---

## 📝 Usage

- Register a new account
- Log in to your personal dashboard
- Create, edit, and delete encrypted notes
- Use the 🌙 **dark mode** and 🌐 **language toggle** in the navbar

---

## 🔒 Security Notes

- 🔐 All note content is encrypted using Fernet (`cryptography.fernet`)
- Passwords are hashed using `bcrypt`
- Session management is handled via `Flask-Login`
- Future improvements can include CSRF protection using Flask-WTF

---

## 🏗️ Future Improvements

- Password reset and 2FA
- Export encrypted archive
- Markdown note support
- Note search and tagging
- User profile management

---

## 🧑‍🎓 CS50x Final Project Submission

This project was built as a final project for CS50x:

- ✅ 200+ lines of original code
- ✅ Authentication and database integration
- ✅ Web UI with dynamic backend
- ✅ Dockerized for portability

---

## 📜 License

MIT License. Feel free to fork, use, and improve it!

---

## 🙏 Acknowledgements - Thanks To:

- Harvard's CS50x for the opportunity
- Flask, Bootstrap, Font Awesome, JavaScript, and OpenAI for the guidance
