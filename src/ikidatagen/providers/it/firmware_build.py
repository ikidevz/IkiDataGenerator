from ..base_provider import BaseProvider
from datetime import datetime, timedelta


class FirmwareBuildProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        start_date = datetime(2022, 1, 1)
        random_days = self.generate_integer(0, 365 * 4)
        build_date = start_date + timedelta(days=random_days)

        date_part = build_date.strftime("%Y.%m.%d")
        build_number = self.generate_integer(1000, 9999)

        return f"FW-{date_part}-{build_number}"
