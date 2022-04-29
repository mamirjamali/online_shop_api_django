from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print('sending 10k enalis...')
    print(message)
    sleep(10)
    print('email were successfully sent!')
