from celery_tasks.celery import app
import time


# 创建任务函数
@app.task
def my_task1(a, b, c):
    print("任务1函数正在执行....")
    time.sleep(10)
    return a + b + c

@app.task
def my_task2():
    print("任务2函数正在执行....")
    time.sleep(10)