from ..base_provider import BaseProvider
import re


class TemplateProvider(BaseProvider):
    def __init__(self, *, blank_percentage: float = 0.0, template: str = '', schema_labels=None, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.template = template
        self.schema_labels = set(schema_labels or [])

    def generate_non_blank(self, row_data: dict = None):
        if not self.template:
            return None

        if not row_data:
            return self.template

        def replace_placeholder(match):
            label = match.group(1).strip()
            if label in row_data:
                return str(row_data[label])
            if label in self.schema_labels:
                raise ValueError(
                    f"Template placeholder '{{{{{label}}}}}' references a field not yet available in the current row."
                )
            raise ValueError(
                f"Template placeholder '{{{{{label}}}}}' does not match any known schema field."
            )

        return re.sub(r"\{\{([^}]+)\}\}", replace_placeholder, self.template)
