# 17.	F(1) = 1, F(n) = F(n–1) * (n + n!), при четных n > 1 F(n)=sin(n) при нечетных n > 1
import time
import matplotlib.pyplot as plt
from math import sin

def recursive_F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return recursive_F(n-1) * (n + factorial(n))
    else:
        return sin(n)


def iterative_F(n):
    if n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        if i % 2 == 0:
            result *= (i + factorial(i))
        else:
            result = sin(i)
    return result


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = 50


start_time = time.perf_counter()
recursive_result = recursive_F(n)
recursive_time = time.perf_counter() - start_time
start_time = time.perf_counter()
iterative_result = iterative_F(n)
iterative_time = time.perf_counter() - start_time
    

print("Значение рекуррентной функции для n =", n)
print("Рекурсивный подход:", recursive_result, "Время выполнения:", recursive_time)
print("Итерационный подход:", iterative_result, "Время выполнения:", iterative_time)


recursive_times = []
iterative_times = []
ns = []
for i in range(1, n+1):
    start_time = time.perf_counter()
    recursive_F(i)
    recursive_times.append(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    iterative_F(i)
    iterative_times.append(time.perf_counter() - start_time)

    ns.append(i)

plt.plot(ns, recursive_times, label="Recursive")
plt.plot(ns, iterative_times, label="Iterative")
plt.xlabel("n")
plt.ylabel("Time, sec")
plt.legend()
plt.show()
import pandas as pd

data = {
    "n": range(1, n + 1),
    "Рекурсивный подход": recursive_times,
    "Итерационный подход": iterative_times,
}

df = pd.DataFrame(data)
print(df)
