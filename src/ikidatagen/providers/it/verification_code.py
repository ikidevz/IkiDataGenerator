from ..base_provider import BaseProvider


class VerificationCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, length: int = 6, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.length = length

    def generate_non_blank(self, row_data=None):
        return ''.join(self.get_random_choices_by_list("0123456789", k=self.length))
