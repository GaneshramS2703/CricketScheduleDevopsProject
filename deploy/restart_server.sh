#!/bin/bash

# Navigate to the project directory
cd /home/ubuntu/Cricketschedule_project/cricketschedule_project

# Activate the virtual environment
source venv/bin/activate

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Restart Gunicorn
pkill gunicorn
gunicorn --bind 0.0.0.0:8000 cricketschedule_project.wsgi:application --daemon

# Restart Nginx to apply any configuration changes
sudo systemctl restart nginx
