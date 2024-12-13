import matplotlib.pyplot as plt
import numpy as np

mean = 0
std_dev = 1
num_samples = 1000


data = np.random.normal(mean, std_dev, num_samples)
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма распределения данных')
plt.show()