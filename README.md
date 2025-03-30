# Task Management API with Django REST Framework

This project is a Task Management API built with Django and Django REST Framework. It allows users to register, authenticate, and manage their personal or professional tasks. This README covers setup and usage for the first 3 weeks of development.

## Features Implemented (Week 1–3)

###  Week 1: Project Setup & User Authentication
- Django project and `accounts` app initialized.
- Custom user model (`CustomUser`) created.
- Token-based authentication implemented using `rest_framework.authtoken`.
- User registration and login endpoints.

###  Week 2: Task Management (CRUD)
- `Task` model created with fields: title, description, due date, status, priority.
- Full CRUD operations on tasks.
- Users can only manage their own tasks (permissions enforced).

###  Week 3: Filtering & Search + Admin Panel
- Filtering tasks by status and priority.
- Search functionality on task title and description.
- Admin panel for viewing and managing all tasks (for superusers).
