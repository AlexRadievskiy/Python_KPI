import pandas as pd
import matplotlib.pyplot as plt

# 1. Завантаження даних
data = pd.read_csv('data/Amazon.csv')

# 2. Перетворення стовпця дати
data['Date'] = pd.to_datetime(data['Date'])

# Встановлення дати як індексу для легшого вибору даних
data.set_index('Date', inplace=True)

# 3. Фільтрація даних та побудова графіків
# а) загальний графік зміни ціни на час закриття біржі
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Ціна закриття')
plt.title('Зміна ціни акцій Amazon')
plt.xlabel('Дата')
plt.ylabel('Ціна закриття')
plt.legend()
plt.show()

# б) графік за 2018 рік
data_2018 = data['2018-01-01':'2018-12-31']
plt.figure(figsize=(10, 6))
plt.plot(data_2018['Close'], label='Ціна закриття за 2018 рік')
plt.title('Зміна ціни акцій Amazon у 2018 році')
plt.xlabel('Дата')
plt.ylabel('Ціна закриття')
plt.legend()
plt.show()

# 4. Обчислення максимальних значень та інші статистичні операції
# Максимальне значення за 2016 рік
max_price_2016 = data['2016-01-01':'2016-12-31']['High'].max()
print(f"Максимальна ціна за день у 2016 році: {max_price_2016}")