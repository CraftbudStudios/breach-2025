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


# Frontend Setup Instructions

## How to Use

1. **Unzip the Frontend Files**  
   Extract the frontend project into the  directory.

2. **Install Dependencies**  
   Navigate to the frontend folder and run:  
   ```sh
   npm install

```
npx run dev
```
