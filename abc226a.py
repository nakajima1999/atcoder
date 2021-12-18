# AtCoder Beginner Contest 226
# A - Round decimals
from decimal import Decimal, ROUND_HALF_UP
x = float(input())
print(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))