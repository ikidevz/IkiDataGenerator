from ..base_provider import BaseProvider


class PlantFamilyProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['plants'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'plant_family',
            dataset='plants',
            by=(('plant_common_name', 'plant_common_name'),
                ('plant_scientific_name', 'plant_scientific_name')),
        )
