from ..base_provider import BaseProvider


class AddressLine2Provider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.prefixes = ["Room", "Apt", "Suite", "Floor", "PO Box"]

    def generate_non_blank(self, row_data=None):
        prefix = self.get_random_data_by_list(self.prefixes)
        if prefix == "PO Box":
            number = self.generate_integer(100, 99999)
        elif prefix == "Floor":
            n = self.generate_integer(1, 200)
            suffix = "th" if 10 <= n % 100 <= 20 else {
                1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
            return f"{n}{suffix} Floor"
        else:
            number = self.generate_integer(1, 2000)

        return f"{prefix} {number}"
