from numbers import Number

from typing import Any, List


def all_bool(xs) -> bool:
    return all(map(is_bool, xs))


def all_float(xs) -> bool:
    return all(map(is_float, xs))


def all_int(xs) -> bool:
    return all(map(is_int, xs))

def all_iterable(xs) -> bool:
    return all(map(is_iterable, xs))


def all_list(xs) -> bool:
    return all(map(is_list, xs))

def all_num(xs) -> bool:
    return all(map(is_num, xs))


def all_str(xs) -> bool:
    return all(map(is_str, xs))


def all_tuple(xs) -> bool:
    return all(map(is_tuple, xs))



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

def is_num(x) -> bool:
    return isinstance(x, Number)

def is_str(x) -> bool:
    return isinstance(x, str)

def is_tuple(x) -> bool:
    return isinstance(x, tuple)


def not_bool(x) -> bool:
    return not is_bool(x)


def not_float(x) -> bool:
    return not is_float(x)

def not_int(x) -> bool:
    return not is_int(x)


def not_iterable(x) -> bool:
    return not is_iterable(x)


def not_list(x) -> bool:
    return not is_list(x)

def not_null(x) -> bool:
    return not null


def not_num(x) -> bool:
    return not is_num(x)


def not_str(x) -> bool:
    return not is_str(x)


def not_tuple(x) -> bool:
    return not is_tuple(x)


def null(x) -> bool:
    return bool(x)


