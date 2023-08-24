from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import UserModel
from .views import *
import datetime
import logging

COLORS = {
    "RED": "38;5;203m",
    "ORANGE": "38;5;202m", 
    "YELLOW": "33;5;202m",
    "GREEN": "38;5;113m",
    "BLUE": "34m",
    "MAGENTA": "38;5;170m",  
    "CYAN": "38;5;80m",
}

@shared_task
def task_one():
    users = UserModel.objects.all()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    for user in users:
        output = f"\033[{COLORS['CYAN']}{current_time} -Format: Username: {user.username}, Email: {user.email}\033[0m"
        logging.info(output)
        
    return f"\033[{COLORS['GREEN']}STATUS [✓]\033[0m"