import numpy as np
import pandas as pd

class Statistics:

    @staticmethod
    def load_data():
        data = pd.read_csv('data/iris.csv')
        return np.array(data['petal.width'])

    @staticmethod
    def run():
        petal_width = Statistics.load_data()

        # Виведення статистичних характеристик
        print("Мінімальне значення:", np.min(petal_width))
        print("Максимальне значення:", np.max(petal_width))
        print("Вибіркове середнє:", np.mean(petal_width))
        print("Дисперсія:", np.var(petal_width))
        print("Середньоквадратичне відхилення:", np.std(petal_width))
        print("Медіана:", np.median(petal_width))
        print("25 персентиль:", np.percentile(petal_width, 25))
        print("75 персентиль:", np.percentile(petal_width, 75))
