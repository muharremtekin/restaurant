# Restaurant Management System

A comprehensive restaurant management system built with Django and Django REST Framework.

## 🚀 Features

- 👤 User Authentication and Authorization
- 🍽️ Menu Management
- 📅 Table Reservation System
- 🛒 Order Management
- 💬 Customer Reviews
- 📊 Admin Dashboard

## 🛠 Technologies

- Python 3.8+
- Django 5.0
- Django REST Framework
- MySQL
- Bootstrap 5
- JavaScript (ES6+)

## 📋 Prerequisites

```bash
Python 3.8 or higher
MySQL 8.0 or higher
pip (Python package manager)
virtualenv or venv (for virtual environment)
```

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/restaurant-project.git
cd restaurant-project
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Create .env file
```bash
# Example .env file
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=restaurant_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Start the development server
```bash
python manage.py runserver
```

## 📁 Project Structure

```
restaurant_project/
├── api/                    # API application
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── views.py           # API views
│   └── urls.py            # API URL patterns
├── authentication/         # Authentication application
├── static/                # Static files
│   ├── css/
│   ├── js/
│   └── img/
├── templates/             # HTML templates
├── manage.py
└── requirements.txt
```

## 🔌 API Endpoints

### Menu Operations
- `GET /api/menu-items/` - List all menu items
- `GET /api/menu-items/{id}/` - Retrieve specific menu item
- `POST /api/menu-items/` - Add new menu item (Admin only)
- `PUT /api/menu-items/{id}/` - Update menu item (Admin only)
- `DELETE /api/menu-items/{id}/` - Delete menu item (Admin only)

### Reservation Operations
- `GET /api/reservations/` - List user's reservations
- `POST /api/reservations/` - Create new reservation
- `PUT /api/reservations/{id}/` - Update reservation
- `DELETE /api/reservations/{id}/` - Cancel reservation

### Order Operations
- `GET /api/orders/` - List user's orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Retrieve order details

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Testing

To run the tests:
```bash
python manage.py test
```

## 🚀 Development

1. Make sure all required packages are installed:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

## 🔒 Security Features

- Token-based authentication for API access
- Environment variables for sensitive data
- Cross-Site Request Forgery (CSRF) protection
- SQL Injection protection through ORM
- Password hashing and security measures

## 📚 API Documentation

Detailed API documentation is available at `/api/docs/` when the server is running.

### Authentication

The API uses token-based authentication. To obtain a token:

```bash
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

Use the token in requests:
```bash
Authorization: Token your_token_here
```

## 🔧 Configuration

Configuration is managed through environment variables. Required variables:

- `DEBUG` - Debug mode (True/False)
- `SECRET_KEY` - Django secret key
- `DB_NAME` - Database name
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host
- `DB_PORT` - Database port

## 🛠 Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - REST API framework
* [MySQL](https://www.mysql.com/) - Database
* [Bootstrap](https://getbootstrap.com/) - Frontend framework
* [jQuery](https://jquery.com/) - JavaScript library

## 🔄 Version Control

This project uses Git for version control. Major versions are released as tags.

## 🤝 Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## ✨ Acknowledgments

* Hat tip to anyone whose code was used
* Django and DRF documentation
* Bootstrap team for the awesome UI framework
