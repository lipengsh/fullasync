from app.core.celery_app import celery_app
from app.worker.rates import benchmark_rate


@celery_app.task(acks_late=True)
def benchmark_rate(word: str) -> str:
    return benchmark_rate()
