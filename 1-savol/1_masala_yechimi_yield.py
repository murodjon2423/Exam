
from math import sqrt

n = int(input())

def prime_numbers(n: int):
    if n >= 2:
        yield 2
    for i in range(3, n + 1, 2):
        for j in range(3, int(sqrt(i)) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i

k = list(prime_numbers(n))
l = list(range(1, n + 1))

for y in k:
    if y in l:
        l.remove(y)

print(l)
