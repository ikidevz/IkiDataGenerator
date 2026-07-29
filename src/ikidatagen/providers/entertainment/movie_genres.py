from ..base_provider import BaseProvider


class MovieGenresProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['movies'], **kwargs)


    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'genres',
            dataset='movies',
            by=(('movie_title', 'title'),),
        )