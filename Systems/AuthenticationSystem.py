import json


class AuthenticationSystem:
    with open('../Data/UserData.Json', 'r') as file:
        DATA = json.load(file)
        ADMIN = DATA["admin"]
        USER = DATA["user"]

    @classmethod

    def login(cls,username, password):
        if username == cls.ADMIN["username"]:
            print(cls.ADMIN["username"])
            print(cls.ADMIN["password"])
            print(username, password)
            if password == cls.ADMIN["password"]:
                return True
            else:
                return False
        elif username == cls.USER["username"]:
            print("hello")
            if password == cls.USER["password"]:
                return True
            else:
                return False
        else:
            print("ohno")
            return False




