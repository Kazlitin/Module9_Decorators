def sum_three(a, b, c):
    """Суммирует три числа."""
    return a + b + c

def is_prime(func):
    """Декоратор для проверки, является ли результат функции простым числом."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, result):
                if (result % i) == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def add_three(a, b, c):
    return sum_three(a, b, c)

result = add_three(2, 3, 6)
print(result)