import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
data = pd.read_csv('data/Amazon.csv')
data['Date'] = pd.to_datetime(data['Date'])

# 1. Побудова графіків зміни ціни на час закриття біржі

# а) загальний
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Закриття біржі')
plt.title('Зміна ціни на час закриття біржі')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.show()

# б) за 2018 рік
data_2018 = data[data['Date'].dt.year == 2018].copy()
plt.figure(figsize=(10, 6))
plt.plot(data_2018['Date'], data_2018['Close'], label='Закриття біржі 2018')
plt.title('Зміна ціни на час закриття біржі за 2018 рік')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.show()

# в) за січень 2020 року
data_jan_2020 = data[(data['Date'] >= '2020-01-01') & (data['Date'] <= '2020-01-31')].copy()
plt.figure(figsize=(10, 6))
plt.plot(data_jan_2020['Date'], data_jan_2020['Close'], label='Закриття біржі січень 2020')
plt.title('Зміна ціни на час закриття біржі за січень 2020 року')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.show()

# г) за грудень 2016 – лютий 2018
data_dec_2016_feb_2018 = data[(data['Date'] >= '2016-12-01') & (data['Date'] <= '2018-02-28')].copy()
plt.figure(figsize=(10, 6))
plt.plot(data_dec_2016_feb_2018['Date'], data_dec_2016_feb_2018['Close'], label='Закриття біржі грудень 2016 - лютий 2018')
plt.title('Зміна ціни на час закриття біржі з грудня 2016 по лютий 2018')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.show()

# д) за 2016 та 2017 на одному графіку (паралельно)
data_2016 = data[data['Date'].dt.year == 2016].copy()
data_2017 = data[data['Date'].dt.year == 2017].copy()
plt.figure(figsize=(10, 6))
plt.plot(data_2016['Date'], data_2016['Close'], label='Закриття біржі 2016')
plt.plot(data_2017['Date'], data_2017['Close'], label='Закриття біржі 2017')
plt.title('Зміна ціни на час закриття біржі за 2016 та 2017 роки')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.show()

# 2. Знаходження максимальних значень найбільшої ціни за день

# а) за 2016 рік
max_high_2016 = data_2016['High'].max()
print(f"Максимальна ціна за день за 2016 рік: {max_high_2016}")

# б) за кожний рік
years = data['Date'].dt.year.unique()
for year in years:
    max_high = data[data['Date'].dt.year == year]['High'].max()
    print(f"Максимальна ціна за день за {year} рік: {max_high}")

# в) за кожний тиждень весни 2019 року
data_spring_2019 = data[(data['Date'] >= '2019-03-20') & (data['Date'] <= '2019-06-21')].copy()
data_spring_2019['Week'] = data_spring_2019['Date'].dt.isocalendar().week
weeks_2019 = data_spring_2019['Week'].unique()
for week in weeks_2019:
    max_high_week = data_spring_2019[data_spring_2019['Week'] == week]['High'].max()
    print(f"Максимальна ціна за день за тиждень {week} весни 2019 року: {max_high_week}")

# г) Розрахунок і зображення змін значення найбільшої ціни за день у відсотках за кожен день впродовж весни 2018 року
data_spring_2018 = data[(data['Date'] >= '2018-03-20') & (data['Date'] <= '2018-06-21')].copy()
data_spring_2018['Price Change %'] = data_spring_2018['High'].pct_change() * 100
plt.figure(figsize=(10, 6))
plt.plot(data_spring_2018['Date'], data_spring_2018['Price Change %'], label='Зміна ціни в %')
plt.title('Зміна найбільшої ціни за день у відсотках за весну 2018 року')
plt.xlabel('Дата')
plt.ylabel('Зміна в %')
plt.legend()
plt.show()

# д) Зображення ковзного середнього найбільшої ціни за день за 2017 рік з вікном в два місяці
data_2017['Rolling Mean'] = data_2017['High'].rolling(window=60).mean()
plt.figure(figsize=(10, 6))
plt.plot(data_2017['Date'], data_2017['Rolling Mean'], label='Ковзне середнє')
plt.title('Ковзне середнє найбільшої ціни за день за 2017 рік')
plt.xlabel('Дата')
plt.ylabel('Ковзне середнє')
plt.legend()
plt.show()
