#17.	Формируется матрица F следующим образом: если в Е количество нулей в нечетных столбцах в области 4 больше, чем сумма чисел в нечетных строках в области 1, то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: (К*(A*F)– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

# задаем исходные данные
K_test = 2
N_test = 6
A_test = [[1, 2, -1, 2, 0, -3],
          [0, -1, 3, 2, -1, 4],
          [0, 0, 1, -2, 3, 1],
          [2, 3, -1, 0, 1, 2],
          [1, 0, 2, -1, 3, -2],
          [2, 1, 4, 3, 2, 1]]

# выбираем использовать тестовые данные или случайные
print('Использовать тестовые данные или случайные?')
choice = input('Ваш выбор (1 - тестовые данные, 2 - случайные, q-выход): ')

if choice == '1':
    K = K_test
    N = N_test
    A = A_test

elif choice == '2':
    K = int(input('Введите K: '))
    N = int(input('Введите N: '))

    if N < 6:
        print('Ошибка в исходных данных. Длина сторон матрицы А (N,N) должна быть больше 5!')
        exit()

    A = []
    for row in range(N):
        cur_row = []
        for col in range(N):
            cur_row.append(random.randint(-10, 10))
        A.append(cur_row)

else:
    exit()

# печатаем матрицу A
print('Матрица A:')
for row in range(N):
    print(A[row])

# формируем матрицу E
n = N // 2  # размерность матриц B, C, D, E (n x n)
if N % 2 == 0:
    step = N // 2
else:
    step = N // 2 + 1

E = []
for row in range(n):
    cur_row = []
    for col in range(n):
        cur_row.append(A[row][col])
    E.append(cur_row)

# формируем матрицы B, C, D
B = [[A[row][col + step] for col in range(n)] for row in range(n)]
C = [[A[row + step][col + step] for col in range(n)] for row in range(n)]
D = [[A[row + step][col] for col in range(n)] for row in range(n)]

# печатаем матрици B, C, D, E
print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

# считаем количество нулевых элементов в нечетных столбцах в области 4 матрицы E
count_zero_E_4 = 0
for row in range(1, n - 1):
    if n % 2 == 1:
        if row <= n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    else:
        if row < n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    for col in range(0, end_col):
        if col % 2 == 1 and E[row][col] == 0:
            count_zero_E_4 += 1  # увеличиваем счетчик

print(f'Количество нулевых элементов в матрице E в области 4 в нечетных столбцах: {count_zero_E_4}')

# считаем сумму чисел в нечётных строках в области 1 матрицы С
sum_odd_rows_C_1 = sum([sum(C[row][:n:2]) for row in range(n)])

# проверяем условие и формируем матрицу F
if count_zero_E_4 > sum_odd_rows_C_1:
    # меняем симметрично области 1 и 2 матрицы Е
    for row in range(n):
        for col in range(n - row):
            if col % 2 == 1:
                temp = E[row][col]
                E[row][col] = E[n - col - 1][n - row - 1]
                E[n - col - 1][n - row - 1] = temp
    print('Матрица E после изменений:')
    for row in range(n):
        print(E[row])

    # формируем матрицу F
    F = []
    for row in range(N):
        cur_row = []
        for col in range(N):
            if row < n and col < n:
                cur_row.append(E[row][col])
            elif row < n and col >= n:
                cur_row.append(B[row][col - n])
            elif row >= n and col < n:
                cur_row.append(D[row - n][col])
            else:
                cur_row.append(C[row - n][col - n])
        F.append(cur_row)

else:
    # меняем несимметрично матрицы С и Е
    C_new = []
    for row in range(n):
        cur_row = []
        for col in range(n):
            cur_row.append(E[row][col] + C[row][col])
        C_new.append(cur_row)

    E_new = []
    for row in range(n):
        cur_row = []
        for col in range(n):
            cur_row.append(E[row][col] - C[row][col])
        E_new.append(cur_row)

    # печатаем новые матрицы С и Е
    print('Матрица C после изменений:')
    for row in range(n):
        print(C_new[row])

    print('Матрица E после изменений:')
    for row in range(n):
        print(E_new[row])

    # формируем матрицу F
    F = []
    for row in range(N):
        cur_row = []
        for col in range(N):
            if row < n and col < n:
                cur_row.append(E_new[row][col])
            elif row < n and col >= n:
                cur_row.append(B[row][col - n])
            elif row >= n and col < n:
                cur_row.append(D[row - n][col])
            else:
                cur_row.append(C_new[row - n][col - n])
        F.append(cur_row)

# печатаем матрицу F
print('Матрица F:')
for row in range(N):
    print(F[row])
F_mult_A = []  # результат перемножения матрицы F на A
for row in range(N):
    F_row = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += F[row][j] * A[j][i]
        F_row.append(sum)
    F_mult_A.append(F_row)

print('Матрица F*A: ')
for row in range(N):
    print(F_mult_A[row])


# вычисляем выражение (K*(A*F)– K*AT)
AT = [] # транспонированная матрица A
for row in range(N):
    AT_row = []
    for col in range(N):
        AT_row.append(A[col][row])
    AT.append(AT_row)

print('Транспонированная матрица A: ')
for row in range(N):
    print(AT[row])

result = [[0 for col in range(N)] for row in range(N)]
for row in range(N):
    for col in range(N):
        for k in range(N):
            result[row][col] += A[row][k] * F[k][col]
        result[row][col] *= K
        result[row][col] -= K * AT[row][col]
AT_mult_K = []  # матрица с результатом умножения K * Aт
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    AT_mult_K.append(
        cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(N):
    for col in range(N):
        AT_mult_K[row][col] = K * AT[row][col]  # транспонированная матрица А умноженная на константу К

print('Транспонированная матрица A умноженная на K: ')
for row in range(N):
    print(AT_mult_K[row])
# печатаем результат
print('Результат выражения (K*(A*F)– K*AT):')
for row in range(N):
    print(result[row])
