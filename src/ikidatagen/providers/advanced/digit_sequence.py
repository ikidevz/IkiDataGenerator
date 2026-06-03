# providers/advanced/character_sequence_provider.py
from ..base_provider import BaseProvider


class DigitSequenceProvider(BaseProvider):
    def __init__(self, *, length: int = 8, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.length = length

    def generate_non_blank(self, row_data=None):
        return "".join(str(self.generate_integer(0, 9)) for _ in range(self.length))
