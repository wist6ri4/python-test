from datetime import datetime

class User:
    def __init__(self, name, mail, point):
        self.name = name
        self.mail = mail
        self.point = point

    def add_point(self, point):
        self.point += point

user_2 = User("testUser", "mail@mail.com", 100)
user_2.add_point(100)
t = datetime.today()
print(user_2.point, t)
