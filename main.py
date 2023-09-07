import sys
from modules.generate_arrays import ArrayGenerator
from modules.access_elements import ElementAccessor
from modules.arithmetic_operations import ArithmeticOperations
from modules.statistics import Statistics

def main():
    while True:
        if len(sys.argv) < 2:
            action = input("Вкажіть дію: generate, access, arithmetic, stats, exit: ")
        else:
            action = sys.argv[1]
            sys.argv.pop(1)  # видаляємо вже оброблений аргумент

        if action == "exit":
            print("Завершення програми.")
            break

        if action == "generate":
            ArrayGenerator.run()
        elif action == "access":
            ElementAccessor.run()
        elif action == "arithmetic":
            ArithmeticOperations.run()
        elif action == "stats":
            Statistics.run()
        else:
            print("Невідома дія. Виберіть з: generate, access, arithmetic, stats")


if __name__ == "__main__":
    main()