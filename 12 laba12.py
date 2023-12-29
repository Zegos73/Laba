#|х*n!|/n!
#У алгоритма д.б. линейная сложность.
#Знак первого слагаемого  -.
import numpy as np
import math
import random
# Количество знаков после запятой
while True:
    t = input("Введите количество знаков после запятой: ")
    if t.isdigit():
        if int(t) == 0:
            print("Введите другое число")
        else:
            t = int(t)
            break
    else:
        print("Вы ввести натуральное число")
# Генерация матрицы случайным образом 
k = random.randint(1,4)
x = np.random.uniform(-1, 1, size=(k, k))
print(f"Матрица: \n{x}")
#Определитель
print(f"Определитель: {np.linalg.det(x)}")
#вычисление суммы знакопеременного ряда
n = 1
result = 0
sign = -1
before_digit = 0
accuracy = 1
fact_denominator = 1
fact_numerator = 1

while abs(accuracy) > (0.1 ** t):
    before_digit += result
    fact_numerator *= (n - 1) * (n)
    fact_denominator *= (n - 1) * (n)
    result += sign * np.linalg.det(x * fact_numerator) / fact_denominator
    n += 1
    accuracy = abs(before_digit - result)
    before_digit = 0
    sign *= -1

# Вывод результатов
print(f"Итоговая сумма ряда: {result:.{t}f}")
print(f"Количество итераций: {n-1}")
