from ..base_provider import BaseProvider


class BankBranchCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefix = self.get_random_data_by_list(["001", "002", "003", "004", "005"])
        remaining_length = 12 - len(prefix)
        rest = "".join(str(self.generate_integer(0, 9))
                       for _ in range(remaining_length))
        return prefix + rest
