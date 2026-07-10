from ..base_provider import BaseProvider


class TimezoneOffsetProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, prefix: str = "UTC", **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.prefix = prefix

    def generate_non_blank(self, row_data=None):
        time_zone = (row_data or {}).get('time_zone')
        if isinstance(time_zone, str) and time_zone.strip():
            normalized = time_zone.strip().lower()
            if normalized.startswith('utc'):
                try:
                    offset = int(normalized.replace('utc', '', 1))
                    sign = "+" if offset >= 0 else ""
                    return f"{self.prefix}{sign}{offset}"
                except ValueError:
                    pass

        offset = self.generate_integer(-12, 14)
        sign = "+" if offset >= 0 else ""
        return f"{self.prefix}{sign}{offset}"
