import random
import string
import warnings
from abc import ABC, abstractmethod
from ..dataset_manager import DatasetManager
from ..payload import PAYLOAD


class BaseProvider(ABC):
    _datasets: dict | None = None

    @classmethod
    def _get_datasets(cls) -> dict:
        if cls._datasets is not None:
            return cls._datasets

        cls._datasets = PAYLOAD

        return cls._datasets

    def __init__(
        self,
        *,
        blank_percentage: float = 0.0,
        datasets: list[str] | None = None,
        **kwargs,
    ):
        if kwargs:
            warnings.warn(
                f"[{self.__class__.__name__}] Unknown option(s) ignored: {', '.join(kwargs.keys())}. "
                f"Check for typos in your schema 'options'.",
                UserWarning,
                stacklevel=3,
            )

        self.blank_percentage = float(blank_percentage or 0.0)
        self.datasets = datasets or []
        self.data = None

        _d = self._get_datasets()
        self.ai = _d.get("ai", {})
        self.advanced = _d.get("advanced", {})
        self.basic = _d.get("basic", {})
        self.car = _d.get("car", {})
        self.commerce = _d.get("commerce", {})
        self.communication = _d.get("communication", {})
        self.construction = _d.get("construction", {})
        self.crypto = _d.get("crypto", {})
        self.education = _d.get("education", {})
        self.finance = _d.get("finance", {})
        self.gaming = _d.get("gaming", {})
        self.health = _d.get("health", {})
        self.it = _d.get("it", {})
        self.legal = _d.get("legal", {})
        self.location = _d.get("location", {})
        self.marketing = _d.get("marketing", {})
        self.nature = _d.get("nature", {})
        self.personal = _d.get("personal", {})
        self.political = _d.get("political", {})
        self.products = _d.get("products", {})
        self.sports = _d.get("sports", {})
        self.travel = _d.get("travel", {})

        self.departments = _d.get("departments", {})
        self.file = _d.get("file", {})
        self.format = _d.get("format", {})
        self.person = _d.get("person", {})
        self.street = _d.get("street", {})

    @abstractmethod
    def generate_non_blank(self, row_data: dict | None = None):
        raise NotImplementedError

    def import_datasets(self) -> dict:
        return {name: DatasetManager.load(name) for name in self.datasets}

    def get_dataset_lookup(self, dataset: str, key_col: str) -> dict:
        rows = self.import_datasets()[dataset]
        return {row[key_col]: row for row in rows if row.get(key_col)}

    def get_row_data_from_datasets(self, dataset: str, columns: str):
        if self.data is None:
            datasets = self.import_datasets()
            self.data = tuple(
                d.get(columns) for d in datasets[dataset] if d.get(columns)
            )
        return random.choice(self.data)

    def sublify_char(self, symbol: str) -> str:
        match symbol:
            case "#": return random.choice(string.digits)
            case "@": return random.choice(string.ascii_lowercase)
            case "^": return random.choice(string.ascii_uppercase)
            case "*": return random.choice(string.ascii_letters + string.digits)
            case "$": return random.choice(string.ascii_lowercase + string.digits)
            case "%": return random.choice(string.ascii_uppercase + string.digits)
            case _: return symbol

    def generate_username(self, row_data: dict | None = None) -> str:
        name_mix = self.person["first_name"]["female"] + \
            self.person["first_name"]["male"]
        pattern = random.choice(self.format["username"])

        first_name = (row_data or {}).get(
            "first_name") or random.choice(name_mix)
        last_name = (row_data or {}).get(
            "last_name") or random.choice(self.person["last_name"])
        full_name = (row_data or {}).get("full_name")

        if full_name:
            parts = full_name.split()
            first_name, last_name = parts[0], parts[1] if len(
                parts) > 1 else last_name

        username = (
            pattern
            .replace("{{first_name}}", first_name)
            .replace("{{last_name}}", last_name)
        )
        return "".join(self.sublify_char(c) for c in username).lower()

    def random_base58(self, length: int) -> str:
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        return "".join(random.choice(alphabet) for _ in range(length))

    def encode_base32(self, data: bytes) -> str:
        alphabet = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
        num = int.from_bytes(data, "big")
        chars = []
        for _ in range((len(data) * 8 + 4) // 5):
            num, rem = divmod(num, 32)
            chars.append(alphabet[rem])
        return "".join(reversed(chars))

    def generate_integer(self, min: int = 0, max: int = 1000) -> int:
        return random.randint(min, max)

    def generate_float(self, min: float = 0.0, max: float = 1000) -> float:
        return random.uniform(min, max)

    def get_random_data_by_list(self, d: list | tuple):
        return random.choice(d)

    def get_random_choices_by_list(self, d: list | tuple, k: int = 1):
        return random.choices(d, k=k)

    def get_random_object(self):
        return random.random()
