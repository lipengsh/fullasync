from core.celery import app 
from tasks.rates import some_rate

@app.task(acks_late=True)
def benchmark_rate(msg) -> str:
    print(msg)
    return some_rate("rates task");
