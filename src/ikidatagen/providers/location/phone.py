from ..base_provider import BaseProvider


class PhoneProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, format: str = "###-###-####", **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries'], **kwargs)
        self.format = format

    def generate_non_blank(self, row_data=None):
        country = (row_data or {}).get('country')
        if isinstance(country, str) and country.strip():
            country_row = self.get_dataset_lookup(
                'countries', 'name').get(country, {})
            phone_code = country_row.get('phone_code')
            if phone_code:
                return f"+{phone_code}-{self.generate_integer(100, 999)}-{self.generate_integer(100, 999)}-{self.generate_integer(1000, 9999)}"

        return "".join(self.sublify_char(c) for c in self.format)
