class PasswordValidator:
    def __init__(self, pwd: str):
        self.pwd = pwd
        self.special_chars = {"_", "!", "@", "#", "$", "%", "&", "*", "?"}

    def check(self) -> bool:
        if len(self.pwd) < 10:
            return False

        return (
            sum(c.islower() for c in self.pwd) >= 2
            and sum(c.isupper() for c in self.pwd) >= 2
            and sum(c.isdigit() for c in self.pwd) >= 2
            and c in self.special_chars
            for c in self.pwd
        )
