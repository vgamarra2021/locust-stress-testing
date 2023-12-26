from locust import TaskSet, between, task
from tasks import createPost, deletePost, getAllPosts

class PcTaskSet(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def getAll(self):
        getAllPosts(self, name="getAll PcTaskSet")
        
    @task
    def create(self):
        createPost(self, name="create PcTaskSet")
