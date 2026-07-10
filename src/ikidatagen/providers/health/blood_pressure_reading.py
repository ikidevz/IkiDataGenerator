from ..base_provider import BaseProvider
import random


class BloodPressureReadingProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        systolic = random.randint(90, 160)
        # Ensure diastolic lower bound is <= upper bound
        upper = min(100, systolic - 40)
        upper = max(60, upper)
        diastolic = random.randint(60, upper)
        return f"{systolic}/{diastolic}"
