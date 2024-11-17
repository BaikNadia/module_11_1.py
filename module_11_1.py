import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Построение графика
plt.plot(x, y, label="Линейный график", color="blue", marker="o")
plt.title("Пример линейного графика")  # Заголовок
plt.xlabel("X-axis")  # Подпись оси X
plt.ylabel("Y-axis")  # Подпись оси Y
plt.legend()  # Легенда
plt.grid()  # Сетка
plt.show()  # Отображение графика


# Создание серии путем передачи питоновского списка
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s, '\n')

# Создание кадра данных путем передачи массива с временным индексом и помеченными столбцами:
# указываем начало временного периода и число повторений (дни по умолчанию)
dates = pd.date_range('20240101', periods=6)
print(dates, '\n')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df, '\n')

# Создание кадра данных путем передачи питоновского словаря объектов, с преобразованием в серию
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20240102'),  # временная метка
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),  # Серия на основе списка
                    'D': np.array([3] * 4, dtype='int32'),  # массив целых чисел
                    'E': pd.Categorical(["test", "train", "test", "train"]),  # категории
                    'F': 'foo'})
print(df2, '\n')

#  Типы данных в столбцах итогового Кадра данных
print(df2.dtypes, '\n')

# Просмотр данных

# верхние строки полученного кадра данных:
print(df.head(), '\n')
# 3 нижние строки полученного кадра данных:
print(df.tail(3), '\n')
# Отображение индексов и столбцов:
print(df.index, '\n')
print(df.columns, '\n')
# Данные в виде массива, на котором строится кадр данных:
print(df.to_numpy(), '\n')
# Запись в excel файл:
df.to_excel('foo.xlsx', sheet_name='Sheet1')
# Чтение из excel файла:
print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))
