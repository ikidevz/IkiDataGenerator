from ..base_provider import BaseProvider


class NoiseLevelProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['noise'], **kwargs)

    def _parse_level(self, level_str):
        if '-' in level_str:
            low, high = map(int, level_str.split('-'))
        elif '+' in level_str:
            low = int(level_str.replace('+', ''))
            high = low + 20
        else:
            low = high = int(level_str)
        return round(self.generate_float(low, high), 1)

    def generate_non_blank(self, row_data=None):
        row_data = row_data or {}
        noise_source = row_data.get('noise_source')
        noise_category = row_data.get('noise_category')

        if noise_source:
            noise_level_db = self.resolve_dataset_field(
                row_data,
                'Noise_Level_DB',
                dataset='noise',
                by=(('noise_source', 'Source'),),
            )
            return self._parse_level(noise_level_db)

        if noise_category:
            noise_level_db = self.resolve_dataset_field(
                row_data,
                'Noise_Level_DB',
                dataset='noise',
                by=(('noise_category', 'Category'),),
            )
            return self._parse_level(noise_level_db)

        return round(self.generate_float(20, 120), 1)
