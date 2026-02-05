import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def create_user(self, data):
        return requests.post(f"{self.BASE_URL}/users", json=data)

    def get_user(self, user_id):
        return requests.get(f"{self.BASE_URL}/users/{user_id}")
