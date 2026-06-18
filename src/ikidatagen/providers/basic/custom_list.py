from ..base_provider import BaseProvider


class CustomListProvider(BaseProvider):
    def __init__(
        self,
        blank_percentage: float = 0.0,
        values=None,
        **kwargs
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

        if isinstance(values, list):
            self.custom_format = values
        elif isinstance(values, str):
            self.custom_format = values.split(',')
        else:
            self.custom_format = []

    def generate_non_blank(self, row_data=None):
        return self.get_random_data_by_list(self.custom_format)
