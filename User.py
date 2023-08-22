class User():
    user_id : int
    def __init__(self, user_name, password, name, email, phone) -> None:
        self.user_name = user_name
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
