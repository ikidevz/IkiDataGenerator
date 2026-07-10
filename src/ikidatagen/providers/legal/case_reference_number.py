from ..base_provider import BaseProvider


class CaseReferenceNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        pattern = self.get_random_data_by_list(
            ["supreme", "case_hash", "criminal", "civil", "admin"])

        if pattern == "supreme":
            number = self.generate_integer(10000, 299999)
            return f"G.R. No. {number}"

        elif pattern == "case_hash":
            year = self.generate_integer(10, 25)
            seq1 = self.generate_integer(1, 999)
            seq2 = self.generate_integer(1, 999)
            return f"Case #{year}-CR-{seq2:03d}"

        elif pattern == "criminal":
            year = self.generate_integer(2010, 2025)
            seq = self.generate_integer(1, 99999)
            return f"CR-{year}-{seq:05d}"

        elif pattern == "civil":
            year = self.generate_integer(2010, 2025)
            seq = self.generate_integer(1, 9999)
            return f"CV-{year}-{seq:04d}"

        elif pattern == "admin":
            year = self.generate_integer(10, 25)
            seq = self.generate_integer(1, 999)
            return f"ADMIN-{year}-{seq:03d}"
