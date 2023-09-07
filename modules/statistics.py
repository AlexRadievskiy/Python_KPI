import numpy as np
import pandas as pd

class Statistics:
    @staticmethod
    def load_data():
        data = pd.read_csv('../data/iris.csv')
        return np.array(data['petal_width'])

    @staticmethod
    def compute_statistics(petal_width):
        # Ваш код для виведення статистичних характеристик
        pass

    @staticmethod
    def run():
        petal_width = Statistics.load_data()
        Statistics.compute_statistics(petal_width)
