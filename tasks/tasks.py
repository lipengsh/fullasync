from core.celery_app import celery_app
from tasks.rates import some_rate

@celery_app.task(acks_late=True)
def benchmark_rate(msg) -> str:
    print(msg)
    return some_rate("rates task");
