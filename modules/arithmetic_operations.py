import numpy as np

class ArithmeticOperations:
    @staticmethod
    def basic_operations():
        print("Основні арифметичні операції:")
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(f"a + b = {a + b}")
        print(f"a - b = {a - b}")
        print(f"a * b = {a * b}")

    @staticmethod
    def advanced_operations():
        print("Розширені арифметичні операції:")
        a = np.array([1, 2, 3])
        # Reduce - застосовує задану операцію до елементів масиву
        print(f"Сума елементів масиву a: {np.add.reduce(a)}")
        # Accumulate - застосовує задану операцію кумулятивно
        print(f"Кумулятивна сума елементів масиву a: {np.add.accumulate(a)}")
        # Outer - обчислює зовнішній добуток двох масивів
        b = np.array([4, 5])
        print(f"Зовнішній добуток масивів a та b:\n{np.multiply.outer(a, b)}")

    @staticmethod
    def run():
        ArithmeticOperations.basic_operations()
        ArithmeticOperations.advanced_operations()
