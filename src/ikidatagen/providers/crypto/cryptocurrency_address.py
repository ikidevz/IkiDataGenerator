from ..base_provider import BaseProvider


class CryptocurrencyAddressProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(
            blank_percentage=blank_percentage,
            datasets=['cryptocurrency'],
            **kwargs
        )

    def _generate_from_template(self, template: str) -> str:
        return ''.join(self.sublify_char(c) for c in template)

    def _eth_address(self):
        return self._generate_from_template("0x****************************************")

    def _btc_address(self):
        return self._generate_from_template("1*********************************")

    def _tron_address(self):
        return self._generate_from_template("T*********************************")

    def _solana_address(self):
        return self._generate_from_template("********************************************")

    def generate_non_blank(self, row_data=None):
        generators = [
            self._eth_address,
            self._btc_address,
            self._tron_address,
            self._solana_address,
        ]

        return self.get_random_data_by_list(generators)()
