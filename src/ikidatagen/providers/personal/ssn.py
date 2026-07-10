from ..base_provider import BaseProvider


class SsnProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        while True:
            area = self.generate_integer(1, 899)
            if area == 666:
                continue
            group = self.generate_integer(1, 99)
            serial = self.generate_integer(1, 9999)

            ssn = f"{area:03d}-{group:02d}-{serial:04d}"
            return ssn
