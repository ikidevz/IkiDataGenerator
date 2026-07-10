from ..base_provider import BaseProvider
import hashlib
import string


class Md5Provider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        random_string = ''.join(self.get_random_choices_by_list(
            string.ascii_letters + string.digits, k=16))
        return hashlib.md5(random_string.encode()).hexdigest()
