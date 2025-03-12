while True:
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Посчитать их сумму")
    print("2 - Преобразование + тип")
    print("3 - Вывести возраст")
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        print("Введите 1-е число:")
        a =input()
        print("Введите 2-е число:")
        b=input()
        sum= float(a) + float(b)
        print("Сумма чисел равна", sum)
    elif choice == 2:
        u = input("Введите число: ")
        value = int(u)
        print("Число:", value)
        print("Тип данных:", type(value))
    elif choice == 3:
        age = input("Введите ваш возраст: ")
        print("Вам", age, "лет.")
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break