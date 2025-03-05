import requests
import time

ip_address = "192.168.20.135"

class WLEDAPI():
    def __init__(self,ip_address):
        self.base_url = f"http://{ip_address}/json"

    def _get_request(self, slug):
        response = requests.get(self.base_url+slug,headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            json_content = response.json()
        return (json_content)

    def _post_request(self,slug, data):
        response = requests.post(self.base_url+slug,data=data,headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            json_content = response.json()
        return (json_content)
    
    def effects(self):
        return (self._get_request('/effects'))

    def info(self):
        return (self._get_request('/info'))

    def set_state(self,data):
        return(self._post_request('/state',data=data))

    def get_state(self):
        return (self._get_request('/state'))

    def on(self):
        self.set_state('{"on":true}')

    def off(self):
        self.set_state('{"on":false}')

    def full_brightness(self):
        self.set_state('{"bri":255}')

    def set_brightness(self,value):
        value = min(max(value,0),255)
        self.set_state('{"bri":'+str(value)+'}')

    def low_brightness(self):
        self.set_state('{"bri":5}')

    def set_transition(self):
        self.set_state('{"transition":0}')

    def set_effect(self,value):
        self.set_state('{"seg":[{"fx":'+str(value)+'}]}')

if __name__ == "__main__":
    api = WLEDAPI(ip_address)
    api.set_transition()
    api.set_effect(0)
    api.set_brightness(50)
    time.sleep(1)
    api.full_brightness()
    time.sleep(2)
    api.set_effect(184)

    
