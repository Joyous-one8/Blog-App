# 📝 Blog API with FastAPI

This is a simple Blog API built using **FastAPI**, **SQLAlchemy**, and **JWT authentication**. It provides endpoints for user registration, login, creating blogs, and more.

---

## 🚀 Features

- ✅ User registration
- ✅ Secure login with hashed passwords
- ✅ JWT-based authentication
- ✅ CRUD operations for blogs
- ✅ FastAPI + SQLAlchemy integration
- ✅ Modular route structure

---

## 📁 Project Structure

app/
│
├── main.py # App entrypoint
├── requirements.txt # Dependencies
│
├── blog/
│ ├── database.py # DB setup
│ ├── hashing.py # Password hashing
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── token.py # JWT token generation
│
│ └── routers/
│ ├── blog.py # Blog routes
│ ├── user.py # User routes
│ └── authentication.py # Auth routes

---

## 🧪 Endpoints Overview

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| POST   | `/user/`         | Register new user      |
| POST   | `/login/`        | Login + get JWT token  |
| GET    | `/blog/`         | List all blogs         |
| GET    | `/blog/{id}`     | Get blog by ID         |
| POST   | `/blog/`         | Create a new blog      |
| PUT    | `/blog/{id}`     | Update a blog          |
| DELETE | `/blog/{id}`     | Delete a blog          |

---

## 🔐 Authentication

- Use `/login` with:
  - `username` → user's email
  - `password` → plaintext password
- You’ll receive a JWT token.
- Add the token as a Bearer token to access protected routes.

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/Blog-App.git
cd Blog-App/app

# Create virtual env
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload

🧠 Tech Stack
Python 3.11+

FastAPI

SQLAlchemy

SQLite (default DB)

JWT + OAuth2PasswordBearer

Pydantic


📫 Author
Joy Jain

GitHub: Joyous-one8