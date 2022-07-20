
from fon.type import all_iterable, all_str, is_int, is_iterable, is_list, is_str, not_int, null, not_null
from itertools import chain, repeat
from typing import Any, List



def chunks_of(i:int, xs) -> List[Any]:
    """
    chunks_of(0, 'hello world')   --> ''
    chunks_of(-2, 'hello world')   --> ''
    chunks_of(5, 'hello world')   --> ['hello', ' worl', 'd']
    chunks_of(3, rangel(10))       --> [[0,1,2], [3,4,5], [6,7,8], [9]]        
    chunks_of(0, rangel(10))       --> []        
    chunks_of(-2, rangel(10))      --> []             
    """
    if is_int(i) and is_iterable(xs):
        return [xs[i:i + n] for n in range(0, len(xs), i)] if i > 0 else xs[:0]
    else:
        return []


def concat(xs) -> Any:
    """
    concat(["never", "the", "less"])   --> "nevertheless"
    concat([[1,9,6], [1,6,8],[0],[1]])  --> [1,9,6,1,6,8,0,1]
    concat([[9,8,7], range(5), (None, 'hi', True)])  --> [9,8,7,0,1,2,3,4,None, 'hi', True]
    concat([0, [9,8,7], range(5), (None, 'hi', True)])  --> []
    concat(None)  --> []
    returns a list of merged original list
    """    
    if all_str(xs):
        return ''.join(xs) 
    elif all_iterable(xs):
        return list(chain.from_iterable(xs))
    else:
        return []

def cons(x, xs) -> Any:
    """
    cons('a','men') ---> 'amen'
    cons('go','daddy')  ---> 'godaddy'
    cons('go', ['down', 'and', 'eat']) -->  ['go', 'down', 'and', 'eat']
    cons('go', (1, 0))   --> ['go', 1, 0]
    cons([1], [])        ---> [[1]]
    cons(0, None )     ---> []
    cons([3], 4)       ---> []
    """
    if is_str(x) and is_str(xs):
        return x + xs 
    elif is_iterable(xs):
        return [x] + list(xs)
    else:
        return []


def drop(i: int, xs) -> Any:
    """
    drop(2, 'woman')   --> 'man'
    drop(6, 'woman')   --> ''
    drop(0, 'hello')   --> 'hello'
    drop(-1, 'hello')  ---> 'hello'
    drop(1.5, 'hello')  ---> ''

    works on lists, strings, ranges, it returns the original type
    """
    if is_int(i) and is_iterable(xs):
        return xs[i:] if i > 0 else xs 
    elif is_iterable(xs):        # i is not int 
        return xs[:0]            # return '' or [] if i is not int
    else:
        return []


def dropl(i: int, xs) -> List[Any]:
    """always returns a list"""
    if is_int(i) and is_iterable(xs):
        return list(xs[i:]) if i > 0 else list(xs)
    else:
        return []

def drop_take(d: int, t: int, xs) -> Any:
    """works on lists and strings"""
    return take(t,(drop(d, xs)))


def drop_takel(d: int, t: int, xs) -> List[Any]:
    """always returns a list
    """
    return takel(t,(dropl(d, xs)))


def head(xs) -> Any:
    """index out of range error on empty variable"""
    return xs[0]


def head_def(default_value, xs) -> Any:
    if is_iterable(xs) and not_null(xs):
        return xs[0]
    else:
        return default_value 


def head_op(xs) -> Any:
    if is_iterable(xs) and not_null(xs):
        return xs[0]
    else:
        return None



def init(xs) -> Any:
    return xs[:-1] if is_iterable(xs) else []


def intercalate(xs, xss) -> str:
    """
    intercalate(' ', ['go', 'down', 'and', 'eat'])  --> 'go down and eat'
    intercalate(', ', ('go', 'down', 'and', 'eat'))  --> 'go, down, and, eat'
    intercalate([0], [[1,2,3], [4,5], [6,7])  ---> [1,2,3,0,4,5,0,6,7]
    intercalate([1], ['hello', 3])        ---> []
    intercalate(1, ['hello', 'world'])    ---> []
    returns a combined list
    """
    if is_iterable(xs) and all_iterable(xss):
        return concat(intersperse(xs, xss))
    else:
        return []



def intersperse(a, xs) -> List[Any]:
    """
    intersperse(' ', 'hello')  ---> 'h e l l o' 
    intersperse(0, [1,2,3]     ---> [1,0,2,0,3] 
    intersperse(0, (1,2)]      ---> [1,0,2]
    intersperse(0, range(5)]   ---> [0,0,1,0,2,0,3,0,4]
    intersperse(0, 1)          ---> []     # 2nd arg is not iterable
    """
    ys = []
    if is_str(a) and is_str(xs):
        for x in xs:
            ys.append(x)
            ys.append(a)
        return ''.join(ys[:-1])    
    elif is_iterable(xs):
        for x in xs:
            ys.append(x)
            ys.append(a)
        return ys[:-1]
    else:
        return []


def last(xs) -> Any:
    """index out of range error on empty variable"""
    return xs[-1]


def last_def(default_value, xs) -> Any:
    if is_iterable(xs) and not_null(xs):
        return xs[-1]
    else:
        return default_value 


def last_op(xs) -> Any:
    if is_iterable(xs) and not_null(xs):
        return xs[-1]
    else:
        return None


def replicate(i: int, x) -> List[Any]:
    """works on any types of data, always return a list"""
    return list(repeat(x, i)) if is_int(i) else []


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
    if is_int(i) and is_iterable(xs):
        return xs[:i] if i > 0 else xs[:0] 
    elif is_iterable(xs):        # i is not int 
        return xs[:0]            # return '' or [] if i is not int
    else:
        return []


def takel(i: int, xs) -> List[Any]:
    """always returns a list"""
    if is_int(i) and i > 0 and is_iterable(xs):
        return list(xs[:i]) 
    else:
        return []
