## Prerequisites

Before proceeding with the setup, make sure you have the following prerequisites installed on your system:

1. Python (version 3.6 or higher)
2. MySQL or MariaDB (e.g., through XAMPP)
3. Git

## Setup Instructions

1. Clone the repository:
git clone https://github.com/narayan-d-zade/devsearch.git

2. Change into the project directory:
cd devsearch

3. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv env
source env/bin/activate

Install the required Django modules:
pip install Django mysqlclient pillow requests

Note: If you encounter any issues related to the mysqlclient module during installation, make sure you have the necessary system dependencies installed. You can refer to the mysqlclient documentation for specific instructions based on your operating system.

Configure the database:

Launch XAMPP and start the Apache and MySQL/MariaDB services.
Open your web browser and navigate to http://localhost/phpmyadmin.
Create a new database named devsearch.
Update the database settings in devsearch/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devsearch',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Apply database migrations:
python manage.py migrate

Create a superuser account (for accessing the admin panel):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Open your web browser and access http://localhost:8000 to view the Devsearch application.

Optional: Additional Django Modules
If you need to install additional Django modules, you can use the pip command with the module name. For example:
pip install <module_name>

Make sure to add the installed module to the INSTALLED_APPS list in the devsearch/settings.py file.

Conclusion
Congratulations! You have successfully set up the Devsearch project on your local or live system. You can now explore and customize the project according to your needs. If you encounter any issues during the setup process, please refer to the project documentation or reach out to the project maintainers for assistance.
