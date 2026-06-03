from ..base_provider import BaseProvider


class CarModelProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['cars'], **kwargs)
        self.lookup = None

    def generate_non_blank(self, row_data=None):

        if self.lookup is None:
            self.lookup = self.get_dataset_lookup('cars', 'Make')

        car_make = row_data.get('Make') if row_data else None

        return (
            self.lookup.get(car_make, {}).get('Model')
            or self.get_row_data_from_datasets('cars', 'Model')
        )
