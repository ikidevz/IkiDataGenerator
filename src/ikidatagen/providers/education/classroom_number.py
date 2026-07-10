from ..base_provider import BaseProvider
import string


class ClassroomNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, format: str = "Auto", **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.format = format

    def generate_non_blank(self, row_data=None):
        formats = {
            "Room": f"Room {self.generate_integer(1, 999)}",
            "Lab": f"Lab {self.generate_integer(1, 50)}{self.get_random_data_by_list(string.ascii_uppercase)}",
            "Lecture": f"Lecture Hall {self.get_random_data_by_list(string.ascii_uppercase)}",
        }

        if self.format == "Auto":
            return self.get_random_data_by_list(list(formats.values()))

        if self.format in formats:
            return formats[self.format]

        return f"Room {self.generate_integer(1, 999)}"
