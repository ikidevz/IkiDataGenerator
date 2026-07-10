from ..base_provider import BaseProvider
import datetime


class InvoiceNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefixes = ["INV", "BILL", "RCPT", "PAY", "TXN"]
        prefix = self.get_random_data_by_list(prefixes)
        year = datetime.datetime.now().year
        number = self.generate_integer(1, 999999)

        # Randomly pick a format pattern
        formats = [
            f"{prefix}-{year}-{number:05d}",
            f"{prefix}-{number:06d}",
            f"{year}-{prefix}-{number:05d}",
            f"{prefix}{year}{number:04d}",
            f"{prefix.upper()}-{self.generate_integer(10, 99)}-{number:04d}",
        ]
        return self.get_random_data_by_list(formats)
