Nairobi County Youth Job Link (NC-YJL) Backend

A production-ready Django REST API for managing transparent youth recruitment and workforce payments for county infrastructure projects.

🚀 Features

JWT Authentication

Role-Based Access Control

Job Management System

Application Workflow Engine

Attendance Verification with Proof Upload

Asynchronous Payment Processing (Celery)

Dashboard & Analytics

Dockerized Deployment

Production-Ready Configuration

🏗 Tech Stack

Django

Django REST Framework

PostgreSQL

Celery

Redis

Gunicorn

Docker

📦 Project Structure
users/         → Authentication & roles
jobs/          → Job management
applications/  → Hiring workflow
verification/  → Attendance system
payments/      → Payment engine
dashboard/     → Analytics
config/        → Project configuration

🔐 Authentication

JWT-based authentication:

POST /api/token/
POST /api/token/refresh/


Use:

Authorization: Bearer <access_token>

🧪 Core API Endpoints
Users
POST   /api/users/register/
GET    /api/users/me/

Jobs
GET    /api/jobs/
POST   /api/jobs/
GET    /api/jobs/matched/

Applications
POST   /api/applications/
PATCH  /api/applications/{id}/hire/
PATCH  /api/applications/{id}/reject/
PATCH  /api/applications/{id}/complete/

Attendance
POST   /api/attendance/
PATCH  /api/attendance/{id}/approve/

⚙️ Local Development Setup
1️⃣ Clone Repository
git clone <repo-url>
cd ncyjl-backend

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Redis
redis-server

6️⃣ Run Celery Worker
celery -A config worker -l info

7️⃣ Start Server
python manage.py runserver

🐳 Docker Setup
docker-compose build
docker-compose up

📊 Architecture Overview
Youth → Apply → Hire → Verify → Complete → Payment → Dashboard


This ensures:

Transparent recruitment

Attendance verification

Controlled payment release

Public accountability

🔒 Security

JWT authentication

Role-based access

Secure environment variables

Async payment processing

Production-ready settings

📌 Future Improvements

M-Pesa Daraja integration

SMS notifications

Swagger API docs

CI/CD pipeline

Unit & integration testing

Cloud deployment automation

👨‍💻 Author

Developed as part of a capstone project focused on building scalable backend systems for public sector digital transformation.