from ..base_provider import BaseProvider
import string


class PostalCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0,  **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=["countries"], **kwargs)

        self.country_formats = {
            # 🌏 Asia-Pacific
            # Philippines
            "PH": lambda: str(self.generate_integer(1000, 9999)),
            # Japan
            "JP": lambda: f"{self.generate_integer(100, 999)}-{self.generate_integer(1000, 9999)}",
            "IN": lambda: str(self.generate_integer(100000, 999999)),  # India
            "CN": lambda: str(self.generate_integer(100000, 999999)),  # China
            # Singapore
            "SG": lambda: str(self.generate_integer(100000, 999999)),
            # Hong Kong (non-official)
            "HK": lambda: str(self.generate_integer(100000, 999999)),
            # South Korea
            "KR": lambda: f"{self.generate_integer(100, 999)}-{self.generate_integer(100, 999)}",
            "AU": lambda: str(self.generate_integer(200, 9999)),  # Australia
            # New Zealand
            "NZ": lambda: str(self.generate_integer(1000, 9999)),
            "TH": lambda: str(self.generate_integer(10000, 99999)),  # Thailand
            "MY": lambda: str(self.generate_integer(10000, 99999)),  # Malaysia

            # 🌎 Americas
            "US": self._generate_us_zip,
            "CA": self._generate_ca_postal,
            "MX": lambda: str(self.generate_integer(10000, 99999)),  # Mexico
            # Brazil
            "BR": lambda: f"{self.generate_integer(10000, 99999)}-{self.generate_integer(100, 999)}",
            # Argentina
            "AR": lambda: f"{self.generate_integer(1000, 9999)}{self.get_random_data_by_list(string.ascii_uppercase)}{self.get_random_data_by_list(string.ascii_uppercase)}",
            # Chile
            "CL": lambda: str(self.generate_integer(1000000, 9999999)),
            # Colombia
            "CO": lambda: str(self.generate_integer(100000, 999999)),
            "PE": lambda: str(self.generate_integer(10000, 99999)),  # Peru

            # 🌍 Europe
            "UK": self._generate_uk_postcode,
            "DE": lambda: str(self.generate_integer(10000, 99999)),  # Germany
            "FR": lambda: str(self.generate_integer(10000, 95999)),  # France
            # Spain
            "ES": lambda: str(self.generate_integer(1000, 52999)).zfill(5),
            "IT": lambda: str(self.generate_integer(10000, 98100)),  # Italy
            # Netherlands
            "NL": lambda: f"{self.generate_integer(1000, 9999)}{self.get_random_data_by_list(string.ascii_uppercase)}{self.get_random_data_by_list(string.ascii_uppercase)}",
            # Sweden
            "SE": lambda: f"{self.generate_integer(100, 999)} {self.generate_integer(10, 99)}",
            "NO": lambda: str(self.generate_integer(1000, 9999)),  # Norway
            # Poland
            "PL": lambda: f"{self.generate_integer(10, 99)}-{self.generate_integer(100, 999)}",
            # Switzerland
            "CH": lambda: str(self.generate_integer(1000, 9999)),

            # 🌍 Middle East & Africa
            # UAE (approx.)
            "AE": lambda: str(self.generate_integer(10000, 99999)),
            # Saudi Arabia
            "SA": lambda: str(self.generate_integer(10000, 99999)),
            # South Africa
            "ZA": lambda: str(self.generate_integer(1000, 9999)),
            "EG": lambda: str(self.generate_integer(11111, 99999)),  # Egypt
            "KE": lambda: str(self.generate_integer(10000, 99999)),  # Kenya
        }

        self.available_countries = list(self.country_formats.keys())

    def _generate_us_zip(self):
        """US ZIP or ZIP+4"""
        if self.get_random_object() < 0.2:
            return f"{self.generate_integer(10000, 99999)}-{self.generate_integer(1000, 9999)}"
        return str(self.generate_integer(10000, 99999))

    def _generate_ca_postal(self):
        """Canadian postal code: A1A 1A1"""
        letters = string.ascii_uppercase
        digits = string.digits
        return f"{self.get_random_data_by_list(letters)}{self.get_random_data_by_list(digits)}{self.get_random_data_by_list(letters)} {self.get_random_data_by_list(digits)}{self.get_random_data_by_list(letters)}{self.get_random_data_by_list(digits)}"

    def _generate_uk_postcode(self):
        """UK postal code (simplified realistic pattern)"""
        letters = string.ascii_uppercase
        digits = string.digits
        return f"{self.get_random_data_by_list(letters)}{self.get_random_data_by_list(letters)}{self.get_random_data_by_list(digits)} {self.get_random_data_by_list(digits)}{self.get_random_data_by_list(letters)}{self.get_random_data_by_list(letters)}"

    def generate_non_blank(self, row_data=None):
        country_code = None
        country = (row_data or {}).get('country')
        if isinstance(country, str) and country.strip():
            normalized = country.strip().upper()
            if normalized in {'UK', 'GB', 'U.K.', 'UNITED KINGDOM', 'GREAT BRITAIN'}:
                country_code = 'UK'
            elif normalized in {'US', 'USA', 'U.S.', 'UNITED STATES', 'UNITED STATES OF AMERICA'}:
                country_code = 'US'
            else:
                country_code = self.resolve_dataset_field(
                    row_data,
                    'iso2',
                    dataset='countries',
                    by=(('country', 'name'),),
                )

        if country_code not in self.country_formats:
            country_code = self.get_random_data_by_list(
                self.available_countries)

        postal_code = self.country_formats[country_code]()
        return postal_code
