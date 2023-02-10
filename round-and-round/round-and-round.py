from decimal import *


def round_by_2_decimal_places(n):
    return Decimal(n).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)