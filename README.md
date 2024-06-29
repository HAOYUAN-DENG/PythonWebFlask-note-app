
First python Web application note app using flask, bootstrap, sqlite 06/2024


# Flask Note-Taking Web Application

This is a simple web application built with Flask that allows users to register, log in, and manage their notes. Users can add, view, and delete notes in a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Frontend](#frontend)
- [Backend](#backend)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and login with Flask-Login.
- Note management: add, view, and delete notes.
- Secure password hashing with bcrypt.
- User authentication and session management.
- Responsive frontend using HTML, CSS, and JavaScript.

## Project Structure

```plaintext
flask_note_app/
├── __init__.py
├── auth.py
├── models.py
├── views.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── sign_up.html
├── static/
│   └── index.js
└── instance/
    └── config.py
```

## Routes

### Authentication:

- `GET /login`: Display login page.
- `POST /login`: Handle login form submission.
- `GET /sign-up`: Display sign-up page.
- `POST /sign-up`: Handle sign-up form submission.
- `GET /logout`: Log out the current user.

### Notes:

- `GET /`: Display the home page with a list of notes.
- `POST /add-note`: Add a new note.
- `POST /delete-note`: Delete a note.

## Frontend

### Templates

- **`base.html`**: Base template with navigation bar.
- **`home.html`**: Home page displaying user's notes and form to add new notes.
- **`login.html`**: Login page template.
- **`sign_up.html`**: Sign-up page template.

### Static Files

- **`index.js`**: JavaScript file containing the logic to handle note deletion.

## Backend

### `__init__.py`

Initializes the Flask application and configures extensions such as SQLAlchemy and Flask-Login.

### `auth.py`

Contains the routes for user authentication, including login, sign-up, and logout functionality.
The auth.py file handles user authentication, including routes for ```user login, sign-up, and logout.```
This file uses ```Flask-Login``` for session management and securely hashes passwords using Werkzeug's security module.
Summary of auth.py Functions:
Login:

-**Route:  /login**

Methods: GET, POST
Purpose: Renders the login page and handles login form submission.
Details:
On a GET request, it renders the login.html template.
On a POST request, it checks the user's credentials. If valid, logs in the user and redirects to the home page. If invalid, flashes an error message.
Logout:

-**Route: /logout**

Methods: GET
Purpose: Logs out the user.
Details:
Requires the user to be logged in (@login_required).
Logs out the user, flashes a success message, and redirects to the login page.
Sign-Up:

-**Route:  /sign-up**

Methods: GET, POST
Purpose: Renders the sign-up page and handles sign-up form submission.
Details:
On a GET request, it renders the sign_up.html template.
On a POST request, it validates the form data (e.g., email uniqueness, password match). If valid, creates a new user, logs them in, and redirects to the home page. If invalid, flashes an error message.


### `models.py`

Defines the database models for `User` and `Note`.

### `views.py`

Contains the main application routes for handling notes and rendering the home page.
The views.py file handles the main application logic, including ```displaying the home page and managing notes (adding and deleting notes).``` It uses Flask-Login to ensure that only authenticated users can access these functionalities.
Summary of views.py Functions:
Home:

-**Route: /**

Methods: GET, POST
Purpose: Displays the home page with a list of notes and a form to add new notes.
Details:
Requires the user to be logged in (@login_required).
On a GET request, it renders the home.html template with the current user's notes.
On a POST request, it processes the note addition form. If the note is valid, adds it to the database and flashes a success message. If invalid, flashes an error message.
Delete Note:

-**Route: /delete-note** 

Methods: POST
Purpose: Handles the deletion of a note.
Details:
Requires the user to be logged in (@login_required).
Receives the note ID as JSON in the request body.
Checks if the note exists and if the current user is the owner. If valid, deletes the note from the database and flashes a success message. If invalid, flashes an error message.
Returns a JSON response with status code 200.

### Frontend Integration
Home Page (home.html):

Displays a list of notes and provides a form to add new notes.
Each note has a delete button that calls the deleteNote JavaScript function.
JavaScript (index.js):

Defines the deleteNote function to send a POST request to the ```/delete-note route``` to delete a note.
Redirects to the home page after the note is deleted.

## Database

- **SQLAlchemy**: Used for database operations.
- **User Model**: Stores user information.
- **Note Model**: Stores notes linked to users.

