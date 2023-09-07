import sys
from modules import generate_arrays, access_elements, arithmetic_operations, statistics

def main():
    if len(sys.argv) < 2:
        action = input("Вкажіть дію: generate, access, arithmetic, stats: ")
    else:
        action = sys.argv[1]

    # Видаліть наступний рядок, оскільки ви вже визначили змінну "action" вище
    # action = sys.argv[1]

    if action == "generate":
        generate_arrays.run()
    elif action == "access":
        access_elements.run()
    elif action == "arithmetic":
        arithmetic_operations.run()
    elif action == "stats":
        statistics.Statistics.run()
    else:
        print("Невідома дія. Виберіть з: generate, access, arithmetic, stats")

if __name__ == "__main__":
    main()