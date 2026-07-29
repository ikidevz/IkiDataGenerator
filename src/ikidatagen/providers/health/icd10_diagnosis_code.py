from ..base_provider import BaseProvider


class Icd10DiagnosisCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['ICD10_diagnosis'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'ICD10_Diagnosis_Code',
            dataset='ICD10_diagnosis',
            by=(('icd10_dx_desc_long', 'ICD10_Dx_Desc_Long'),
                ('icd10_dx_desc_short', 'ICD10_Dx_Desc_Short')),
        )
