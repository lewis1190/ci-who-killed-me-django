# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Django 6.0.1 web application project called "ci-who-killed-me-django".

## Environment Setup

### Virtual Environment
- **Location**: `.venv/` (already configured)
- **Activation** (PowerShell): `.\.venv\Scripts\Activate.ps1`
- **Activation** (CMD): `.\.venv\Scripts\activate.bat`
- **Python Version**: Python 3.12

### Dependencies
- Django 6.0.1 is already installed
- Use `pip install -r requirements.txt` once requirements file is created
- Use `pip freeze > requirements.txt` to save current dependencies

## Common Development Commands

### Django Management Commands
```powershell
# Start development server
python manage.py runserver

# Create new Django app
python manage.py startapp <app_name>

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test

# Run specific test
python manage.py test <app_name>.tests.<TestClass>.<test_method>

# Collect static files (for production)
python manage.py collectstatic
```

## Architecture Guidelines

### Django Project Structure
When the project is initialized, it will follow Django's standard structure:
- **Project settings**: Located in the main project directory (settings.py, urls.py, wsgi.py, asgi.py)
- **Apps**: Separate Django apps for different features, each with models, views, templates, and tests
- **Static files**: CSS, JavaScript, and images typically in static/ directories
- **Templates**: HTML templates in templates/ directories
- **Media files**: User-uploaded content in media/ directory

### Database
- Default database will be SQLite (db.sqlite3) for development
- Use Django ORM for database interactions
- All database schema changes must go through migrations

### Settings Organization
- Keep sensitive settings (SECRET_KEY, database passwords) in environment variables
- Consider splitting settings.py into base.py, development.py, and production.py for different environments

### URL Routing
- Main URL configuration in project-level urls.py
- Include app-specific URLs using `include()` pattern
- Use `path()` and `re_path()` for URL patterns

### Views and Templates
- Use class-based views (CBVs) for CRUD operations where appropriate
- Function-based views (FBVs) for simpler logic
- Template inheritance for consistent layouts (typically base.html)

### Static Files and Media
- STATIC_URL and STATIC_ROOT for static files
- MEDIA_URL and MEDIA_ROOT for user uploads
- Use `{% static %}` template tag for static file references

## Development Workflow

### Starting a New Feature
1. Create a new Django app: `python manage.py startapp <app_name>`
2. Add app to INSTALLED_APPS in settings.py
3. Define models in models.py
4. Create and run migrations
5. Create views in views.py
6. Define URL patterns in urls.py
7. Create templates in templates/<app_name>/
8. Write tests in tests.py

### Testing
- Write tests in tests.py within each app
- Test models, views, forms, and business logic
- Use Django's TestCase class for database-backed tests
- Use Django's test client for view testing

### Code Organization
- Keep views focused and delegate business logic to model methods or separate service modules
- Use Django's form classes for form handling and validation
- Leverage Django's built-in authentication system
- Use mixins for reusable view functionality

## Windows-Specific Notes

- Use PowerShell or CMD for running commands
- File paths use backslashes (\\) on Windows
- Virtual environment activation differs from Unix systems (see Environment Setup above)
- SQLite database file will be created in project root as db.sqlite3
