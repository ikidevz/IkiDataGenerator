from ..base_provider import BaseProvider


class CreditScoreBandProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        if row_data and row_data.get('credit_score') is not None:
            try:
                score = int(row_data['credit_score'])
            except (TypeError, ValueError):
                score = None

            if score is not None:
                if score < 580:
                    return 'Subprime Risk'
                if score < 670:
                    return 'Poor'
                if score < 740:
                    return 'Fair'
                if score < 800:
                    return 'Good'
                if score < 850:
                    return 'Prime Borrower'
                return 'Excellent'

        return self.get_random_data_by_list(self.finance['credit_score_band'])
