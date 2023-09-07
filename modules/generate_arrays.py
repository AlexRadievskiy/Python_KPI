import numpy as np

class ArrayGenerator:
    @staticmethod
    def random_arrays():
        # Код для генерації випадкових масивів
        print("Генерація випадкових масивів:")
        # Пример генерации массива
        arr = np.random.randint(0, 100, 10)
        print(arr)

    @staticmethod
    def non_random_arrays():
        # Код для генерації невипадкових масивів
        print("Генерація невипадкових масивів:")
        # Пример генерации массива
        arr = np.arange(10)
        print(arr)

    @staticmethod
    def run():
        ArrayGenerator.random_arrays()
        ArrayGenerator.non_random_arrays()