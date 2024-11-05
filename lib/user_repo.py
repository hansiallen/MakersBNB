class UserRepo:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, email, password):
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        user = {
            'id': user_id,
            'name': name,
            'email': email,
            'password': password
        }
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return list(self.users.values())

    def user_exists(self, email):
        return any(user["email"] == email for user in self.users.values())

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

