#Вычислить сумму знакопеременного ряда |х**2n|/(2n)!, где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
#Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.
import numpy as np
import random
#Создание матрицы и ввод данных
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
k = random.randint(1,4)
x = np.random.uniform(-1, 1, (k, k))
print(f"Матрица: \n{x}")
#Определитель
print(f"Определитель: {np.linalg.det(x)}")
#вычисление суммы знакопеременного ряда
n = 1
before_digit, result, accuracy = 0, 0, 1
fact_denominator, fact_numerator,sign = 1, 1,-1

while abs(accuracy) > (0.1 ** t):
    before_digit += result
    numerator = (2 * n) 
    fact_denominator *= np.prod(2 * n) * (2 * n + 1)
    result += sign * np.linalg.det(x ** fact_numerator) / fact_denominator
    n += 1
    accuracy = abs(before_digit - result)
    before_digit = 0
    sign *= -1
print(f"\nИтоговая сумма: {result:.{t}f}")
print(f"Кол-во итераций: {n-1}")
