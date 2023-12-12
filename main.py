import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# Завантаження даних
df = pd.read_csv('data/Stars.csv')

# Визначення цільової змінної та незалежних змінних
y = df['Type'].apply(lambda x: 1 if x in [0, 1] else 0)
X = df.drop(columns=['Type'])

# Кодування категоріальних змінних
X = pd.get_dummies(X)

# Розділення даних на навчальні та тестові набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Створення та навчання моделі логістичної регресії
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(random_state=0))
])
pipeline.fit(X_train, y_train)

# Оцінка моделі
predictions = pipeline.predict(X_test)
print("Класифікаційний звіт для логістичної регресії:")
print(classification_report(y_test, predictions))
print("Матриця невідповідностей:")
print(confusion_matrix(y_test, predictions))

# Покращення моделі за допомогою випадкового лісу
rf = RandomForestClassifier(random_state=0)
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [4, 6, 8],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Оцінка покращеної моделі
best_rf = grid_search.best_estimator_
rf_predictions = best_rf.predict(X_test)
print("Класифікаційний звіт для випадкового лісу:")
print(classification_report(y_test, rf_predictions))
print("Матриця невідповідностей:")
print(confusion_matrix(y_test, rf_predictions))
