#!/bin/bash
cd /home/ubuntu/CricketScheduleDevopsProject

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate
