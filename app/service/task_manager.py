from datetime import datetime, timedelta
from celery import shared_task

from app.repository import Supplier
from app.repository import get_session
from utils.logger import logger


@shared_task
def send_message(supplier_id):
    """
    Celery task to send a message to a supplier.

    Args:
        supplier_id (int): The ID of the supplier to whom the message should be sent.
    """
    session = get_session()
    try:
        supplier = session.query(Supplier).get(supplier_id)
        if supplier:
            logger.info(f"Message sent: {supplier.name} ({supplier.phone})")
        else:
            logger.warning(f"Supplier with ID {supplier_id} not found.")
    finally:
        session.close()


def schedule_messages():
    """
    Schedule messages for all suppliers to be sent at 10:00 AM local time the next day.
    """
    session = get_session()
    try:
        now = datetime.utcnow()

        for supplier in session.query(Supplier).all():
            utc_offset = supplier.district.utc_offset
            local_time = now + timedelta(hours=utc_offset)

            send_time = local_time.replace(hour=10, minute=0, second=0, microsecond=0)
            if send_time < local_time:
                send_time += timedelta(days=1)
            delay = (send_time - now).total_seconds()

            send_message.apply_async((supplier.id,), countdown=int(delay))
            logger.info(f"Task for {supplier.name} ({supplier.phone}) scheduled at {send_time}.")
    except Exception as e:
        logger.error(f"Error while scheduling messages: {e}")
    finally:
        session.close()
