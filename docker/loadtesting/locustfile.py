from locust import SequentialTaskSet, HttpUser, task

class DetectorTask(SequentialTaskSet):
    @task
    def detect(self):
        payload = {
            "carlength": 180,
            "carwidth": 70,
            "horsepower": 130,
            "brandavg": 3,
            "averagempg": 25
        }
        self.client.post('/send_carprice', json=payload)

class LoadTester(HttpUser):
    host = "https://ml-playground-235086122205.asia-south1.run.app"
    tasks = [DetectorTask]
    min_wait = 1000
    max_wait = 2000
