#(-1)n-1(|х(2n+1)|)/(2n+1)!
#У алгоритма д.б. линейная сложность.
import numpy as np
import math
import random
# Количество знаков после запятой
while True:
    t = input("Введите количество знаков после запятой при вычислении неточности : ")
    if t.isdigit():
        if int(t) == 0:
            print("Вы ввели ноль. Введите другое число")
        else:
            t = int(t)
            break
    else:
        print("Вы должны были ввести натуральное число")
# Генерация матрицы случайным образом 
k = random.randint(1,4)
x = np.random.uniform(-1, 1, size=(k, k))
print(f"Матрица: \n{x}")
#Определитель
print(f"Определитель: {np.linalg.det(x)}")
# Вычисление нормы матрицы x
norm_x = np.linalg.norm(x)
#вычисление суммы знакопеременного ряда
n = 1
s = 10 ** (-t)
sum_result = 0

while True:
    fact_denominator = math.factorial(2 * n - 1)
    term = ((-1) ** (n - 1)) * (abs(norm_x) ** (2 * n - 1)) / fact_denominator
    sum_result += term

    if abs(term) < s:
        break

    n += 1

# Вывод результатов
print(f"Итоговая сумма ряда: {sum_result:.{t}f}")
print(f"Количество итераций: {n-1}")
