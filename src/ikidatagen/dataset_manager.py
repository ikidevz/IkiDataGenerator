from __future__ import annotations

import csv
import json
from pathlib import Path
import importlib.resources as pkg_resources


class DatasetManager:
    """
    Loads and caches external dataset files (JSON / CSV) bundled with the package.

    All loaded data is cached in-process so each file is only read once per
    interpreter session, regardless of how many providers request it.
    """

    _cache: dict[str, list | dict] = {}

    @classmethod
    def _get_base_path(cls) -> Path:
        with pkg_resources.path(__package__, "external_datasets") as p:
            return p

    @classmethod
    def load(cls, name: str) -> list | dict:
        """
        Load a dataset by name.  Searches for {name}.json then {name}.csv under
        the package's external_datasets directory.

        Results are cached — subsequent calls with the same name are free.
        """
        if name in cls._cache:
            return cls._cache[name]

        base_path = cls._get_base_path()

        for ext in ("json", "csv"):
            file_path = base_path / ext / f"{name}.{ext}"
            if file_path.exists():
                data = cls._load_file(file_path)
                cls._cache[name] = data
                return data

        raise FileNotFoundError(
            f"[DatasetManager] Dataset '{name}' not found.\n"
            f"  → Searched in: {base_path / 'json'} and {base_path / 'csv'}"
        )

    @classmethod
    def load_key(cls, name: str, key: str) -> tuple:
        """
        Load a dataset file and extract a single key from it, returning
        the values as a tuple (ready for random.choice).

        Equivalent to: tuple(DatasetManager.load(name)[key])

        Results are cached under "name:key" so repeated calls are free.

        Parameters
        ----------
        name : dataset file name (e.g. "basic", "names", "it")
        key  : the key inside the file to extract (e.g. "frequency", "first_name_female")

        Raises
        ------
        KeyError  — if the key doesn't exist in the loaded file
        FileNotFoundError — if the dataset file doesn't exist
        """
        cache_key = f"{name}:{key}"

        if cache_key in cls._cache:
            return cls._cache[cache_key]

        class _LazyKey:
            def __init__(self, name: str, key: str, manager: type[DatasetManager]):
                self.name = name
                self.key = key
                self._manager = manager
                self._val = None

            def _load(self):
                if self._val is None:
                    data = self._manager.load(self.name)
                    if self.key not in data:
                        raise KeyError(
                            f"[DatasetManager] Key '{self.key}' not found in dataset '{self.name}'.\n"
                            f"  → Available keys: {', '.join(str(k) for k in data.keys())}"
                        )
                    self._val = tuple(data[self.key])
                return self._val

            def __iter__(self):
                return iter(self._load())

            def __len__(self):
                return len(self._load())

            def __getitem__(self, idx):
                return self._load()[idx]

            def __repr__(self):
                return f"LazyDatasetKey({self.name!r}, {self.key!r})"

            def __add__(self, other):
                if isinstance(other, _LazyKey):
                    return tuple(self._load()) + tuple(other._load())
                try:
                    return tuple(self._load()) + tuple(other)
                except Exception:
                    return NotImplemented

            def __radd__(self, other):
                if isinstance(other, _LazyKey):
                    return tuple(other._load()) + tuple(self._load())
                try:
                    return tuple(other) + tuple(self._load())
                except Exception:
                    return NotImplemented

        lazy = _LazyKey(name, key, cls)
        cls._cache[cache_key] = lazy
        return lazy

    @staticmethod
    def _load_file(path: Path) -> list | dict:
        if path.suffix == ".json":
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)

        if path.suffix == ".csv":
            with open(path, "r", encoding="utf-8") as f:
                return list(csv.DictReader(f))

        raise ValueError(
            f"[DatasetManager] Unsupported file type: {path.suffix!r}")
