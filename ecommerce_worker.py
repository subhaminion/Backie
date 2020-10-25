from ecommerce_task import EmailTask

from worker import Worker

if __name__ == "__main__":
    email_task = EmailTask()
    worker = Worker(task=email_task)
    worker.start()
                