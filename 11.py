import requests


token = 


class User():
    def __init__(self, user_id):
        self.alias = user_id
        self.friends = None
        self.user_id = None

     
    def update_id(self):
        user_id = self.alias
        if (isinstance(user_id, int)):
            self.user_id = user_id
            return self

        elif (user_id[:2] == "id"):
            user_id = user_id[2:]

        try:
            self.user_id = int(user_id)
        
        except ValueError:
            self.user_id = User.get_id_by_alias(user_id)

        if (self.user_id is None):
            print("User not created!")
            return None
        else:
            return self


    @staticmethod
    def get_id_by_alias(alias):
        '''Возвращает id пользователя по его screen_name, в случае ошибки - None'''
        response = requests.get("http://api.vk.com/method/users.get", 
            params={"user_ids": alias, 
                    "access_token": token,
                    "v": "5.124"
                    })

        response_parsed = response.json()
        if ("error" in response_parsed):
            print(response_parsed)
            return None
        else:
            return int(response_parsed["response"][0]["id"]) 


    def get_mutual_friends_normal(self, other):
        '''Этот метод работает, если бы токен был НОРМАЛЬНЫЙ, с разрешением на друзей'''
        print(self.user_id)
        print(other.user_id)
        response = requests.get("https://api.vk.com/method/friends.getMutual", 
            params={"source_uid": self.user_id, 
                    "target_uid": other.user_id,
                    "access_token": token,
                    "v": "5.124"
                    })

        if (response.status_code == 200):
            return response.json()["response"]

        '''Но токен кривой, поэтому извращаемся'''


    def get_mutual_friends_complex(self, other):
        '''Но токен кривой, поэтому извращаемся'''
        if (self.friends is None):
            self.get_friends()

        if (other.friends is None):
            other.get_friends()

        return list(set(map(lambda x: x.user_id, self.friends))\
            .intersection(set(map(lambda x: x.user_id, other.friends))))


    def get_friends(self):
        '''Обновляет данные о друзьях этого пользователя'''

        if (self.user_id is None):
            self.update_id()

        response = requests.get("https://api.vk.com/method/friends.get", 
            params={"user_id": self.user_id,
                    "access_token": token,
                    "v": "5.124"
                    })

        if (response.status_code == 200 and "error" not in response.json()):
            self.friends = set(map(lambda x: User(x).update_id(),
                                   response.json()["response"]["items"]))
            return self
        else:
            print(response.json())
            return None


    def __and__(self, other):
        return self.get_mutual_friends_complex(other)

    def __str__(self):
        return "https://vk.com/" + self.alias

a = User("ant1vlas")
b = User("shalomandra")

print(a.get_mutual_friends_complex(b))
print(a & b)
print(a)

