class Login:
    """Dette er en class for login-siden"""
    def __init__(self, username: str, password: str, validate_user: str):
        self.username = username
        self.password = password
        self.validate_user = validate_user

    def get_username(self): return self.username
    def set_username(self, new_username): self.username = new_username

    def get_password(self): return self.password
    def set_password(self, new_password): self.password = new_password
    
    def get_validate_user(self): return self.validate_user
    def set_validate_user(self, new_validate_user): self.validate_user = new_validate_user

    def __str__(self):
        return f"{self.username}, {self.password}, {self.validate_user}"