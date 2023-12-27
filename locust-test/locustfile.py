from locust import FastHttpUser, task, between, events
from task_sets import MobileTaskSet, PcTaskSet

@events.request.add_listener
def on_request(request_type, name, response_time, response_length, response, **kwargs):
    print(f"Request type: {request_type}, Name: {name}, Response time: {response_time}, Response content: {response.text}")

class MobileUser(FastHttpUser):
    wait_time = between(1, 2)
    
    tasks= {
        MobileTaskSet
    }
    
class PcUser(FastHttpUser):
    wait_time = between(1, 2)
    
    tasks= {
        PcTaskSet
    }