import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import math

#Загрузка данных из файла hmap.json
with open('hmap.json', 'r') as file:
    data = json.load(file)

# Отнимаем 754 от каждого числа и умножим на 2
# для избавления от отрицательных чисел возводим 
# в квадрат и тут же берем корень
result = [[int(math.sqrt((num - 754) **2)*2) for num in row] for row in data]
result_str = "\n".join([str(row) + ("," if i < len(result) - 1 else "") for i, row in enumerate(result)])
print(result_str)

# Запись результатов в файл itog.json
with open('itog.json', 'w') as file:
    file.write("[\n")
    for i, row in enumerate(result):
        file.write("[")
        file.write(", ".join(str(num) for num in row))
        file.write("]")
        if i < len(result) - 1:
            file.write(",\n")
        else:
            file.write("\n")
    file.write("]")

# Загрузка данных из файла itog.json
with open('itog.json', 'r') as file:
    data = json.load(file)

data = np.array(data)

# Создание координатных осей
x = np.arange(data.shape[1])
y = np.arange(data.shape[0])
X, Y = np.meshgrid(x, y)

# Создание графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение 3D графика
ax.plot_surface(X, Y, data, rstride=1, cstride=1, cmap='plasma')

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графика
plt.show()