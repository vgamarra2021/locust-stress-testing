import uuid

def createPost(self, name):
    data = {
        "title": f"Post Example #{uuid.uuid4()}",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries"
    }
    self.client.post("/posts", name=name, json=data)