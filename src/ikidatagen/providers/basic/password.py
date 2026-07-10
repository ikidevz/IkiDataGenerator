import string
from ..base_provider import BaseProvider


class PasswordProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, min_length: int = 8, upper_num: int = 1, lower_num: int = 1, numbers_num: int = 1, symbols_num: int = 1, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.min_length = min_length
        self.upper_num = upper_num
        self.lower_num = lower_num
        self.numbers_num = numbers_num
        self.symbols_num = symbols_num

    def generate_non_blank(self, row_data=None):
        upper_chars = self.get_random_choices_by_list(
            string.ascii_uppercase, self.upper_num)
        lower_chars = self.get_random_choices_by_list(
            string.ascii_lowercase, self.lower_num)
        number_chars = self.get_random_choices_by_list(
            string.digits, self.numbers_num)
        symbol_chars = self.get_random_choices_by_list(
            "!@#$%^&*()-_=+[]{};:,.<>?", self.symbols_num)

        password_chars = upper_chars + lower_chars + number_chars + symbol_chars
        remaining_length = max(0, self.min_length - len(password_chars))
        if remaining_length > 0:
            all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
            password_chars += self.get_random_choices_by_list(
                all_chars, remaining_length)

        self.shuffle_list(password_chars)
        return "".join(password_chars)
