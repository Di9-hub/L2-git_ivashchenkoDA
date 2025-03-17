while True:
    
    print("Выберите действие, которое хотите выполнить:")
    print("1 - Hello, File! ")
    print("2 - Вывести содержимое файла")
    print("3 - Добавить новую строку")
    choice = int(input("Введите выбранное действие: "))
    if choice == 1:
        def create_and_write_file():
            try:
                with open("my_file.txt", "w") as f:
                    f.write("Hello, File!\n")  # Добавлен символ новой строки
                print("Файл успешно создан и запись произведена.")
            except Exception as e:
                print(f"Произошла ошибка при создании/записи файла: {e}")

        create_and_write_file()
    elif choice == 2:
        def read_file():
            try:
                with open("my_file.txt", "r") as f:
                    content = f.read()
                print(f"Содержимое файла:\n{content}")
            except FileNotFoundError:
                print("Файл не найден.")
            except Exception as e:
                print(f"Произошла ошибка при чтении файла: {e}")

        read_file()
    elif choice == 3:
        def append_to_file():
            try:
                with open("my_file.txt", "a") as f:
                    f.write("This is a new line.\n")
                print("Строка успешно добавлена в файл.")
            except FileNotFoundError:
                print("Файл не найден.")
            except Exception as e:
                print(f"Произошла ошибка при добавлении в файл: {e}")

        append_to_file()
    else:
        print("Вы ввели неправильный выбор, программа завершена")
        break