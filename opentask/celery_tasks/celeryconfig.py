from django.conf import settings
import os

# ===================================================
# 参考： https://www.jianshu.com/p/15e02fea4263
# 参考： https://github.com/celery/django-celery-beat
# ===================================================
# 为celery设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opentask.settings")

# 设置结果存储, django_celery_results 使用django orm 作为结果存储
# CELERY_RESULT_BACKEND = 'redis://:123456@localhost:6379/2'
CELERY_RESULT_BACKEND = 'django-db'  
# 设置代理人broker
BROKER_URL = 'redis://:123456@localhost:6379/1'
# celery 的启动工作数量设置
CELERY_WORKER_CONCURRENCY = 20
# 任务预取功能，就是每个工作的进程／线程在获取任务的时候，会尽量多拿 n 个，以保证获取的通讯成本可以压缩。
CELERYD_PREFETCH_MULTIPLIER = 20
# 非常重要,有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True
# celery 的 worker 执行多少个任务后进行重启操作
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
# 禁用所有速度限制，如果网络资源有限，不建议开足马力。
CELERY_DISABLE_RATE_LIMITS = True
# 指定任务接收的内容序列化类型
CELERY_ACCEPT_CONTENT = ['application/json'] 
# 任务序列化方式
CELERY_TASK_SERIALIZER = 'json' 
# 任务结果序列化方式
CELERY_RESULT_SERIALIZER = 'json' 
# 任务过期时间
CELERY_TASK_RESULT_EXPIRES =  60 * 60 * 24  
# 是否压缩
CELERY_MESSAGE_COMPRESSION = 'zlib' 



# celery beat配置
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = settings.TIME_ZONE
DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'




