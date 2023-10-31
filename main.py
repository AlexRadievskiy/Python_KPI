import pandas as pd

# 1. Читання файлу
data = pd.read_json('data/Version 5.json')

# Зміна назв стовпців
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
print("Відсутні значення:\n", missing_values)

# Заповнення відсутніх значень
if missing_values['Customer_care_calls'] > 0:
    mean_value = data['Customer_care_calls'].mean()
    data['Customer_care_calls'].fillna(mean_value, inplace=True)

# Перевірка статистичних даних
print("\nСтатистичні дані:\n", data.describe())

# Перевірка унікальних значень категоріальних змінних
categorical_columns = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender', 'Reached_on_Time']
for column in categorical_columns:
    print(f"\nУнікальні значення для {column}:\n", data[column].value_counts())

# Виведення перших 5 рядків даних для перевірки
print("\nПерші 5 рядків даних:\n", data.head())