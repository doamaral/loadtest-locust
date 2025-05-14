from locust import HttpUser, task, between
from faker import Faker

fake = Faker()


class MessageLoadTester(HttpUser):
    wait_time = between(1, 2)

    @task
    def send_message(self):
        body = {
            "message": f"Hello, {fake.name()}!"
        }
        response = self.client.post("/log", json=body)
        print(response.status_code, response.text)