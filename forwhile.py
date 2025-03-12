while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Вывести все числа от 1 до 10")
    print("2 - Вывести все числа от 1 до N")
    print("3 - Сумма всех чисел от 1 до 100")
    
    choice = int(input("Введите выбранное действие: "))
    
    if choice == 1:
        print("Числа от 1 до 10 :")
        for i in range(1, 11):
            print(i)
    
    elif choice == 2:
        N = int(input("Введите число N: "))
        print(f"Числа от 1 до {N}:")
        for i in range(1, N + 1):
            print(i)
    
    elif choice == 3:
        summa = 0
        i = 1
        while i <= 100:
            summa += i
            i += 1

        print(f"Сумма чисел от 1 до 100 : {summa}")
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break