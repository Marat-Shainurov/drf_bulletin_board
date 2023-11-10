# General description
bulletin_board is a django-rest-framework project. \
The project is created as a backend part of an online bulletin board with adverts and reviews from the service users.
Main stack and tools: Djangorestframework, Postgresql, unittest, docker, djangorestframework-simplejwt.

# Install and usage
1. Clone the project from https://github.com/Marat-Shainurov/drf_bulletin_board to your local machine.

2. Build a new image and run the project container from the root project directory:
   - docker-compose build
   - docker-compose up

3. Read the project's documentation (swagger or redoc format):
   - http://127.0.0.1:8000/docs/
   - http://127.0.0.1:8000/redoc/

4. Go to the main page on your browser http://127.0.0.1:8000/ and start working with the app's endpoints.


# Testing fixture
You can load the fixture with several testing objects:
  - docker-compose exec app_bulletin python manage.py loaddata test_fixture.json \
     Available credentials:
     - superuser:
       {
         "email": "m_shaynurov@outlook.com",
         "password": "123"
       }
     - manager:
       {
         "email": "test_user@mail.ru",
         "password": "123"
       }
     - common user:
       {
         "email": "test_admin@mail.ru",
         "password": "123"
       }

# Project structure and models

1. *ads* - an app for adverts and reviews.
   - *Ad* - a model for adverts. 
   - *Review* - a model for reviews.\
     Related to Ad via FK.

2. *users* - users app.
   - CustomUser - customized User model.
   - UserManager class is overridden and customized (./users/manager.py)
   - The admin site is also overridden and customized. (./users/admin.py)

# Testing
-All the endpoints are covered by unittests in /<app>/tests.py \
- Run tests:\
  docker-compose exec app_bulletin python manage.py test

