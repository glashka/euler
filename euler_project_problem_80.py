""" Problem 80
"""

from decimal import *

squares = set([1, 4, 9, 16, 25, 36, 49, 64, 81])

getcontext().prec = 105

result = 0

for n in range(2, 100):
    if n not in squares:
        result += sum(int(i) for i in str(Decimal(n).sqrt()).replace('.', '')[:100])

print(result)
