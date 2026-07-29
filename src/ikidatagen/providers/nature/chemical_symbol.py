from ..base_provider import BaseProvider


class ChemicalSymbolProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['period_table'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'symbol',
            dataset='period_table',
            by=(('name', 'name'),),
        )