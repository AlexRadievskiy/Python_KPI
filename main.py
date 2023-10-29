import pandas as pd

# 1. Читання файлу
data = pd.read_json('data/Version 5.json')

# Зміна назв стовпців (якщо потрібно)
data.columns = ['ID', 'Warehouse_block', 'Mode_of_Shipment', 'Customer_care_calls', 'Customer_rating',
                'Cost_of_the_Product', 'Prior_purchases', 'Product_importance', 'Gender', 'Discount_offered',
                'Weight_in_gms', 'Reached_on_Time']

# 2. Ідентифікація та вирішення проблем з даними

# Перевірка на дублікати
duplicates = data.duplicated()
if duplicates.sum() > 0:
    data = data.drop_duplicates()

# Перевірка на відсутні значення
missing_values = data.isnull().sum()
print(missing_values)

# Заповнення відсутніх значень
# Наприклад, якщо у нас є відсутні значення в стовпці 'Customer_care_calls', ми можемо заповнити їх середнім значенням
if missing_values['Customer_care_calls'] > 0:
    mean_value = data['Customer_care_calls'].mean()
    data['Customer_care_calls'].fillna(mean_value, inplace=True)

# Виведення перших 5 рядків даних для перевірки
print(data.head())
