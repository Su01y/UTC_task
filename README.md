# Проект: Рассылка сообщений с учетом часового пояса

## Описание проекта

Этот проект предназначен для автоматической отправки сообщений поставщикам в зависимости от их часового пояса. Система использует `Celery` для выполнения отложенных задач, а также `RabbitMQ` в качестве брокера и `PostgreSQL` для хранения данных. Основной API реализован с использованием `FastAPI`.

## Основные компоненты

### 1. **FastAPI**
FastAPI используется для создания веб-интерфейса и управления задачами. 

### 2. **Celery**
Celery используется для обработки фоновых задач, таких как отложенная отправка сообщений.

### 3. **RabbitMQ**
RabbitMQ служит брокером сообщений, обеспечивая надежную постановку задач в очередь.

### 4. **PostgreSQL**
База данных для хранения информации о поставщиках, часовых поясах и других данных.

## Контейнеризация

Проект упакован в контейнеры с использованием Docker. Основные сервисы включают:

- **web**: сервис, содержащий API FastAPI и Celery.
- **rabbitmq**: брокер сообщений RabbitMQ.
- **db**: база данных PostgreSQL.
