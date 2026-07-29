from ..base_provider import BaseProvider


class AppBundleIdProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['app'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'app_bundle_id',
            dataset='app',
            by=(('app_name', 'app_name'),),
        )