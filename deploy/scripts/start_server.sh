#!/bin/bash
cd /home/ubuntu/CricketScheduleDevopsProject

# Start Gunicorn server
source venv/bin/activate
gunicorn --bind 127.0.0.1:8000 cricketschedule_project.wsgi:application &
