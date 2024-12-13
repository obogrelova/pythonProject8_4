import pandas as pd
import matplotlib.pyplot as plt


file_path = 'cleaned_price.csv'
data = pd.read_csv(file_path)

prices = data['Price']

plt.hist(prices, bins=10, color='blue')

plt.title('Гистограмма цен')
plt.xlabel('Значения')
plt.ylabel('Частота')

plt.show()