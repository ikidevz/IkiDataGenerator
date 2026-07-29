from ..base_provider import BaseProvider


class CountryProvider(BaseProvider):
    ALLOWED_FIELDS = ["name", "iso2", "iso3"]

    def __init__(self, blank_percentage: float = 0.0, field: str = "name", **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries'], **kwargs)
        if field not in self.ALLOWED_FIELDS:
            raise ValueError(
                f"Invalid field '{field}'. Allowed values: {sorted(self.ALLOWED_FIELDS)}"
            )
        self.field = field

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(row_data, self.field, by=(("city", "capital"),))
