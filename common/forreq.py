import requests

class Requests():
    def __init__(self,method,url,headers=None,):
        if method=='get':
            self.res=requests.get(url=url,headers=headers,)
        elif method=='post':
            self.res=requests.post(url=url,headers=headers)

    def get_status_code(self):
        return self.res.status_code

    def get_json(self):
        return self.res.json()

if __name__ == '__main__':
    res=Requests(method='get',url='https://www.weseepro.com/api/v1/message/discovery/v1')
    print(res.get_status_code())