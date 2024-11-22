DATABASE_URL = "postgresql+psycopg2://user:password@db:5432/mydb"
CELERY_BROKER_URL = "amqp://rabbitmq"
CELERY_RESULT_BACKEND = DATABASE_URL
