# WorldCountries Django Project

This Django project manages world countries through a RESTful API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/worldCountries.git
   cd worldCountries

## Set Up the Database

### Prerequisites
- Ensure PostgreSQL is installed and running on your local machine.

### Steps to Set Up the Database

1. **Create PostgreSQL Database:**

   - Open a terminal or command prompt.
   - Log in to PostgreSQL as a user with sufficient privileges (e.g., `postgres`):

     ```bash
     psql -U postgres
     ```

   - Create a new database named `countriesdb`:

     ```sql
     CREATE DATABASE countriesdb;
     ```

2. **Update Database Credentials:**

   - Open `worldCountries/settings.py` in your preferred text editor.
   - Locate the `DATABASES` setting:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'countriesdb',
             'USER': 'postgres',
             'PASSWORD': 'postgres',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

   - Modify `USER`, `PASSWORD`, `HOST`, and `PORT` if your PostgreSQL configuration differs.

3. **Apply Database Migrations:**

   - Run the following command in your terminal to apply Django migrations and create necessary database tables:

     ```bash
     python manage.py migrate
     ```

   - This command ensures your database schema is up-to-date based on your Django project's models.
