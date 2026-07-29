import datetime
import platform
from dateutil import parser as date_parser
from ..base_provider import BaseProvider


DEFAULT_DATE_FORMAT = "mm/dd/yyyy"
DEFAULT_FROM_DATE = "01/01/1970"


class DatetimeProvider(BaseProvider):

    _DATE_FORMAT_ALIASES = {
        "m/d/yyyy": "m/d/yyyy",
        "mm/dd/yyyy": "mm/dd/yyyy",
        "yyyy-mm-dd": "yyyy-mm-dd",
        "yyyy-mm": "yyyy-mm",
        "d/m/yyyy": "d/m/yyyy",
        "dd/mm/yyyy": "dd/mm/yyyy",
        "d.m.yyyy": "d.m.yyyy",
        "dd.mm.yyyy": "dd.mm.yyyy",
        "dd-mm-yyyy": "dd-mm-yyyy",
        "dd-mon-yyyy": "dd-Mon-yyyy",
        "yyyy/mm/dd": "yyyy/mm/dd",
        "sql datetime": "SQL datetime",
        "sql_datetime": "SQL datetime",
        "sql-datetime": "SQL datetime",
        "iso 8601 (utc)": "ISO 8601 (UTC)",
        "iso8601 (utc)": "ISO 8601 (UTC)",
        "iso8601": "iso",
        "iso 8601": "iso",
        "epoch": "epoch",
        "unix timestamp": "epoch",
        "unix_timestamp": "epoch",
        "timestamp": "epoch",
        "mongodb epoch": "mongoDB epoch",
        "mongodb_epoch": "mongoDB epoch",
        "mongodb iso": "mongoDB ISO",
        "mongodb_iso": "mongoDB ISO",
    }

    def __init__(
        self,
        from_date: str = None,
        to_date: str = None,
        date_format: str = DEFAULT_DATE_FORMAT,
        minimum_age: int = None,
        maximum_age: int = None,
        blank_percentage: float = 0.0,
        **kwargs
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

        today = datetime.date.today()
        from_date, to_date = self._resolve_date_bounds(
            from_date, to_date, minimum_age, maximum_age, today
        )

        self.from_date = self._parse_date(from_date, "from_date")
        self.to_date = self._parse_date(to_date, "to_date")

        if self.from_date > self.to_date:
            raise ValueError(
                f"[{self.__class__.__name__}] 'from_date' ({from_date!r}) is after "
                f"'to_date' ({to_date!r}). 'from_date' must not be later than 'to_date'."
            )

        self.format = self._normalize_date_format(date_format)

        self.no_zero_day = "%#d" if platform.system() == "Windows" else "%-d"
        self.no_zero_month = "%#m" if platform.system() == "Windows" else "%-m"

    def _resolve_date_bounds(self, from_date, to_date, minimum_age, maximum_age, today):
        if minimum_age is not None and maximum_age is not None:
            to_date = (
                today - datetime.timedelta(days=minimum_age * 365)).strftime("%m/%d/%Y")
            from_date = (
                today - datetime.timedelta(days=maximum_age * 365)).strftime("%m/%d/%Y")

        if to_date is None:
            to_date = today.strftime("%m/%d/%Y")
        if from_date is None:
            from_date = DEFAULT_FROM_DATE

        return from_date, to_date

    def _normalize_date_format(self, value: str) -> str:
        if not isinstance(value, str):
            return value

        normalized = value.strip().lower()
        return self._DATE_FORMAT_ALIASES.get(normalized, value)

    _KNOWN_DATE_FORMATS = (
        "%m/%d/%Y",
        "%m/%d/%Y %H:%M:%S",
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%d.%m.%Y",
        "%Y/%m/%d",
        "%Y-%m",
        "%d-%b-%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
    )

    def _parse_date(self, value, param_name: str = "date") -> datetime.datetime:
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            return datetime.datetime(value.year, value.month, value.day)

        if isinstance(value, (int, float)):
            return datetime.datetime.fromtimestamp(
                value, tz=datetime.timezone.utc
            ).replace(tzinfo=None)

        if isinstance(value, str):
            text = value.strip()
            if not text:
                raise ValueError(
                    f"[{self.__class__.__name__}] '{param_name}' cannot be an empty string."
                )

            if text.lstrip("-").isdigit():
                try:
                    return datetime.datetime.fromtimestamp(
                        int(text), tz=datetime.timezone.utc
                    ).replace(tzinfo=None)
                except (ValueError, OSError, OverflowError):
                    pass

            for fmt in self._KNOWN_DATE_FORMATS:
                try:
                    return datetime.datetime.strptime(text, fmt)
                except ValueError:
                    continue

            try:
                return date_parser.parse(text)
            except (ValueError, OverflowError, date_parser.ParserError):
                raise ValueError(
                    f"[{self.__class__.__name__}] Could not parse '{param_name}' value "
                    f"{value!r} as a date. Try an unambiguous format such as "
                    f"'YYYY-MM-DD' or 'MM/DD/YYYY'."
                )

        raise TypeError(
            f"[{self.__class__.__name__}] '{param_name}' must be a string, "
            f"datetime.date/datetime.datetime, or epoch number, got {type(value).__name__}."
        )

    def _random_datetime_between(
        self, start: datetime.datetime, end: datetime.datetime
    ) -> datetime.datetime:
        delta = end - start
        random_seconds = self.generate_integer(0, int(delta.total_seconds()))
        return start + datetime.timedelta(seconds=random_seconds)

    def _safe_epoch_seconds(self, dt: datetime.datetime) -> int:
        return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())

    def _build_format_map(self, dt: datetime.datetime) -> dict[str, str]:
        d, m = self.no_zero_day, self.no_zero_month
        epoch_seconds = self._safe_epoch_seconds(dt)

        return {
            "m/d/yyyy": dt.strftime(f"{m}/{d}/%Y"),
            "mm/dd/yyyy": dt.strftime("%m/%d/%Y"),
            "yyyy-mm-dd": dt.strftime("%Y-%m-%d"),
            "yyyy-mm": dt.strftime("%Y-%m"),
            "d/m/yyyy": dt.strftime(f"{d}/{m}/%Y"),
            "dd/mm/yyyy": dt.strftime("%d/%m/%Y"),
            "d.m.yyyy": dt.strftime(f"{d}.{m}.%Y"),
            "dd.mm.yyyy": dt.strftime("%d.%m.%Y"),
            "dd-mm-yyyy": dt.strftime("%d-%m-%Y"),
            "dd-Mon-yyyy": dt.strftime("%d-%b-%Y"),
            "yyyy/mm/dd": dt.strftime("%Y/%m/%d"),
            "SQL datetime": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "ISO 8601 (UTC)": dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "epoch": str(epoch_seconds),
            "unix timestamp": str(epoch_seconds),
            "mongoDB epoch": str(epoch_seconds * 1000),
            "mongoDB ISO": dt.isoformat() + "Z",
            "iso": dt.isoformat(),
        }

    def _format_datetime(self, dt: datetime.datetime) -> str:
        format_map = self._build_format_map(dt)
        return format_map.get(self.format, dt.isoformat())

    def generate_non_blank(self, row_data=None):
        random_datetime = self._random_datetime_between(
            self.from_date, self.to_date)
        return self._format_datetime(random_datetime)
