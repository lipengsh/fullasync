from celery import Celery

celery_app = Celery("worker", broker="amqp://0.0.0.0", backend="amqp://0.0.0.0")
celery_app.conf.task_routes = {"tasks.tasks.benchmark_rate": "main-queue"}
celery_app.autodiscover_tasks(['tasks'])