from numbers import Number

from typing import Any, List


def all_bool(xs) -> bool:
    return all(map(is_bool, xs))

def all_int(xs) -> bool:
    return all(map(is_int, xs))

def all_str(xs) -> bool:
    return all(map(is_str, xs))




def is_bool(x) -> bool:
    return isinstance(x, bool)


def is_float(x) -> bool:
    return isinstance(x, float)

def is_int(x) -> bool:
    return isinstance(x, int)

def is_iterable(x) -> bool:
    return hasattr(x, '__iter__') or hasattr(x, '__getitem__')

def is_list(x) -> bool:
    return isinstance(x, list)

def is_number(x) -> bool:
    return isinstance(x, Number)

def is_str(x) -> bool:
    return isinstance(x, str)

def is_tuple(x) -> bool:
    return isinstance(x, tuple)



