import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Завантаження даних
df = pd.read_csv('data/Amazon.csv', parse_dates=['Date'], index_col='Date')

# 1. Побудувати графік зміни ціни на час закриття біржі
# а) загальний
fig_general = px.line(df, y='Close', title='Загальний графік ціни закриття')
fig_general.show()

# б) за 2018 рік
fig_2018 = px.line(df.loc['2018'], y='Close', title='Ціна закриття за 2018 рік')
fig_2018.show()

# в) за січень 2020 року
fig_jan_2020 = px.line(df.loc['2020-01'], y='Close', title='Ціна закриття за січень 2020 року')
fig_jan_2020.show()

# г) за грудень 2016 – лютий 2018
fig_dec_2016_feb_2018 = px.line(df.loc['2016-12':'2018-02'], y='Close', title='Ціна закриття з грудня 2016 по лютий 2018')
fig_dec_2016_feb_2018.show()

# д) за 2016 та 2017 на одному графіку (паралельно)
df_2016 = df.loc['2016', 'Close'].reset_index()
df_2016['Month-Day'] = df_2016['Date'].dt.strftime('%m-%d')
df_2017 = df.loc['2017', 'Close'].reset_index()
df_2017['Month-Day'] = df_2017['Date'].dt.strftime('%m-%d')

fig_parallel = go.Figure()
fig_parallel.add_trace(go.Scatter(x=df_2016['Month-Day'], y=df_2016['Close'], mode='lines', name='2016'))
fig_parallel.add_trace(go.Scatter(x=df_2017['Month-Day'], y=df_2017['Close'], mode='lines', name='2017'))
fig_parallel.update_layout(title='Паралельне порівняння цін закриття за 2016 та 2017 роки', xaxis_title='Дата', yaxis_title='Ціна закриття')
fig_parallel.show()

# 2. Знайти максимальні значення найбільшої ціни за день
# а) за 2016 рік
max_price_2016 = df.loc['2016']['High'].max()
print(f'Максимальна ціна за 2016 рік: {max_price_2016}')

# б) за кожний рік
max_price_annual = df['High'].resample('Y').max()
print('Максимальна ціна за кожний рік:\n', max_price_annual)

# в) за кожний тиждень весни 2019 року
max_price_spring_2019 = df.loc['2019-03-01':'2019-05-31']['High'].resample('W').max()
print('Максимальна ціна за кожний тиждень весни 2019 року:\n', max_price_spring_2019)

# г) Зміни значення найбільшої ціни за день у відсотках за кожен день впродовж весни 2018 року
spring_2018 = df.loc['2018-03-01':'2018-05-31']['High'].pct_change() * 100
fig_spring_2018 = px.line(spring_2018, title='Зміна найбільшої ціни за день у відсотках (весна 2018)')
fig_spring_2018.show()

# д) Ковзне середнє найбільшої ціни за день за 2017 рік з вікном в два місяці
rolling_avg_2017 = df.loc['2017']['High'].rolling('60D').mean()
fig_rolling_avg_2017 = px.line(rolling_avg_2017, title='Ковзне середнє найбільшої ціни за день (2017, вікно 2 місяці)')
fig_rolling_avg_2017.show()
