from locust import HttpUser, task, constant, TaskSet, LoadTestShape
from faker import Faker

fake = Faker()

class SetOfTasks(TaskSet):
    @task
    def send_message(self):
        body = {
            "userID": f"{fake.uuid4()}",
            "sessionID": f"{fake.uuid4()}",
            "userCurrentInteraction": "How many cameras does iphone 16 have?",
            "deviceType": "iPhone 16",
            "plataform": "whatsapp",
            "locale": "pt_br",
            "message_type": "text",
        }
        with  self.client.post("/log", json=body, verify=False) as response:
            print(response.status_code, response.text)

class MessageLoadTester(HttpUser):
    wait_time = constant(0.5)
    tasks = [SetOfTasks]

class CustomLoadShape(LoadTestShape):
    # Set default parameters
    user_count = 500
    spawn_rate = 30
    run_time = 120  # in seconds

    def tick(self):
        # Stop the test after the specified run time
        run_time_elapsed = self.get_run_time()
        if run_time_elapsed > self.run_time:
            return None

        return (self.user_count, self.spawn_rate)


    