from celery import Celery

app = Celery("worker", broker="amqp://0.0.0.0", backend="amqp://0.0.0.0")
app.conf.task_routes = {"tasks.tasks.benchmark_rate": "main-queue"}
app.autodiscover_tasks(['tasks'])