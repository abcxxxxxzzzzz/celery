from celery import Celery
from celery_tasks import celeryconfig
from django.utils import timezone

import os
# 为celery设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openstask.settings")

## 创建celery app
app = Celery('celery_tasks')

# 从单独的配置模块中加载配置
app.config_from_object(celeryconfig)

# 设置app自动加载任务
app.autodiscover_tasks([
    'celery_tasks',
])

# 解决时区问题,定时任务启动就循环输出
app.now = timezone.now