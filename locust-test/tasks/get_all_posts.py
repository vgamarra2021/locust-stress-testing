
def getAllPosts(self, name):
    self.client.get("/posts", name=name)