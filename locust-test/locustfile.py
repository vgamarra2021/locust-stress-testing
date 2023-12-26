from locust import FastHttpUser, task, between, events
from task_sets import MobileTaskSet, PcTaskSet

def print_response(request_type, name, response_time, **kwargs):
    print(f"Request type: {request_type}, Name: {name}, Response time: {response_time}, Response content: {response.text}")

events.request_success.add_listener(print_response)
events.request_failure.add_listener(print_response)

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