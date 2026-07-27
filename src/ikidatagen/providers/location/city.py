from ..base_provider import BaseProvider


class CityProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        # Use both countries and hotels datasets to provide richer city options
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['countries', 'hotels'], **kwargs)
        self._countries_lookup = None
        self._cities_by_country = None
        self._all_cities = None

    def generate_non_blank(self, row_data=None, row_index: int | None = None):
        if self._countries_lookup is None:
            self._countries_lookup = self.get_dataset_lookup(
                'countries', 'name')

        if self._cities_by_country is None:
            # Build mapping country_name -> list of cities from hotels dataset
            datasets = self.import_datasets()
            hotels = datasets.get('hotels', [])
            mapping: dict[str, list[str]] = {}
            all_cities = []
            for r in hotels:
                c = r.get('country')
                city = r.get('city')
                if not c or not city:
                    continue
                mapping.setdefault(c, []).append(city)
                all_cities.append(city)
            self._cities_by_country = mapping
            self._all_cities = tuple(dict.fromkeys(all_cities))

        country = (row_data or {}).get('country')

        # Prefer sampling a city from the same country (excluding the capital when possible)
        if country:
            cities = self._cities_by_country.get(country)
            if cities:
                # try to avoid returning the capital when a non-capital exists
                capital = self._countries_lookup.get(
                    country, {}).get('capital')
                non_caps = [c for c in cities if c != capital]
                choices = non_caps or cities
                return self._rng.choice(choices)

        # Fallback: pick a random city from the hotels-derived list
        if self._all_cities:
            return self._rng.choice(self._all_cities)

        # Final fallback: return the country's capital from countries dataset
        return self.get_row_data_from_datasets('countries', 'capital')
