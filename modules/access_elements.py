import numpy as np

class ElementAccessor:
    @staticmethod
    def access_by_index():
        print("Доступ до елементів за індексом:")
        a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(f"Масив a:\n{a}")
        print(f"a[1]: {a[1]}")
        print(f"a[-2]: {a[-2]}")
        print(f"a[0, -1]: {a[0, -1]}")

    @staticmethod
    def subarrays():
        print("Виділення підмасивів:")
        a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(f"Масив a:\n{a}")
        print(f"Підмасив a[1:3]:\n{a[1:3]}")
        print(f"Підмасив a[:, 1:3]:\n{a[:, 1:3]}")

    @staticmethod
    def run():
        ElementAccessor.access_by_index()
        ElementAccessor.subarrays()