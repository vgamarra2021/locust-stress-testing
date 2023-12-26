from locust import TaskSet, between, task
from tasks import createPost, deletePost, getAllPosts

class MobileTaskSet(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def getAll(self):
        getAllPosts(self, name="getAll MobileTaskSet")
    
