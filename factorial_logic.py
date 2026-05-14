def calculate_factorial(n):
    """Обчислює факторіал числа n за допомогою циклу for"""
    if n < 0:
        return "Помилка: Факторіал не існує для від'ємних чисел"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result