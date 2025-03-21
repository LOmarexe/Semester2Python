class User:
<<<<<<< HEAD
    def __init__(self, user_id, Name, Password, Email):
        self.id = user_id
=======
    def __init__(self, Name, Password, Email):
        self.id = None
>>>>>>> f24dfc903eef70c01891381e2390b0cb250793e1
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
    