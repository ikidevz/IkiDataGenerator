import hashlib
import string

from ..base_provider import BaseProvider

try:
    import bcrypt
except ImportError:
    bcrypt = None


class PasswordHashProvider(BaseProvider):
    def __init__(
        self,
        blank_percentage: float = 0.0,
        min_length: int = 8,
        max_length: int = 16,
        rounds: int = 4,
        fast: bool = False,
        **kwargs
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.min_length = min_length
        self.max_length = max_length
        self.rounds = rounds
        # When True, use SHA256-based hashing instead of bcrypt (much faster for bulk generation)
        self.fast = fast

    def generate_non_blank(self, row_data=None):
        length = self.generate_integer(self.min_length, self.max_length)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
        plain_password = "".join(
            self.get_random_choices_by_list(all_chars, length))

        # Fast mode: use SHA256-based hash (suitable for bulk fixtures, not production security)
        if self.fast:
            digest = hashlib.sha256(
                f"v1:{self.rounds}:{length}:{plain_password}".encode("utf-8")
            ).hexdigest()
            return f"sha256${digest}"

        # Bcrypt mode (if available and not in fast mode)
        if bcrypt is not None:
            salt = bcrypt.gensalt(rounds=self.rounds)
            hashed_password = bcrypt.hashpw(
                plain_password.encode("utf-8"), salt)
            return hashed_password.decode("utf-8")

        # Fallback to SHA256 if bcrypt is not available
        digest = hashlib.sha256(
            f"{self.rounds}:{length}:{plain_password}".encode("utf-8")
        ).hexdigest()
        return f"$2b$04${digest[:60]}"
