from ..base_provider import BaseProvider


class NoiseSourceProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['noise'], **kwargs)

    def _determine_range(self, value):
        ranges = [
            (30, "20-30"),
            (50, "30-50"),
            (70, "60-70"),
            (85, "70-85"),
            (100, "85-100"),
            (120, "120+"),
        ]
        if isinstance(value, (int, float)):
            for upper, category in ranges:
                if value <= upper:
                    return category

    def generate_non_blank(self, row_data=None):
        row_data = row_data or {}
        noise_level = row_data.get('noise_level')

        if noise_level is not None:
            resolved_level = self._determine_range(noise_level)
            if resolved_level:
                return self.resolve_dataset_field(
                    {**row_data, 'noise_level': resolved_level},
                    'Source',
                    dataset='noise',
                    by=(('noise_level', 'Noise_Level_DB'),
                        ('noise_category', 'Category')),
                )

        return self.resolve_dataset_field(
            row_data,
            'Source',
            dataset='noise',
            by=(('noise_category', 'Category'),),
        )
