import math
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def recursive_f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return recursive_f(n - 1) * (n + factorial(n))
    else:
        return math.sin(n)

def iterative_f(n):
    result = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            result *= (i + factorial(i))
        else:
            result = math.sin(i)
    return result

import matplotlib.pyplot as plt

N = 125
recursive_times = []
iterative_times = []

for i in range(1, N + 1):
    start_time = time.time()
    recursive_f(i)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

    start_time = time.time()
    iterative_f(i)
    end_time = time.time()
    iterative_times.append(end_time - start_time)

plt.plot(range(1, N + 1), recursive_times, label="Рекурсивный подход")
plt.plot(range(1, N + 1), iterative_times, label="Итерационный подход")
plt.xlabel("n")
plt.ylabel("Время выполнения (с)")
plt.legend()
plt.show()

import pandas as pd

data = {
    "n": range(1, N + 1),
    "Рекурсивный подход": recursive_times,
    "Итерационный подход": iterative_times,
}

df = pd.DataFrame(data)
print(df)
