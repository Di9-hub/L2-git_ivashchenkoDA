def calculator():
    expression = input("Введите выражение (например, 2 + 2): ")

    try:
        num1, operator, num2 = expression.split()

        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Ошибка: деление на ноль!"
            result = num1 / num2
        else:
            return "Ошибка: неизвестный оператор!"

        return f"Результат: {result}"

    except ValueError:
        return "Ошибка: некорректный ввод. Пожалуйста, введите выражение в формате 'число оператор число'."

print(calculator())