""" Problem 80
"""

from decimal import *

getcontext().prec = 105

result = 0

for n in range(2, 100):
    result += sum(int(i) for i in str(Decimal(n).sqrt()).replace('.', '')[:100])

print(result)
