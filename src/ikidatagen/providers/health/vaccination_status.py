from ..base_provider import BaseProvider


class VaccinationStatusProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

        self.statuses = [
            "Vaccinated",
            "Not Vaccinated",
            "Partially Vaccinated",
            "Up to Date",
            "Due",
            "Overdue",
            "Declined",
            "Unknown",
            "Exempted",
        ]

    def generate_non_blank(self, row_data=None):
        return self.get_random_data_by_list(self.statuses)
