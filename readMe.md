# Event Management System

## Overview

The Event Management System is a web application built using Django, designed to manage events with functionalities such as creating events, listing events, and viewing event details. This README provides an overview of how to set up and use the application.

## Features

- **Create Events:** Users can create new events by filling out a form with details such as title, description, location, start date, end date, and capacity.
- **List Events:** Displays a list of all events with basic information like title, date, and location.
- **View Event Details:** Clicking on an event from the list provides detailed information about the event including its description, dates, and available capacity.

## Technologies Used

- **Backend Framework:** Django
- **Frontend Framework:** HTML (with Django templates) and Tailwind CSS for styling
- **Database:** SQLite (for development, can be swapped with PostgreSQL for production)
- **Deployment:** Docker and Heroku (or alternative cloud service)

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   ```
2. **Set up a virtual environment:**

   ```
   cd event_management_system
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```
   python manage.py runserver
   ```

6. **Run the development server:**

   ```
   python manage.py runserver
   ```

7. **Access the application:**
   Open a web browser and go to http://127.0.0.1:8000/ to view the application.

## Folder Structure

```
event_management_system/
├── events/                     # Django app for events management
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files (e.g., images, CSS)
│   ├── templates/              # HTML templates for rendering views
│   ├── forms.py                # Forms for event creation and editing
│   ├── models.py               # Database models for events
│   ├── urls.py                 # URL routing for the app
│   └── views.py                # View functions for handling requests
├── event_management_system/     # Project settings and configuration
│   ├── settings.py             # Django settings file
│   ├── urls.py                 # Main URL routing for the project
│   └── wsgi.py                 # WSGI config for deployment
├── static/                      # Project-wide static files (e.g., CSS, JS)
├── templates/                   # Project-wide templates (e.g., base.html)
├── venv/                        # Virtual environment (ignored by Git)
├── manage.py                    # Django's command-line utility
└── README.md                    # Project documentation (you are here)

```

## Contributing

-natejonesiii
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or a pull request on GitHub.

## License

This project is licensed under the MIT License.
