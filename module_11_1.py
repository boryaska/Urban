import numpy as np
import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data)

print(df)
# выводим строку и столбец по номеру
print(df.loc[0])
print(df.loc[:, 0])
# транспонируем матрицу
df_trans = df.T
print(df_trans)
# Удаляем вторую строку DataFrame
df = df.drop(1)
print(df)

# Создаем массив numpy
a = np.array([1, 2, 3, 4, 5])
# Создаем матрицу
a = np.array([[1, 2], [3, 4]])
# Вычисляем определитель матрицы
det = np.linalg.det(a)
print(det)
# Вычисляем квадратный корень из каждого элемента массива
sqrt = np.sqrt(a)
print(sqrt)

