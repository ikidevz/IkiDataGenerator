from ..base_provider import BaseProvider


class ApiVersionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        major = self.generate_integer(1, 10)
        if self.get_random_object() < 0.5:
            minor = self.generate_integer(0, 9)
            return f"v{major}.{minor}"
        else:
            return f"v{major}"
