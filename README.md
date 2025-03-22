# AntiFraud Django Application

## Prerequisites

Ensure you have the following installed:
- Python 3.10+
- pip (Python package manager)
- virtualenv (recommended for dependency management)
- SQLite (comes pre-installed with Python)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:CraftbudStudios/breach-2025.git
cd breach-2025
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser
To create an admin user for managing the application:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### 6. Populate the Database (Optional)
If you want to add test data:
```bash
python populate_db.py
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
By default, the application will be available at `http://127.0.0.1:8000/`

### 8. Running Tests
```bash
python manage.py test
```

## Project Structure
```
.
├── antifraud/          # Main Django project settings and configurations
│   ├── settings.py     # Django settings file
│   ├── urls.py         # URL routing configuration
│   ├── wsgi.py         # WSGI entry point for deployment
├── main/               # Application logic (models, views, etc.)
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── urls.py         # Application-specific URL patterns
│   ├── admin.py        # Django admin configurations
│   ├── migrations/     # Database migrations
├── db.sqlite3          # SQLite database (if used)
├── manage.py           # Django's management script
├── generate_test_data.py # Script to generate test data
└── populate_db.py      # Script to populate the database
```
