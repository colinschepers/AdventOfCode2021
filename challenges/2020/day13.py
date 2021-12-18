from functools import reduce
from typing import Sequence

from utils import get_input


def mul_inv(a: int, b: int) -> int:
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n: Sequence[int], a: Sequence[int]) -> int:
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


data = get_input(year=2020, day=13)
t0 = int(data[0])
busses = [(i, int(bus)) for i, bus in enumerate(data[1].split(',')) if bus != 'x']
diffs = [(b[1] - t0 % b[1], b[1]) for b in busses]
min_bus = min(diffs)

print(min_bus[0] * min_bus[1])
print(chinese_remainder([bus for _, bus in busses], [bus - i for i, bus in busses]))
