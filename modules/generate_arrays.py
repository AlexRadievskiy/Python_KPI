import numpy as np

class ArrayGenerator:
    @staticmethod
    def random_arrays():
        print("Генерація випадкових масивів:")
        arr = np.random.randint(0, 100, 10)
        print(arr)

    @staticmethod
    def non_random_arrays():
        print("Генерація невипадкових масивів:")
        arr = np.arange(10)
        print(arr)

    @staticmethod
    def run():
        ArrayGenerator.random_arrays()
        ArrayGenerator.non_random_arrays()