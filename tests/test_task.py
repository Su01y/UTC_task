import pytest
from celery import Celery

from config.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from app.service.task_manager import send_message


@pytest.fixture(scope='module')
def celery_app():
    app = Celery(
        "tasks",
        broker=CELERY_BROKER_URL,
        backend=CELERY_RESULT_BACKEND
    )
    return app


@pytest.mark.celery
def test_send_message(celery_app):
    supplier_id = 1

    result = send_message.apply_async((supplier_id,))

    assert result.status == "SUCCESS"
    assert result.result == "Сообщение отправлено: ООО «Ромашка» (+7 000 000 00 00)"
