from locust import HttpUser, task, constant
from os import getenv
from faker import Faker

fake = Faker()


class MessageLoadTester(HttpUser):
    wait_time = constant(0.5)
    host = getenv("HOST", "http://localhost:8000")

    @task
    def send_message(self):
        body = {
            "message": f"Hello, {fake.name()}!"
        }
        response = self.client.post("/log", json=body)
        print(response.status_code, response.text)