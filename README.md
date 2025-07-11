# Zeno Web — Online Tutoring Portal

**Zeno Web** is a Django-based web application built to manage class bookings, teacher assignments, and session tracking for a tutoring service. The platform supports a structured admin panel, teacher login system, and live dashboard updates.

## Features

- Class booking form with validation (email, date, phone)
- Email confirmation sent to the student upon booking
- Admin panel for registering teachers and assigning subjects
- Teacher login dashboard showing tutoring requests by subject
- Booking claim system: first-come-first-serve per subject
- PostgreSQL backend with environment-based configuration
- Clean, responsive Bootstrap design
- Separate views for admins, teachers, and students
- Modular structure with subject-based filtering
- Audit logging (in development)

## Tech Stack

- **Backend:** Django 5.x
- **Database:** PostgreSQL (originally SQLite)
- **Frontend:** HTML, Bootstrap 5
- **Email:** Gmail SMTP via Django
- **Deployment-ready:** AWS EC2 & RDS
- **Security:** CSRF protection, Django auth

## Project Structure

zeno_web/
├── bookings/ # Class booking logic
│ └── templates/bookings/
├── users/ # Teacher dashboard & login
│ └── templates/users/
├── zeno_web/ # Root settings and routing
│ └── templates/
│ ├── base.html
│ ├── home.html
│ └── partials/
├── .env # Hidden config
├── manage.py
└── requirements.txt

## Setup Instructions

1. **Clone the repo**


git clone https://github.com/your-username/zeno_web.git
cd zeno_web
Create virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Set up environment variables

Create a .env file in the root with:

ini
Copy
Edit
EMAIL_HOST_USER=your_gmail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DB_NAME=zeno
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost

Apply migrations
python manage.py makemigrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Run the server
python manage.py runserver

Visit http://localhost:8000 in your browser.

Notes
.env must be excluded from GitHub (.gitignore).
Use Google App Passwords for Gmail SMTP.
Forms are protected with CSRF middleware.
Teacher logins are restricted to accounts added via admin panel.


Future Roadmap
API endpoints for mobile and calendar integrations
Rich audit logs
Public deployment on AWS with custom domain + SSL
Role-based dashboards and schedule filters
Stripe/Razorpay payment integration
OAuth and multi-factor authentication

Contact
Developer: Parv S.
Email: zeno.learners@gmail.com
GitHub: github.com/parv-sr
