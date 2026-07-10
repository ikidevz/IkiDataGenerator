from ..base_provider import BaseProvider
import string
import datetime


class CouponCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefix_list = [
            "SAVE", "DEAL", "PROMO", "DISCOUNT", "SALE", "WELCOME",
            "OFFER", "FREESHIP", "BONUS", "BLACKFRIDAY", "CYBER", "NEWYEAR", "HOLIDAY",
            "CHRISTMAS", "XMAS", "EASTER", "SUMMER", "WINTER", "SPRING", "FALL", "VALENTINE",
            "BACK2SCHOOL", "YEAR-END", "CLEARANCE", "VIP", "MEMBER", "LOYALTY",
            "REWARD", "THANKYOU", "RETURNCUSTOMER", "REFER", "FRIEND", "POINTS", "CASHBACK",
            "LIMITED", "FLASH", "HOTDEAL", "WEEKEND", "EARLYBIRD", "LAUNCH",
            "INTRO", "FIRSTORDER", "TRYME", "WELCOME2025"
        ]
        prefix = self.get_random_data_by_list(prefix_list)
        numeric = str(self.generate_integer(5, 75))
        letters = ''.join(self.get_random_choices_by_list(
            string.ascii_uppercase + string.digits, self.generate_integer(3, 6)))
        year = str(datetime.datetime.now().year)[-2:]
        formats = [
            f"{prefix}{numeric}",
            f"{prefix}{year}",
            f"{prefix}-{letters}",
            f"{prefix}{numeric}-{letters}",
            f"{prefix}-{numeric}{year}",
            f"{prefix}{letters}{numeric}"
        ]
        return self.get_random_data_by_list(formats)
