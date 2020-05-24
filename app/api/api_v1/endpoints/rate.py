from typing import Any

from fastapi import APIRouter

from app import schemas
from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/rates/", response_model=schemas.Msg, status_code=201)
def rates_celery(
    msg: schemas.Msg
) -> Any:
    """
    Call Rates Celery worker.
    """
    celery_app.send_task("app.worker.rates.benchmark_rate", args=[msg.msg])
    return {"msg": "Word received"}
