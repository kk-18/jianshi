import requests

class Requests():
    def __init__(self,method,url):
        if method=='get':
            self.res=requests.get(url=url)
        elif method=='post':
            self.res=requests.post(url=url)

    def get_status_code(self):
        return self.res.status_code

    def get_json(self):
        return self.res.json()

