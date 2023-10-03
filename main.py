import pandas as pd
from scipy import stats

# Завантаження даних
data = pd.read_csv('data/Budget.csv')

# 1. Середній вік та середньоквадратичне відхилення найстаршого в сім’ї
max_age = data['age'].max()
max_age_group = data[data['age'] == max_age]
mean_age = max_age_group['age'].mean()
std_age = max_age_group['age'].std()

print(f"Середній вік: {mean_age}, Середньоквадратичне відхилення: {std_age}")

# 2. Перевірка нормальності розподілу витрат на одежу
w, p_value = stats.shapiro(data['wcloth'])
if p_value > 0.05:
    print("Витрати на одежу розподілені нормально")
else:
    print("Витрати на одежу не розподілені нормально")

# 3. Зв’язок між кількістю дітей і витратами на алкоголь
correlation, _ = stats.pearsonr(data['children'], data['walc'])
print(f"Кореляція між кількістю дітей і витратами на алкоголь: {correlation}")

# 4. Порівняння витрат на їжу в сім’ях з однією та двома дітьми
group_1 = data[data['children'] == 1]['wfood']
group_2 = data[data['children'] == 2]['wfood']

t_stat, p_val = stats.ttest_ind(group_1, group_2)
if p_val < 0.05:
    print("Є статистично значуща різниця між витратами на їжу в сім’ях з однією та двома дітьми")
else:
    print("Немає статистично значущої різниці між витратами на їжу в сім’ях з однією та двома дітьми")
