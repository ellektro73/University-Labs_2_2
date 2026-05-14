import factorial_logic


# Функція користувача 1: Обчислення виразу z
def calculate_z(x, y):
    if x > 8:
        z = 3 + y
    else:
        z = 9 * x * y
    return z


def main():
    print("Програма з використанням власного модуля")
    try:
        # Робота з першою функцією
        x = float(input("Введіть x для обчислення z: "))
        y = float(input("Введіть y для обчислення z: "))
        z_res = calculate_z(x, y)
        print(f"Результат z = {z_res}")

        print("\nВиклик функції з підключеного модуля")
        n = int(input("Введіть ціле число n для факторіала: "))

        # Виклик функції з модуля factorial_logic
        fact_res = factorial_logic.calculate_factorial(n)
        print(f"Результат {n}! = {fact_res}")

    except ValueError:
        print("Помилка: введіть коректні числові дані.")


if __name__ == "__main__":
    main()