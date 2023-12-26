from locust import FastHttpUser, task, between
from task_sets import MobileTaskSet, PcTaskSet

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