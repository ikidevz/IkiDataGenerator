from ..base_provider import BaseProvider


class AnimalScientificNameProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['animals'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'animal_scientific_name',
            dataset='animals',
            by=(('animal_name', 'animal_name'),),
        )