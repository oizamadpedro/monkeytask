from utils import utils as Utils
from auth.models.userModel import User, UserLogin

class authService:
    def createUser(user: User):
        user.password = Utils.hash_password(user.password)
        query = "insert into users(username, email, password) values (%s, %s, %s);"
        values = (user.username, user.email, user.password)
        createdUser = Utils.insDB(query, values)
        return createdUser

    def findUserByEmail(email):
        query = "select * from users where email = %s;"
        values = (email, )
        user = Utils.selDB(query, values)
        return user
    
    def findUserByUsername(username):
        query = "select * from users where username = %s;"
        values = (username, )
        user = Utils.selDB(query, values)
        return user