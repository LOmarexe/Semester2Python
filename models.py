class User:
    def __init__(self, user_id, Name, Password, Email):
        self.id = user_id
        self.name = Name
        self.password = Password
        self.email = Email
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password':self.password,
            'email' : self.email
        }
    