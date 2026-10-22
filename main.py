print("=== КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР ===")

OPERATIONS = ["+", "-", "*", "/", "//", "%", "^"]


def read_number(prompt):
    """Запрашивает число, пока пользователь не введёт корректное значение."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Ошибка: необходимо ввести число. Попробуйте ещё раз.")


def read_operation():
    """Запрашивает операцию, пока пользователь не введёт допустимую."""
    while True:
        operation = input(f"Введите операцию ({', '.join(OPERATIONS)}): ").strip()
        if operation in OPERATIONS:
            return operation
        print("Ошибка: неизвестная операция. Попробуйте ещё раз.")


def ask_continue(prompt):
    """Спрашивает да/нет, пока пользователь не даст корректный ответ."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["да", "д"]:
            return True
        if answer in ["нет", "н"]:
            return False
        print("Ошибка: введите «да» или «нет».")


def calculate(first, operation, second):
    """Возвращает результат или None, если произошло деление на ноль."""
    if operation in ["/", "//", "%"] and second == 0:
        return None
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        return first / second
    if operation == "//":
        return first // second
    if operation == "%":
        return first % second
    return first ** second


def format_number(value):
    """Убирает лишний .0 у целых результатов: 50.0 -> 50."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


while True:
    print()
    first = read_number("Введите первое число: ")
    operation = read_operation()
    second = read_number("Введите второе число: ")

    try:
        result = calculate(first, operation, second)
    except OverflowError:
        print("\nОшибка: результат слишком большой.")
    else:
        if result is None:
            print("\nОшибка: деление на ноль.")
        else:
            print(f"\nРезультат: {format_number(result)}")

    print()
    if not ask_continue("Хотите выполнить ещё одну операцию? (да/нет): "):
        break

print("\nРабота программы завершена.")
