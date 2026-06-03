import random

from ..base_provider import BaseProvider


class DriverLicenseNumberProvider(BaseProvider):

    FORMATS = [
        "^########",        # D12345678
        "^^#######",        # AB1234567
        "^^-########",      # CA-12345678
        "^###-###-###",     # D123-456-789
        "##########",       # 1234567890
        "^^##########",     # NY1234567890
        "%########",        # A12345678
        "^^##-####-##",     # AB12-3456-78
    ]

    def __init__(
        self,
        pattern: str | None = None,
        blank_percentage: float = 0.0,
        **kwargs
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.pattern = pattern

    def generate_non_blank(self, row_data=None):

        pattern = self.pattern or random.choice(self.FORMATS)

        return "".join(
            self.sublify_char(char)
            for char in pattern
        )
