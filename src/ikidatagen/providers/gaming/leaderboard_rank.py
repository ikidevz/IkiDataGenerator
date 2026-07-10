from ..base_provider import BaseProvider


class LeaderboardRankProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, len: int = 1000, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.len = len

    def generate_non_blank(self, row_data=None):
        return self.generate_integer(1, self.len)
