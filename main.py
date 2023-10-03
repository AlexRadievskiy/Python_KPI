import pandas as pd

# Завантаження даних
data = pd.read_csv('data/penguins.csv')

# Виведення інформації про набір даних
print(data.info())

# Виведення основних статистичних характеристик
print(data.describe())

# Визначення типів ознак
print(data.dtypes)

# Копія частини даних
subset_data = data.iloc[10:20].copy()

# Встановлення нових індексів і стовпців
subset_data.index = [f'new_index_{i}' for i in range(10)]
subset_data.columns = [f'new_col_{col}' for col in subset_data.columns]

# Додавання нового рядка
new_row = pd.DataFrame({
    'new_col_species': ['New_Species'],
    'new_col_island': ['New_Island'],
    # ... для інших стовпців
}, index=['new_index_10'])

subset_data = pd.concat([subset_data, new_row])

# а) Кількість самців і самок на кожному з островів
sex_count_per_island = data.groupby('island')['sex'].value_counts()
print(sex_count_per_island)

# б) Самці Аделі, що мають масу понад 3 кг
adelie_males_over_3kg = data[(data['species'] == 'Adelie') & (data['sex'] == 'Male') & (data['body_mass_g'] > 3000)]
print(adelie_males_over_3kg)

# в) Додавання стовпця: чи перевищує глибина дзьобу половину довжини дзьобу
data['beak_depth_gt_half_length'] = data['culmen_length_mm'] / 2 < data['flipper_length_mm']
print(data[['culmen_length_mm', 'flipper_length_mm', 'beak_depth_gt_half_length']])

# г) Додавання стовпця: середня вага пінгвінів даного виду
mean_weight_per_species = data.groupby('species')['body_mass_g'].mean()
data['mean_weight_per_species'] = data['species'].map(mean_weight_per_species)
print(data[['species', 'body_mass_g', 'mean_weight_per_species']])
