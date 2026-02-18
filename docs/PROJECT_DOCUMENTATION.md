Nairobi County Youth Job Link (NC-YJL)
Backend System Documentation
1. Project Overview

The Nairobi County Youth Job Link (NC-YJL) is a tech-driven workforce management platform designed to:

Connect youth to county infrastructure projects

Eliminate informal hiring practices

Ensure transparent recruitment

Track attendance digitally

Automate payments

Provide public accountability dashboards

This backend system is built using:

Django

Django REST Framework

JWT Authentication

Celery (async tasks)

Redis (task queue)

PostgreSQL (production DB)

Docker (containerization)

2. System Architecture

The system follows a modular architecture:

Users → Jobs → Applications → Verification → Payments → Dashboard

Core Apps
App	Responsibility
users	Authentication & role management
jobs	Job postings & skill requirements
applications	Hiring workflow
verification	Attendance & proof of work
payments	Payment processing
dashboard	Reporting & analytics
3. Authentication & Authorization
Authentication

JWT-based authentication

Endpoints:

/api/token/

/api/token/refresh/

Roles
Role	Permissions
Youth	Apply for jobs, check in
Official	Create jobs, hire/reject
Supervisor	Approve attendance, complete jobs

Role-based permissions enforced at ViewSet level.

4. Core Workflows
4.1 Job Lifecycle

Official creates job

Youth applies

Official hires

Supervisor verifies

Payment processed

Dashboard updates

4.2 Application Status Transitions
Pending → Hired → Completed
Pending → Rejected


Validation ensures:

No invalid transitions

No duplicate applications

Vacancy control enforced

4.3 Attendance Verification

One-to-one relationship with application

Geo-coordinates stored

Proof image required

Supervisor approval required

Prevents:

Ghost workers

Fake check-ins

Duplicate attendance

4.4 Payment Processing

Payment auto-created upon completion

Processed asynchronously via Celery

Status flow:

Pending → Processing → Paid / Failed


Ensures:

Non-blocking API

Retry capability

Financial audit trail

5. Dashboard & Transparency

Dashboard endpoints provide:

Total jobs

Total applications

Total completed jobs

Total payments made

Role-based statistics

This supports public accountability and reporting.

6. Production Configuration
Development

SQLite

Local Redis

DEBUG=True

Production

PostgreSQL

Redis

Gunicorn

Docker

Environment variables

Secure cookies

HTTPS enforcement

7. Security Considerations

JWT authentication

Role-based access control

Unique constraints

Transaction logging

Secure environment variable management

Async payment handling

Media file isolation

8. Future Enhancements

M-Pesa Daraja integration

SMS notifications

Swagger/OpenAPI documentation

Audit logs

CI/CD pipeline

Automated testing

Public analytics dashboard

9. Conclusion

The NC-YJL backend is built with scalability, transparency, and security in mind.

It is structured for:

Government deployment

High concurrency

Modular expansion

Production scaling