from ..base_provider import BaseProvider


class LongitudeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries'], **kwargs)

    def generate_non_blank(self, row_data=None):
        longitude = self.resolve_dataset_field(
            row_data,
            'longitude',
            dataset='countries',
            by=(('country', 'name'),),
        )
        if longitude is not None:
            return round(float(longitude), 6)

        return round(self.generate_float(-180.0, 180.0), 6)
