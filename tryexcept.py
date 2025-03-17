while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Введите число")
    print("2 - Чтение файла")
    
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        def get_number_from_user():
            while True:
                try:
                    user_input = input("Введите число: ")
                    number = float(user_input)  # Преобразуем в float, чтобы обрабатывать и целые, и дробные числа
                    print(f"Вы ввели число: {number}")
                    break  # Выходим из цикла, если ввод успешен
                except ValueError:
                    print("Ошибка: Введите, пожалуйста, *число*.")

        get_number_from_user()
    elif choice == 2:
        def open_file_safely():
            try:
                with open("nonexistent_file.txt", "r") as f:
                    content = f.read()
                    print(content)
            except FileNotFoundError:
                print("Ошибка: Файл не найден.")
            except Exception as e:
                print(f"Произошла другая ошибка: {e}")

        open_file_safely()
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break