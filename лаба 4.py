import numpy as np
import matplotlib.pyplot as plt


K = int(1)
N = int(2)


A = np.random.randint(-10, 11, (N, N))


B = A[:N//2, :N//2]
C = A[:N//2, N//2:]
D = A[N//2:, :N//2]
E = A[N//2:, N//2:]


F = A.copy()


E_odd_cols_zeros = np.count_nonzero(E[:, 1::2] == 0)
E_odd_rows_sum = np.sum(E[1::2, :])


if E_odd_cols_zeros > E_odd_rows_sum:
    A[:N//2, :N//2] = E
    A[N//2:, N//2:] = B

else:
    A[:N//2, N//2:] = E
    A[N//2:, :N//2] = C


if np.linalg.det(A) > np.sum(np.diagonal(F)):
    G = np.tril(A)

    A_inv = np.linalg.inv(A)
    A_transpose = np.transpose(A)
    A_inv_transpose = np.transpose(A_inv)

    F_inv = np.linalg.inv(F)

    result = np.dot(A_inv, A_transpose) - K * F_inv


else:
    G = np.tril(A)

    A_inv = np.linalg.inv(A)
    F_inv = np.linalg.inv(F)

    result = (A_inv + G - F_inv) * K


print("Матрица A:")
print(A)
print("Матрица F:")
print(F)
print("Матрица G:")
print(G)
print("Результат вычисления выражения:")
print(result)

plt.figure(figsize=(6, 6))
plt.imshow(F, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title("Тепловая карта матрицы F")
plt.show()

F_flat = F.flatten()
plt.hist(F_flat, bins=20, color='blue', edgecolor='black')
plt.title("Гистограмма элементов матрицы F")
plt.xlabel("Значения")
plt.ylabel("Количество")
plt.show()

F_sum_cols = np.sum(F, axis=0)
plt.bar(range(1, N + 1), F_sum_cols, color='purple', edgecolor='black')
plt.title("Столбчатая диаграмма сумм по столбцам матрицы F")
plt.xlabel("Номер столбца")
plt.ylabel("Сумма")
plt.xticks(range(1, N + 1))
plt.show()
