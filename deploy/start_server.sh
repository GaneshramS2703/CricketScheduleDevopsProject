#!/bin/bash
sudo systemctl restart nginx
cd /home/ec2-user/yourapp
source venv/bin/activate
gunicorn --workers 3 --bind 0.0.0.0:8000 yourproject.wsgi:application
