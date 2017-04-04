#!/bin/bash

source venv/bin/activate \
 && cd website \
 && python manage.py runserver 0.0.0.0:8080
