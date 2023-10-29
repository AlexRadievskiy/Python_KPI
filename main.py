import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Завантажуємо дані
data = pd.read_csv('data/tips.csv')

# Перетворюємо категоріальні змінні в числові
le = LabelEncoder()
categorical_features = ['sex', 'smoker', 'day', 'time']
for feature in categorical_features:
    data[feature] = le.fit_transform(data[feature])

# 1) Прогнозування розміру чайових

# Визначаємо незалежні змінні (X) та залежну змінну (y)
X = data[['total_bill', 'size', 'sex', 'smoker']]  # можна додати інші ознаки для аналізу
y = data['tip']

# Розділяємо дані на тренувальні та тестові
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Створюємо модель лінійної регресії
model = LinearRegression()
model.fit(X_train, y_train)

# Робимо прогнози
predictions = model.predict(X_test)

# Оцінюємо модель
mse = mean_squared_error(y_test, predictions)
print(f"Середньоквадратична помилка: {mse}")

# 2) Кластерний аналіз

# Вибираємо ознаки для кластеризації
features_for_clustering = data[['total_bill', 'tip']]  # можна вибрати інші ознаки

# Створюємо модель k-середніх
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)  # вибрано 3 кластери для прикладу
kmeans.fit(features_for_clustering)

# Отримуємо мітки кластерів
data['cluster'] = kmeans.labels_

# Візуалізуємо кластери
plt.scatter(data['total_bill'], data['tip'], c=data['cluster'], cmap='viridis')
plt.xlabel('Загальний рахунок')
plt.ylabel('Чайові')
plt.title('Кластеризація розміру чайових')
plt.show()
