from ..base_provider import BaseProvider
import ast


class BookGenreProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['books'], **kwargs)

    def generate_non_blank(self, row_data=None):
        # Some rows store the literal string "[]" which parses to an empty list.
        # Retry a few times to avoid returning an empty list; if still empty, return None.
        for _ in range(20):
            raw = self.get_row_data_from_datasets('books', "genres")
            try:
                genres_list = ast.literal_eval(raw)
            except Exception:
                genres_list = []
            if genres_list:
                return self.get_random_data_by_list(genres_list)

        return None
