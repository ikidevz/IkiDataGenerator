from ..base_provider import BaseProvider


class ProductSubcategoryProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['product'], **kwargs)

    def generate_non_blank(self, row_data=None):
        col = self.get_random_data_by_list(
            ['tag1', 'tag2', 'tag3', 'tag4', 'tag5'])
        return self.resolve_dataset_field(
            row_data,
            col,
            dataset='product',
            by=(('product_name', 'Product Name'),),
        )
