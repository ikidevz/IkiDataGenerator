import hashlib
import string

from ..base_provider import BaseProvider

try:
    import bcrypt
except ImportError:
    bcrypt = None


class PasswordHashProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, min_length: int = 8, max_length: int = 16, rounds: int = 4, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.min_length = min_length
        self.max_length = max_length
        self.rounds = rounds

    def generate_non_blank(self, row_data=None):
        length = self.generate_integer(self.min_length, self.max_length)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
        plain_password = "".join(
            self.get_random_choices_by_list(all_chars, length))

        if bcrypt is not None:
            salt = bcrypt.gensalt(rounds=self.rounds)
            hashed_password = bcrypt.hashpw(
                plain_password.encode("utf-8"), salt)
            return hashed_password.decode("utf-8")

        digest = hashlib.sha256(
            f"{self.rounds}:{length}:{plain_password}".encode("utf-8")
        ).hexdigest()
        return f"$2b$04${digest[:60]}"
