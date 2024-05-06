#!/bin/bash

# Run Django makemigrations
python manage.py makemigrations

# Apply Django database migrations
python manage.py migrate

#Create Django admin credentials
python manage.py createsuperuser --username fm_app_admin  --password fm_app_admin_pwd

#Start Django application
python manage.py runserver 0.0.0.0:8000

