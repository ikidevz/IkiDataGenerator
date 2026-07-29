from ..base_provider import BaseProvider


class HcpcsNameProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['hcpcs'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'name',
            dataset='hcpcs',
            by=(('hcpcs_code', 'code'),),
        )
