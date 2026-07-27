from ..base_provider import BaseProvider


class EpisodeNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        season = self.generate_integer(1, 10)
        episode = self.generate_integer(1, 20)

        formats = [
            f"S{season:02d}E{episode:02d}",
            f"Episode {episode}",
            f"Season {season} Episode {episode}",
        ]

        return self.get_random_data_by_list(formats)
