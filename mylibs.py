import random
import datetime
import math

while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Cлучайное число от 1 до 100 ")
    print("2 - Текущая дата и время")
    print("3 - Квадратный корень числа с math")
    print("4 - Квадратный корень числа без math")
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        def generate_random_number():
            random_number = random.randint(1, 100)
            print(f"Случайное число: {random_number}")

        generate_random_number()
    elif choice == 2:
        def print_current_datetime():
            now = datetime.datetime.now()
            print(f"Текущая дата и время: {now}")

        print_current_datetime()
    elif choice == 3:
        def calculate_square_root(number):
            try:
                sqrt = math.sqrt(number)
                print(f"Квадратный корень из {number} (с использованием math.sqrt): {sqrt}")
            except ValueError:
                print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа.")

        calculate_square_root(26)
        calculate_square_root(-4) # Обработка ошибки
    elif choice == 4:
        def calculate_square_root_without_math(number):
            if number < 0:
                print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа.")
                return

            x = number
            y = 1.0
            epsilon = 0.00001  # Точность вычислений
            while abs(x - y) > epsilon:
                x = (x + y) / 2
                y = number / x
            print(f"Квадратный корень из {number} (без math.sqrt): {x}")

        calculate_square_root_without_math(25)
        calculate_square_root_without_math(9)
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break