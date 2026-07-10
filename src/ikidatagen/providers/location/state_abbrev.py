from ..base_provider import BaseProvider


class StateAbbrevProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['states'], **kwargs)

    def generate_non_blank(self, row_data=None):
        country = (row_data or {}).get('country')
        if isinstance(country, str) and country.strip():
            matching_states = [
                row for row in self.import_datasets()['states']
                if str(row.get('country_name', '')).lower() == country.strip().lower()
            ]
            if matching_states:
                return self.get_random_data_by_list([
                    row.get('iso2') for row in matching_states if row.get('iso2')
                ])

        return self.get_row_data_from_datasets('states', 'iso2')
