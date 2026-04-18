🟢 DAY 1 — DJANGO CORE + SETUP
🎯 GOAL (by end of today)

You should:

Understand how Django works internally
Run your first project
Create first API (/hello)
Know request → response flow
🧠 PART 1: DJANGO FLOW (VERY IMPORTANT)

Before coding, understand this:

🔄 What happens when user hits API?
Browser → URL → urls.py → View → Response → Browser

👉 Example:

GET /hello
↓
urls.py matches path
↓
View function runs
↓
Returns JSON
🏗️ PART 2: SETUP PROJECT
✅ Step 1: Install Django
pip install django
✅ Step 2: Create Project
django-admin startproject ecommerce
cd ecommerce
✅ Step 3: Run Server
python manage.py runserver

👉 Open:

http://127.0.0.1:8000/

If you see Django page → ✅ success

📁 PART 3: UNDERSTAND STRUCTURE
ecommerce/
│
├── manage.py        ❗ command center
├── ecommerce/
│   ├── settings.py  ⚙️ config
│   ├── urls.py      🔗 routing
│   ├── asgi.py      ⚡ async
│   └── wsgi.py      🌐 server
🧩 PART 4: CREATE FIRST APP
python manage.py startapp users

👉 Register it in settings.py:

INSTALLED_APPS = [
    'users',
]
🔗 PART 5: CREATE FIRST API
Step 1: Create View

Inside users/views.py:

from django.http import JsonResponse

def hello(request):
    return JsonResponse({
        "status": "success",
        "message": "Hello from Django 🚀"
    })
Step 2: Create App URLs

Create users/urls.py:

from django.urls import path
from .views import hello

urlpatterns = [
    path('hello/', hello),
]
Step 3: Connect to Main URLs

In ecommerce/urls.py:

from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),
]
✅ Final API

Open:

http://127.0.0.1:8000/api/hello/

👉 Expected:

{
  "status": "success",
  "message": "Hello from Django 🚀"
}
🧠 PART 6: INTERNAL UNDERSTANDING (INTERVIEW GOLD)
🔥 What is manage.py?

👉 CLI tool to run Django commands

🔥 What is urls.py?

👉 Router → maps URL → view

🔥 What is views.py?

👉 Business logic

🔥 What is settings.py?

👉 Configuration (DB, apps, middleware)

🔥 WSGI vs ASGI
Type	Use
WSGI	Sync apps
ASGI	Async (WebSockets, real-time)
🧪 MINI TASK (MANDATORY)

👉 Modify API:

Return this:

{
  "status": "success",
  "data": {
    "name": "Alok",
    "role": "Backend Developer"
  }
}
🎤 YOUR DAY 1 INTERVIEW

Answer at least 5–7 questions:


