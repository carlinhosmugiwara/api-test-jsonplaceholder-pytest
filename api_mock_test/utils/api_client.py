import requests


class APICLIENT:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        return response
    
    def post(self, endpoint, data=None):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=data)
        return response
