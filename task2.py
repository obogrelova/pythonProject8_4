import matplotlib.pyplot as plt
import numpy as np


quantity = 5

random_array_first = np.random.rand(quantity)
random_array_second = np.random.rand(quantity)
print('Первый массив')
print(random_array_first)
print('Второй массив')
print(random_array_second)
plt.figure(figsize=(10, 6))
plt.scatter(random_array_first, random_array_second, color='blue', marker='*')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Диаграмма рассеяния')
plt.grid(True)
plt.show()