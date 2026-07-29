from ..base_provider import BaseProvider


class AirportRegionCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['airport'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'iso_region',
            dataset='airport',
            by=(('airport_code', 'iata_code'), ('airport_name', 'name')),
        )
