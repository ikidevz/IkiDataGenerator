from ..base_provider import BaseProvider
import string


class DeliveryRouteCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        route_prefixes = ["RT", "MX", "PH", "CN",
                          "EU", "US", "JP", "BR", "IN", "RU"]
        hub_codes = ["SEA", "LAX", "SIN", "MNL",
                     "DXB", "FRA", "HKG", "AMS", "JFK", "NRT"]
        pattern_type = self.get_random_data_by_list(["simple", "airport"])

        if pattern_type == "simple":
            prefix = self.get_random_data_by_list(route_prefixes)
            number = self.generate_integer(1, 999)
            optional_letter = self.get_random_data_by_list(
                ["", self.get_random_data_by_list(list(string.ascii_uppercase))])
            return f"{prefix}-{number}{optional_letter}"

        else:  # Airport-to-airport style
            origin, destination = self.get_random_sample(hub_codes, 2)
            number = str(self.generate_integer(1, 99)).zfill(2)
            return f"{origin}-{destination}-{number}"
