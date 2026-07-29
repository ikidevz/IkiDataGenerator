from ..base_provider import BaseProvider


class LatitudeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries'], **kwargs)

    def generate_non_blank(self, row_data=None):
        latitude = self.resolve_dataset_field(
            row_data,
            'latitude',
            dataset='countries',
            by=(('country', 'name'),),
        )
        if latitude is not None:
            return round(float(latitude), 6)

        return round(self.generate_float(-90.0, 90.0), 6)
