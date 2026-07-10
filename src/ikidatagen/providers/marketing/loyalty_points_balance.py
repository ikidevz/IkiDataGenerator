from ..base_provider import BaseProvider


class LoyaltyPointsBalanceProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        r = self.get_random_object()
        if r < 0.75:
            # Most customers: normal everyday balances
            points = self.generate_integer(10, 5000)
        elif r < 0.95:
            # Occasional high earners
            points = self.generate_integer(5000, 50000)
        else:
            # Rare super loyal users
            points = self.generate_integer(50000, 500000)

        return f"{points:,}"
