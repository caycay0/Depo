#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Apply migrations
python manage.py migrate
# Run the application
gunicorn task_manager.wsgi
