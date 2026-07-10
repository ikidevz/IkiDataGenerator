from ..base_provider import BaseProvider
import string


class TrackingNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefixes = ["UPS", "FDX", "DHL", "LBC",
                    "USPS", "JNT", "NINJA", "GRB", "XDE"]
        prefix = self.get_random_data_by_list(prefixes)
        numeric_part = ''.join(self.get_random_choices_by_list(
            string.digits, k=self.generate_integer(8, 12)))

        suffix = ''.join(self.get_random_choices_by_list(
            string.ascii_uppercase, k=self.get_random_data_by_list([0, 2, 3])))
        formats = [
            f"{prefix}{numeric_part}{suffix}",
            f"{prefix}-{numeric_part}-{suffix}" if suffix else f"{prefix}-{numeric_part}",
            f"{numeric_part}{suffix}",
            f"{prefix}{numeric_part}"
        ]

        return self.get_random_data_by_list(formats)
