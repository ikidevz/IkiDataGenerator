from ..base_provider import BaseProvider


class CharacterSequenceProvider(BaseProvider):
    """
    Generates random sequences of characters, digits, and symbols
    based on a pattern string that can include wildcard symbols:

    Wildcards:
      # → random digit (0-9)
      @ → random lowercase letter (a-z)
      ^ → random uppercase letter (A-Z)
      * → random digit or letter
      $ → random digit or lowercase letter
      % → random digit or uppercase letter

    Example:
      pattern="@@##%"  → "ab34F"
      pattern="^^-####" → "AB-1234"
    """

    def __init__(self, *, pattern: str = "@@##%", blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.pattern = pattern

    def generate_non_blank(self, row_data=None) -> str:
        return "".join(self.sublify_char(c) for c in self.pattern)
