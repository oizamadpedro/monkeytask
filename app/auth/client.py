from uplink import Consumer, json, get, post

@json
class UserClient(Consumer):

    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__(base_url)

    @post("/register/")
    def register(self, user_data):
        pass

    @post("/login/")
    def login(self, user_data):
        pass

    @get("/user/")
    def details(self, token):
        pass