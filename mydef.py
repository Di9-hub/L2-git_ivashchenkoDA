while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Принимает два числа и возвращает их сумму")
    print("2 - Проверяет, является ли число простым")
    print("3 - Принимает список чисел и возвращает их среднее значение")
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        def add(x, y):
            return x + y

        result = add(5, 3)
        print(f"Сумма: {result}")

    elif choice == 2:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        print(f"17 простое? {is_prime(17)}")
        print(f"4 простое? {is_prime(4)}")
    elif choice == 3:
        def average(numbers):
            if not numbers:
                return 0  # Возвращаем 0, если список пуст, чтобы избежать ошибки деления на ноль
            return sum(numbers) / len(numbers)

        numbers = [1, 2, 3, 4, 5]
        print(f"Среднее значение: {average(numbers)}")
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break