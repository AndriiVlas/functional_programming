# 1. Генератор парних чисел у діапазоні
def even_in_range(start: int, end: int):
    for x in range(start, end):
        if x % 2 == 0:
            yield x

# 2. Ітератор по списку з пропуском елементів
class SkipIterator:
    def __init__(self, list: list, step: int):
        if step <= 0:
            raise ValueError("Крок не може бути нульовим або від'ємним")
        self.list = list
        self.step = step
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.list):
            raise StopIteration
        item = self.list[self.current]
        self.current += self.step
        return item

# 3. Генератор підрядків рядка
def substrings(s: str, k: int):
    n = 0
    while k <= len(s):
        yield s[:k]
        s = s[n:]
        n += 1

# 4. Перетворення списку кортежів у словник
def aggragare_pairs(pairs: list[tuple[str, int]]) -> dict[str, int]:
    product_quantity = {}
    for product, quantity in pairs:
        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity
    return product_quantity 

# 5. Генератор для "плаского" обходу вкладених списків
def flatten(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem

# 6. Перетворення словника в список кортежів і навпаки
def dict_to_tuples(d: dict) -> list[tuple]:
    return [(k, v) for k, v in d.items()]

def tuples_to_dict(pairs: list[tuple]) -> dict:
    return {k: v for k, v in pairs}

# 7. Фільтрація словника за умовою (через генератор/ітератор)
def filter_dict(d: dict[str, int], threshold: int) -> dict[str, int]:
    return {k: v for k, v in d.items() if v > threshold}

# 8. Генератор комбінованих даних зі списку і словника
def name_scores_pairs(names: list[str], scores: dict[str, int]):
    """Функція name_scores_pairs проходить по списку names та для кожного імені, що є у словнику scores, повертає кортеж (name, score). Якщо ім'я в словнику scores відсутнє — пропускає його.
    Аргументи:
        names (list[str]): Список імен студентів.
        scores (dict[str, int]): Словник, що містить імена студентів та кількість балів.
    """
    for name in names:
        if scores.__contains__(name):
            yield (name, scores[name])

# 9. Ітератор по словнику з фільтрацією ключів
class KeyFilterIterator:
    def __init__(self, d: dict, allowed_keys):
        self.d = d
        self.allowed_keys = allowed_keys
        self.current = iter(self.d.keys())
    
    def __iter__(self):
        return self
    
    def __next__(self):
        key = next(self.current)
        if self.allowed_keys.__contains__(key):
            return (key, self.d[key])

# 10. Генератор статистики по списку чисел
def running_stats(numbers: list[float]):
    count = 0
    current_sum = 0
    average = 0
    for x in numbers:
        count += 1
        current_sum += x
        average = current_sum / count
        yield (count, current_sum, average)