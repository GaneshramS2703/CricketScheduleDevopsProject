#!/bin/bash
# Stop any running Gunicorn server
pkill -f gunicorn || true
