from ..base_provider import BaseProvider


class LongitudeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries'], **kwargs)

    def generate_non_blank(self, row_data=None):
        country = (row_data or {}).get('country')
        if isinstance(country, str) and country.strip():
            country_row = self.get_dataset_lookup(
                'countries', 'name').get(country, {})
            longitude = country_row.get('longitude')
            if longitude is not None:
                return round(float(longitude), 6)

        return round(self.generate_float(-180.0, 180.0), 6)
