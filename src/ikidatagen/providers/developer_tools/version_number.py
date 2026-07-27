from ..base_provider import BaseProvider


class VersionNumberProvider(BaseProvider):

    def __init__(
        self,
        version_format: str = "auto",
        blank_percentage: float = 0.0,
        **kwargs
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.version_format = version_format.lower()

    def _semver(self):
        return f"{self.generate_integer(0, 20)}.{self.generate_integer(0, 50)}.{self.generate_integer(0, 100)}"

    def _major_minor(self):
        return f"{self.generate_integer(0, 20)}.{self.generate_integer(0, 50)}"

    def _major(self):
        return str(self.generate_integer(1, 20))

    def _build(self):
        return (
            f"{self.generate_integer(0, 20)}."
            f"{self.generate_integer(0, 50)}."
            f"{self.generate_integer(0, 100)}+"
            f"{self.generate_integer(100, 9999)}"
        )

    def _prerelease(self):
        tag = self.get_random_data_by_list(
            ["alpha", "beta", "rc", "preview", "dev"]
        )

        return (
            f"{self.generate_integer(0, 20)}."
            f"{self.generate_integer(0, 50)}."
            f"{self.generate_integer(0, 100)}-"
            f"{tag}.{self.generate_integer(1, 10)}"
        )

    def _date_version(self):
        year = self.generate_integer(2020, 2035)
        month = self.generate_integer(1, 12)
        day = self.generate_integer(1, 28)

        return f"{year}.{month:02d}.{day:02d}"

    def generate_non_blank(self, row_data=None):

        generators = {
            "semver": self._semver,
            "major_minor": self._major_minor,
            "major": self._major,
            "build": self._build,
            "prerelease": self._prerelease,
            "date": self._date_version,
        }

        if self.version_format == "auto":
            return self.get_random_data_by_list(list(generators.values()))()

        generator = generators.get(self.version_format)

        if generator is None:
            raise ValueError(
                f"Unsupported version_format: '{self.version_format}'. "
                f"Supported formats: {', '.join(generators.keys())}, auto"
            )

        return generator()
