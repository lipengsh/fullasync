from typing import Any
from fastapi import APIRouter
from core.celery_app import celery_app

router = APIRouter()


@router.post("/", status_code=201)
def rates_celery(
) -> Any:
    """
    Call Rates Celery worker.
    """
    celery_app.send_task("tasks.tasks.benchmark_rate", args=["hello"])
    return {"msg": "Word received"}
