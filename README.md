# TechNest E-commerce Platform

A modern e-commerce platform built with Django, featuring a sleek dark theme interface and real-time cart functionality.

## Features
- User authentication and authorization
- Product catalog with categories
- Real-time shopping cart
- Secure checkout process
- Responsive design
- Dark theme UI
- Accessibility features
- Promo code support
- Order notes functionality

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```

2. Create and activate a virtual environment:
```cmd
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install required packages:
```cmd
pip install -r requirements.txt
```

Required packages include:
- Django==4.2.7
- django-crispy-forms
- crispy-tailwind
- Pillow
- stripe
- python-dotenv
- django-allauth

4. Create a .env file in the root directory and add your environment variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`

## Project Structure
```
technest/
├── app/                    # Main application directory
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   └── views.py           # View logic
├── static/                # Global static files
├── media/                 # User-uploaded content
└── manage.py             # Django management script
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is open source and available under the MIT License.


#### created by:

** Mohamed Raslaan Najeeb **
- Villa ID: S2400578
- UWE ID: 24047953
- Email: s2400578@sudents.villacollege.edu.mv




