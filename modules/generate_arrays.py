import numpy as np

class ArrayGenerator:
    @staticmethod
    def random_arrays():
        print("Генерація випадкових масивів:")
        # Генерація випадкового масиву розміром 5x5
        random_array = np.random.rand(5, 5)
        print(random_array)

    @staticmethod
    def non_random_arrays():
        print("Генерація невипадкових масивів:")
        # Генерація масиву з послідовними числами
        sequence_array = np.arange(10)
        print(sequence_array)

    @staticmethod
    def run():
        ArrayGenerator.random_arrays()
        ArrayGenerator.non_random_arrays()