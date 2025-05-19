import os
from locust import HttpUser, task, constant, LoadTestShape
from faker import Faker

fake = Faker()


class MessageLoadTester(HttpUser):
    wait_time = constant(1)
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def send_message(self):
        body = {
            "message": f"Hello, {fake.name()}!"
        }
        response = self.client.post("/log", json=body)
        print(response.status_code, response.text)


class CustomLoadShape(LoadTestShape):
    base_users = int(os.getenv("BASE_USERS", 10))
    peak_users = int(os.getenv("PEAK_USERS", 500))
    spawn_rate = int(os.getenv("SPAWN_RATE", 30))
    peak_duration = int(os.getenv("PEAK_DURATION", 20))
    base_duration = int(os.getenv("BASE_DURATION", 20))
    repeat_count = int(os.getenv("REPEAT_COUNT", 10))
    stages = []
    
    if not stages:
        for i in range(repeat_count):
            stages.append({"duration": (i * (peak_duration + base_duration)) + base_duration, "users": base_users, "spawn_rate": spawn_rate})
            stages.append({"duration": (i * (peak_duration + base_duration)) + peak_duration + base_duration, "users": ((i+1) * base_users), "spawn_rate": spawn_rate})
    
    print(stages)
#    
    def tick(self):
        run_time = self.get_run_time()
        for i, stage in enumerate(self.stages):
            if run_time < stage["duration"]:
                print(
                    f"🕒 Running Stage {i+1}: {stage['users']} users, {stage['spawn_rate']} spawn rate")
                return (stage["users"], stage["spawn_rate"])
        print("🏁 Test Complete - No More Stages")
        return None
    