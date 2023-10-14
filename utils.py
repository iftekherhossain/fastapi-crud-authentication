import json

class MyAuthentication:
    def get_valid_user(self,credentials):
        # print(credentials)
        with open("basic_auth_users.json",'rb') as f:
            users = json.load(f)
        for user_type in users:
            se_users = users[user_type] 
            for se_user in se_users:
                if se_user["username"] == credentials.username and se_user["password"] == credentials.password:
                    return user_type
        return None