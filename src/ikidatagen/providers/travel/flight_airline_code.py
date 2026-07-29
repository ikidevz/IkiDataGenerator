from ..base_provider import BaseProvider


class FlightAirlineCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['airlines'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'code',
            dataset='airlines',
            by=(('airlines_name', 'name'),),
        )
