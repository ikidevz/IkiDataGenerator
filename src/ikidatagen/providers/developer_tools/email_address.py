from ..base_provider import BaseProvider


class EmailAddressProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        pattern = self._rng.choice(self.format['email'])
        user = self.generate_username(row_data)
        domain = self.get_random_data_by_list(self.it['domains'])
        first = (row_data or {}).get('first_name') or self._rng.choice(
            self.person['first_name']['female'] + self.person['first_name']['male'])
        last = (row_data or {}).get('last_name') or self._rng.choice(
            self.person['last_name'])
        subdomain = self._rng.choice(('www', 'mail', 'app', 'inbox'))
        number = str(self._rng.randint(1, 9999))

        return (
            pattern
            .replace('{{user_name}}', user)
            .replace('{{domain_name}}', domain)
            .replace('{{first_name}}', first)
            .replace('{{last_name}}', last)
            .replace('{{subdomain}}', subdomain)
            .replace('{{number}}', number)
        )
