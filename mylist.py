while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Список из 5 чисел и выводит их сумму")
    print("2 - Максимальное число в списке")
    print("3 - Удалить дубликаты из списка")
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        def sum_list():
            numbers = [1, 2, 3, 4, 5]
            total = sum(numbers)
            print(f"Сумма чисел в списке: {total}")
        sum_list()

    elif choice == 2:
        def find_max():
            numbers = [5, 2, 9, 1, 5, 6]
            maximum = max(numbers)
            print(f"Максимальное число в списке: {maximum}")
        find_max()
    elif choice == 3:
        def remove_duplicates():
            numbers = [1, 2, 2, 3, 4, 4, 5]
            unique_numbers = list(set(numbers))
            print(f"Список с удаленными дубликатами: {unique_numbers}")

        remove_duplicates()
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break    