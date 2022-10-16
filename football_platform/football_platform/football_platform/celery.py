from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_platform.settings')
app = Celery('football_platform') #celery初始化,名字为football_platform
app.conf.update(
    broker_url = 'redis://:245478@127.0.0.1:6379/1'
)

#自动去应用下找worker函数
app.autodiscover_tasks(settings.INSTALLED_APPS)