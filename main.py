import sys
from modules import generate_arrays, access_elements, arithmetic_operations, statistics

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
            generate_arrays.run()
        elif action == "access":
            access_elements.run()
        elif action == "arithmetic":
            arithmetic_operations.run()
        elif action == "stats":
            statistics.Statistics.run()
        else:
            print("Невідома дія. Виберіть з: generate, access, arithmetic, stats, exit")


if __name__ == "__main__":
    main()