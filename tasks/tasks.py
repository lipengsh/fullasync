from core.celery_app import celery_app
from tasks.rates import some_rate

@celery_app.task(acks_late=True)
def benchmark_rate(msg:str) -> str:
    print(str)
    print("enter celery benchmark")
    return some_rate("rates task");
