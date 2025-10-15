import copy

def update_dict(original: dict, key, value) -> dict:
    copied = copy.deepcopy(original)
    copied[key] = value
    return copied

def append_tuple(tpl: tuple, item) -> tuple:
    return (*tpl, *[item])

def push(stack: list, item) -> list:
    return [item] + [x for x in stack]