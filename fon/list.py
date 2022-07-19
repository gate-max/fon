
from fon.basics import all_iterable, all_str, is_iterable, is_str
from itertools import chain, repeat
from typing import Any, List



def chunks_of(n:int, xs) -> List[Any]:
    """
    chunks_of(0, 'hello world')   --> ''
    chunks_of(-2, 'hello world')   --> ''
    chunks_of(5, 'hello world')   --> ['hello', ' worl', 'd']
    chunks_of(3, rangel(10))       --> [[0,1,2], [3,4,5], [6,7,8], [9]]        
    chunks_of(0, rangel(10))       --> []        
    chunks_of(-2, rangel(10))      --> []             
    """
    return xs[:0] if not n else [xs[i:i + n] for i in range(0, len(xs), n)]


def concat(xs) -> Any:
    """returns a list of merging the original list of lists"""
    if all_str(xs):
        return ''.join(xs) 
    elif all_iterable(xs):
        return list(chain.from_iterable(xs))
    else:
        return []

def cons(x, xs) -> Any:
    if is_str(x) and is_str(x):
        return x + xs 
    elif is_iterable(xs):
        return [x] + list(xs)
    else:
        return []


def drop(drop: int, xs) -> Any:
    """works on lists, strings, ranges, it returns the original type"""
    return xs[drop:] if is_iterable(xs) else []


def dropl(drop: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[drop:]) if is_iterable(xs) else []

def drop_take(drop: int, take: int, xs) -> Any:
    """works on lists and strings"""
    return xs[drop:drop+take] if is_iterable(xs) else []


def drop_takel(drop: int, take: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[drop:drop+take]) if is_iterable(xs) else []

def head(xs) -> Any:
    """index out of range error on empty variable"""
    return xs[0]


def head_def(default_value, xs) -> Any:
    return default_value if not xs else xs[0]


def head_op(xs) -> Any:
    return None if not xs else xs[0]



def init(xs) -> Any:
    return xs[:-1]


def intercalate(xs, xss) -> str:
    """returns a combined list"""
    return concat(intersperse(xs, xss))



def intersperse(a, xs) -> List[Any]:
    """examples:
    intersperse(0, [1,2,3]  ---> [1,0,2,0,3] """
    ys = []
    for x in xs:
        ys.append(x)
        ys.append(a)
    return ys[:-1]


def last(xs) -> Any:
    """index out of range error on empty variable"""
    return xs[-1]



def replicate(i: int, x) -> List[Any]:
    """works on any types of data, always return a list"""
    return list(repeat(x, i))





def reverse(xs) -> Any:
    """can reverse lists, ranges and strings, return the original type"""
    return xs[::-1] if is_iterable(xs) else []


def reversel(xs) -> List[Any]:
    """reversel() always return a list, if this function is used in strings, it will return a list of characters / list of single string"""
    return list(xs[::-1]) if is_iterable(xs) else []


def tail(xs) -> Any:
    return xs[1:] if is_iterable(xs) else []


def take(i: int, xs) -> Any:
    """works on lists and strings"""
    return xs[:i] if i > 0 and is_iterable(xs) else []


def takel(i: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[:i]) if i > 0 and is_iterable(xs) else []
