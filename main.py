import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження даних
data = pd.read_csv('data/StudentsPerformance.csv')

# Завдання 1
# а) Кількість учнів кожної раси/етносу
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='race/ethnicity')
plt.title('Кількість учнів кожної раси/етносу')
plt.xlabel('Раса/Етнос')
plt.ylabel('Кількість учнів')
plt.show()

# б) Максимальні бали за математику у учнів кожної раси/етносу
max_scores = data.groupby('race/ethnicity')['math score'].max()
max_scores.plot(kind='bar', figsize=(10, 6))
plt.title('Максимальні бали за математику')
plt.xlabel('Раса/Етнос')
plt.ylabel('Максимальні бали')
plt.show()

# в) Середні бали за письмо у учнів кожної раси/етносу з розподілом за статтю
plt.figure(figsize=(12, 6))
sns.barplot(x='race/ethnicity', y='writing score', hue='gender', data=data, errorbar=None)
plt.title('Середні бали за письмо з розподілом за статтю')
plt.xlabel('Раса/Етнос')
plt.ylabel('Середні бали')
plt.show()

# Завдання 2
# Гістограма балів за читання
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='reading score', kde=True, hue='test preparation course', multiple="stack")
plt.title('Гістограма балів за читання')
plt.xlabel('Бали за читання')
plt.ylabel('Кількість учнів')
plt.show()

# Завдання 3
# Діаграма розмаху балів за математику
plt.figure(figsize=(12, 6))
sns.boxplot(x='parental level of education', y='math score', data=data)
plt.title('Діаграма розмаху балів за математику')
plt.xlabel('Рівень освіти батьків')
plt.ylabel('Бали за математику')
plt.xticks(rotation=45)
plt.show()

# Завдання 4
# а) Діаграми розсіювання
sns.jointplot(x='reading score', y='writing score', data=data, kind='scatter')
plt.suptitle('Залежність між балами за читання і письмо')
plt.show()

sns.jointplot(x='math score', y='reading score', data=data, kind='scatter')
plt.suptitle('Залежність між балами за математику і читання')
plt.show()

# б) Коефіцієнт кореляції
corr_reading_writing = data['reading score'].corr(data['writing score'])
print(f"Коефіцієнт кореляції між балами за читання і письмо: {corr_reading_writing}")

corr_math_reading = data['math score'].corr(data['reading score'])
print(f"Коефіцієнт кореляції між балами за математику і читання: {corr_math_reading}")
