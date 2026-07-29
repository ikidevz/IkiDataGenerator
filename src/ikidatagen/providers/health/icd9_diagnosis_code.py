from ..base_provider import BaseProvider


class Icd9DiagnosisCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['ICD9_diagnosis'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'IC9_DIAGNOSIS_CODE',
            dataset='ICD9_diagnosis',
            by=(('icd9_dx_desc_long', 'IC9_DX_DESC_LONG'),
                ('icd9_dx_desc_short', 'IC9_DX_DESC_SHORT')),
        )
