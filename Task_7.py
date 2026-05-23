import random
import matplotlib.pyplot as plt
from collections import Counter

N = 100000

sums = []
for _ in range(N):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sums.append(d1 + d2)

count = Counter(sums)
possible_sums = list(range(2, 13))
exp_prob = [count[s] / N for s in possible_sums]

theoretical_prob = [
    1/36, 2/36, 3/36, 4/36, 5/36, 6/36,
    5/36, 4/36, 3/36, 2/36, 1/36
]

print("Сума | Монте-Карло | Теорія | Різниця")
print("--------------------------------------")

for s, e, t in zip(possible_sums, exp_prob, theoretical_prob):
    diff = e - t
    print(f"{s:>4} | {e:>11.4f} | {t:>6.4f} | {diff:+.4f}")
