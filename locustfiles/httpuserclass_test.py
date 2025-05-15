from locust import HttpUser, task, constant, TaskSet
from os import getenv
from faker import Faker

fake = Faker()

class SetOfTasks(TaskSet):
    @task
    def send_message(self):
        body = {
            "message": f"Hello, {fake.name()}!"
        }
        with  self.client.post("/log", json=body, verify=False) as response:
            print(response.status_code, response.text)


class MessageLoadTester(HttpUser):
    wait_time = constant(0.5)
    host = getenv("HOST", "http://localhost:8000")
    tasks = [SetOfTasks]


    