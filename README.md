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
