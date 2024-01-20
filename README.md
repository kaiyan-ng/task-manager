#Task Management Application

## Overview
This project is a simple task manageemnt application built with Django. It allows users to add a new task, view all tasks, and mark a task as completed.

## Tech Stack
- **Backend Framework:** Django
- **Database:** SQLite (for development; can be replaced with other databases in production)
- **Frontend:** HTML, CSS (possibly with Bootstrap for styling), JavaScript
- **RESTful API:** Django REST Framework
- **Version Control:** Git (Hosted on GitHub)

## Steps to deploy application:
1. Clone the repository: `git clone https://github.com/kaiyan-ng/task-manager.git`
2. Navigate to project directory: `cd task-manager`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   Windows: `.\venv\Scripts\activate`
   MacOS: `source venv/bin/activate`
5. Install required python packages: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Run the development server: `python manage.py runserver`
8. Open the application in your web browser: http://localhost:8000/tasks


   
