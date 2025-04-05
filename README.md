# Task Management API with Django REST Framework

This project is a Task Management API built with Django and Django REST Framework. This RESTful API allows users to register, authenticate, and manage personal tasks (Create, Read, Update, Delete). It also supports token-based authentication for secure access. This README covers setup and usage.

## Features Implemented

###  Project Setup & User Authentication
- Django project and `accounts` app initialized.
- Custom user model (`CustomUser`) created.
- Token-based authentication implemented using `rest_framework.authtoken`.
- User registration and login endpoints.

###  Task Management (CRUD)
- `Task` model created with fields: title, description, due date, status, priority.
- Full CRUD operations on tasks.
- Users can only manage their own tasks (permissions enforced).

###  Filtering & Search + Admin Panel
- Filtering tasks by status and priority.
- Search functionality on task title and description.
- Admin panel for viewing and managing all tasks (for superusers).

###  Token Authentication, API Security, and Documentation
- Enable Token Authentication (DRF)
- Secure API Endpoints
- Add API Documentation
- Test Endpoints (Using Postman)

### Final Testing, Debugging, and Deployment
- Final test of Endpoints
- Debugging
- Deploy to Heroku

### Prepare Final Report/ Documentation
- Project Overview
- API Usage Guide
- Screenshots from Postman
- Known Issues/ Future Improvements

## API Documentation

### 1. Authentication
#### Register
- URL: `/api/accounts/register/`
- Method: `POST`
- Request Body: `{"username": "user1", "password": "your_password"}`
- Response: `{"token": "user_auth_token"}`

#### Login
- URL: `/api/accounts/login/`
- Method: `POST`
- Request Body: `{"username": "user1", "password": "your_password"}`
- Response: `{"token": "user_auth_token"}`

### 2. Task Endpoints
#### Create Task
- URL: `/api/tasks/`
- Method: `POST`
- Headers: `Token required`
- Request Body: `{"title": "Do assignment", "description": "Finish ALX Backend", "status": "Pending", "priority": "High", "due_date": "2025-04-10"}`
- Response: `201 Created` `{
  "id": 1,
  "title": "Do assignment",
  "description": "Finish Django homework",
  "status": "Pending",
  "priority": "High",
  "due_date": "2025-04-10",
  "created_at": "2025-04-01T12:00:00Z",
  "updated_at": "2025-04-01T12:00:00Z",
  "user": 1
}`

#### List Tasks
- URL: `/api/tasks/`
- Method: `GET`
- Headers: `Token required`
- Response: `200 OK` `[
  {
    "id": 1,
    "title": "Do assignment",
    "description": "Finish Django homework",
    "status": "Pending",
    "priority": "High",
    "due_date": "2025-04-10",
    "created_at": "2025-04-01T12:00:00Z",
    "updated_at": "2025-04-01T12:00:00Z",
    "user": 1
  }
]`

#### Get Task by ID
- URL: `/api/tasks/<id>/`
- Method: `GET`
- Headers: `Token required`
- Response: `200 OK`

#### Update Task
- URL: `/api/tasks/<id>/`
- Method: `PUT` or `PATCH`
- Headers: `Token required`
- Request Body (example): `{
  "status": "Completed"
}`
- Response: `200 OK`

#### ❌ Delete Task
- URL: `/api/tasks/<id>/`
- Method: `DELETE`
- Headers: `Token required`
- Response: `204 No Content`

#### ⚙️ Admin Panel
- Accessible at `/admin/`
- Admin users can view and manage all tasks and users


















