# 1. Логування викликів
def log_calls(func):
    def inner(x: int, y: int) -> int:
        result = func(x, y)
        print(f"{func.__name__} = {result}")
        return func(x, y)
    return inner

@log_calls
def add(a: int, b: int) -> int:
    return a + b

# 2. Вимірювання часу виконання
import time
def timeit(func):
    def inner(x: int):
        start = time.time()
        result = func(x)
        end = time.time()
        duration = (end - start) * 1000
        print(f"{func.__name__} took {round(duration)} ms")
        return func(x)
    return inner

@timeit
def slow(n: int) -> int:
    time.sleep(0.05)
    return n*n

# 3. Перевірка "сильного" пароля (any/all)
def is_strong_password(s: str) -> bool:
    return (s.__len__() >= 8) and any(x.isupper() for x in s) and any(x.isdigit() for x in s) and any(x.islower() for x in s) and not all(x.isalnum() for x in s)

# 4. Чи всі значення "приблизно рівні"? (all)
from typing import Iterable
def all_close(xs: Iterable[float], tol: float = 1e-6) -> bool:
    min = xs[0] - tol
    max = xs[0] + tol
    return all(x >= min and x <= max for x in xs)

# 5. Є хоч одне просте число? (any + lambda)
import math
def has_prime(nums: Iterable[int]) -> bool:
    return any(map(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)), nums))

# 6. Масштабування і зсув (map + lambda)
def scale_and_shift(xs: Iterable[float], scale: float, shift: float) -> list[float]:
    return list(map(lambda x: x * scale + shift, xs))

# 7. Фільтрація e-mail (filter + lambda)
def filter_emails(items: Iterable[str]) -> list[str]:
    return list(filter(lambda s: '.' in s.split('@')[-1], items))

# 8. Частотний словник символів (reduce + lambda)
def char_hist(s: str) -> dict[str, int]:
    return [1]

#9. Топ-K студентів за балом (lambda як key)
def top_k(students: list[dict[str, int | str]], k: int) -> list[str]:
    return [1]

#10. Нормалізація даних (map + lambda)
def minmax_scale(xs: list[float]) -> list[float]:
    if (min(xs) == max(xs)):
        return list(map(lambda x: 0, xs))
    return list(map(lambda x: (x - min(xs)) / (max(xs) - min(xs)), xs))


print(add(2, 3))

print(slow(10))

print(is_strong_password("Qwerty12!"))
print(is_strong_password("qwerty12"))

print(all_close([1.0, 1.0000005, 0.9999999], tol=1e-5))
print(all_close([1.0, 1.1], tol=1e-3))

print(has_prime([4, 6, 8, 9]))
print(has_prime([4, 6, 7, 9, 10]))

print(scale_and_shift([1, 2, 3], 2.0, -1.0))

emails = ["a@b.com", "wrong@", "x@y", "john.doe@mail.org"]
print(filter_emails(emails))

print(char_hist("aba c"))

students = [{"name":"Ann","score":90},{"name":"Bob","score":95},{"name":"Ada","score":95}]
print(top_k(students, 2))

print(minmax_scale([10, 20, 30]))
print(minmax_scale([5, 5, 5]))