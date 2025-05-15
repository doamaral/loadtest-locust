import os
from locust import HttpUser, task, between, LoadTestShape
from faker import Faker

fake = Faker()


class MessageLoadTester(HttpUser):
    wait_time = between(1, 2)
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def send_message(self):
        body = {
            "message": f"Hello, {fake.name()}!"
        }
        response = self.client.post("/log", json=body)
        print(response.status_code, response.text)


class CustomLoadShape(LoadTestShape):
    stages = [
        {'duration': 5, 'users': 5, 'spawn_rate': 1},
        {'duration': 10, 'users': 100, 'spawn_rate': 100},
        {'duration': 40, 'users': 20, 'spawn_rate': 20},
        {'duration': 60, 'users': 100, 'spawn_rate': 100},
        {'duration': 70, 'users': 20, 'spawn_rate': 20},
        {'duration': 90, 'users': 100, 'spawn_rate': 100},
        {'duration': 100, 'users': 20, 'spawn_rate': 20},
        {'duration': 120, 'users': 100, 'spawn_rate': 100},
        {'duration': 130, 'users': 20, 'spawn_rate': 20},
        {'duration': 150, 'users': 100, 'spawn_rate': 100}
    ]

    def tick(self):
        run_time = self.get_run_time()
        for i, stage in enumerate(self.stages):
            if run_time < stage["duration"]:
                print(
                    f"🕒 Running Stage {i+1}: {stage['users']} users, {stage['spawn_rate']} spawn rate")
                return (stage["users"], stage["spawn_rate"])
        print("🏁 Test Complete - No More Stages")
        return None
