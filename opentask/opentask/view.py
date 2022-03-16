
from django.http import JsonResponse

from django.db import transaction
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json, pytz

# def index(request):
#     return JsonResponse({"state": 1, "message": "welcome"})



def index(request):
    with transaction.atomic():
        save_id = transaction.savepoint()

        try:
            schedule, _ = CrontabSchedule.objects.get_or_create(
                    minute='30',
                    hour='*',
                    day_of_week='*',
                    day_of_month='*',
                    month_of_year='*',
                    timezone=pytz.timezone('Asia/Shanghai')
                )

            PeriodicTask.objects.create(
                    crontab=schedule,
                    name='Importing contacts2',
                    task='opentask.tasks.my_task1',
                    args=json.dumps([10, 20, 30]),
                )

            print('计划任务添加成功')
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            print('添加计划任务失败，错误原因：' + str(e))

    return JsonResponse({"state": 1, "message": "welcome"})