from celery import Celery

app = Celery('task', backend='redis://127.0.0.1:6379/1', broker='redis://127.0.0.1:6379/0')

@app.task
def add(x, y):
    return x + y
