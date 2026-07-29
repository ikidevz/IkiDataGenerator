from ..base_provider import BaseProvider


class Icd10DxDescLongProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['ICD10_diagnosis'], **kwargs)

    def generate_non_blank(self, row_data=None):
        return self.resolve_dataset_field(
            row_data,
            'ICD10_Dx_Desc_Long',
            dataset='ICD10_diagnosis',
            by=(('icd10_diagnosis_code', 'ICD10_Diagnosis_Code'),
                ('icd10_dx_desc_short', 'ICD10_Dx_Desc_Short')),
        )
