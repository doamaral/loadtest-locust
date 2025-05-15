from locust import User, task, constant
from faker import Faker

fake = Faker()


class UserTester(User):
    wait_time = constant(0.5)

    @task(7)
    def sample_task(self):
        print(f"Execute task: {fake.user_name()}")

    @task(3)
    def other_task(self):
        print("Other task")

class DifferentUserTester(User):
    wait_time = constant(5)

    @task(5)
    def sample_task(self):
        print(f"DifferentUserTester Execute task: {fake.user_name()}")

    @task(5)
    def other_task(self):
        print("DifferentUserTester Other task")  