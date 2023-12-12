import pandas as pd

# Налаштування відображення DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def remove_rare_values(df, column_name, threshold=2):
    value_counts = df[column_name].value_counts()
    to_remove = value_counts[value_counts < threshold].index
    df = df[~df[column_name].isin(to_remove)]
    return df

# Читання файлу JSON
file_path = 'data/Version 5.json'
try:
    df = pd.read_json(file_path)
except ValueError as e:
    print(f"Помилка при читанні файлу: {e}")

# Зміна назв стовпців
new_column_names = {
    "ID": "ID",
    "Warehouse_block": "WarehouseBlock",
    "Mode_of_Shipment": "ShipmentMode",
    "Customer_care_calls": "CustomerCareCalls",
    "Customer_rating": "CustomerRating",
    "Cost_of_the_Product": "ProductCost",
    "Prior_purchases": "PriorPurchases",
    "Product_importance": "ProductImportance",
    "Gender": "Gender",
    "Discount_offered": "DiscountOffered",
    "Weight_in_gms": "WeightInGms",
    "Reached.on.Time_Y.N": "ReachedOnTime"
}
df.rename(columns=new_column_names, inplace=True)

# Видалення рідкісних значень
df = remove_rare_values(df, 'ShipmentMode')
df = remove_rare_values(df, 'ProductImportance')

# Видалення всіх значень у 'Gender', крім 'M' та 'F'
df = df[df['Gender'].isin(['M', 'F'])]

# Виявлення та виправлення проблем з даними
if df.isnull().values.any():
    print("Виявлено відсутні значення")
    df.ffill(inplace=True)

if df.duplicated().any():
    print("Виявлено дублікати")
    df.drop_duplicates(inplace=True)

# Видалення рядків, де значення у 'WarehouseBlock' має більше ніж один символ
df = df[df['WarehouseBlock'].apply(lambda x: len(x) == 1)]

# Виведення результатів
print(df)

# Статистичний аналіз даних
print(df.describe())

# Видалення рідкісних значень з порогом 2
df = remove_rare_values(df, 'ShipmentMode', threshold=2)

# Аналіз категоріальних змінних
categorical_columns = ['WarehouseBlock', 'ShipmentMode', 'ProductImportance', 'Gender']
for col in categorical_columns:
    print(f"Унікальні значення для {col}:")
    print(df[col].value_counts())
