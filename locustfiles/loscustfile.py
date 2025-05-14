from locust import HttpUser, task, between, LoadTestShape


class MessageLoadTester(HttpUser):
    wait_time = between(1, 3)

    @task
    def send_message(self):
        body = {
            "message": "Hello, World!"
        }
        response = self.client.post("/log", json=body)
        print(response.status_code, response.text)
