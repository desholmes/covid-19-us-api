#!/bin/bash

# Run qa
if [ -n $QA ] && [ $QA == 1 ]; then
  pip install flake8==3.7.9
  echo ">>>> APP ENTRY POINT: Running QA"
  flake8
fi

# Run dev
if [ -n $DEV ] && [ $DEV == 1 ]; then
  echo ">>>> APP ENTRY POINT: Running in DEV mode"
  python manage.py runserver 0.0.0.0:$PORT
else
  echo ">>>> APP ENTRY POINT: Running in PROD mode"
  gunicorn --config gunicorn.py covid_19_us.wsgi
fi