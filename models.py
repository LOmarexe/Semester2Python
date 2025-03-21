class User:
    def __init__(self, user_id, Name, Password, Email):
        self.id = None
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
    