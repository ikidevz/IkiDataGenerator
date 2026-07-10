from ..base_provider import BaseProvider
import datetime
import string


class SkuProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        year = datetime.datetime.now().year
        letters = ''.join(self.get_random_choices_by_list(
            string.ascii_uppercase, k=self.generate_integer(2, 3)))
        digits = ''.join(self.get_random_choices_by_list(string.digits, k=self.generate_integer(3, 5)))

        formats = [
            f"SKU-{digits}-{letters}",
            f"PRD-{year}-{self.generate_integer(100, 999)}",
            f"ITEM-{digits}-{letters}",
            f"SKU-{letters}-{digits}",
            f"INV-{digits}-{letters}",
            f"CODE-{year}-{letters}",
        ]
        return self.get_random_data_by_list(formats)
