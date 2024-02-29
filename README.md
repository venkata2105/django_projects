# Django User Post Management System

This project is a  Django application for  user registrations, logins, and posts.

## Features

- User Registration: Allows users to register with a username, email, and password.
- User Login: it allows users to log in using their credentials which are created during registration.
- User Logout: it has logout operation..
- Post Management: Provides functionality to create, view, and retrieve posts.

## Setup

1. **Installation**:
   - Make sure you have Python and Django are installed in your machine .
   -
2. **Install Dependencies**:
   - Navigate to the project directory and install the required dependencies by running:
     ```
     pip install -r requirements.txt
     ```

3. **Database Setup**:
   - Run Django migrations to create necessary database tables:
     ```
     py manage.py makemigrations,py manage.py migrate
	 
3. **Creating Superuser**:
	- after migrations create super user to acces all the tables in admin interface
	```py manage.py createsuperuser```

4. **Running the Server**:
   - after doing migrations Start the Django development server by running:
     ```
     py manage.py runserver
     ```

5. **Accessing the Application**:
   - Once the server is running, you can access the application in your web browser at `http://127.0.0.1:8000/`.


