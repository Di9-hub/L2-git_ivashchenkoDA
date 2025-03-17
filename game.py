import random

def guess_the_number():
    secret_number = random.randint(0, 10)
    attempts = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас есть {attempts} попытки, чтобы угадать число от 0 до 10.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка №{attempt}")
        try:
            guess = int(input("Введите ваше число: "))

            if guess == secret_number:
                print("Поздравляем! Вы угадали число!")
                return
            elif guess < secret_number:
                print("Неверно! Загаданное число больше.")
            else:
                print("Неверно! Загаданное число меньше.")
        except ValueError:
            print("Ошибка: введите целое число.")

    print(f"\nК сожалению, вы проиграли. Загаданное число было: {secret_number}.")

guess_the_number()