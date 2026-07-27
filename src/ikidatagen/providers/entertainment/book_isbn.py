from ..base_provider import BaseProvider


class BookIsbnProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['books'], **kwargs)

        self.lookup = None

    def generate_non_blank(self, row_data=None):
        if self.lookup is None:
            self.lookup = self.get_dataset_lookup('books', 'title')

        book_title = row_data.get('title') if row_data else None

        return (
            self.lookup.get(book_title, {}).get('isbn')
            or self.get_row_data_from_datasets('books', 'isbn')
        )
