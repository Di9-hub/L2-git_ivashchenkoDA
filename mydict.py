while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - словарь с информацией о студенте")
    print("2 - объединяет два словаря в один")
    print("2 - есть ли определенный ключ в словаре")
    
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        student = {
            "имя": "Дима",
            "возраст": 23,
            "курс": 1
        }

        print("Информация о студенте:")
        for key, value in student.items():
            print(f"{key}: {value}")

    elif choice == 2:
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        merged_dict = {**dict1, **dict2}
        print("Объединенный словарь:", merged_dict)
    elif choice == 3:
        my_dict = {"name": "Дима", "age": 23, "city": "Tokyo"}

        key_to_check = "age"

        if key_to_check in my_dict:
            print(f"Ключ '{key_to_check}' присутствует в словаре.")
        else:
            print(f"Ключ '{key_to_check}' отсутствует в словаре.")
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break    