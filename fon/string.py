from typing import Any, List
from fon.list import intersperse
from fon.type import all_str, is_str

def is_alpha(s: str) -> bool:
    return s.isalpha()

def is_alphanum(s: str) -> bool:
    return s.isalnum()


def is_ascii(s: str) -> bool:
    return s.isascii()


def is_decimal(s: str) -> bool:
    return s.isdecimal()



def is_digit(s: str) -> bool:
    return s.isdigit()


def is_lower(s: str) -> bool:
    return s.islower()

def is_numeric(s: str) -> bool:
    return s.isnumeric()


def is_print(s: str) -> bool:
    return s.isprintable()


def is_space(s: str) -> bool:
    return s.isspace()

def is_title(s: str) -> bool:
    return s.istitle()

def is_upper(s: str) -> bool:
    return s.isupper()



def lines(s: str) -> List[str]:
    return s.splitlines() if is_str(s) else []


def not_alpha(s: str) -> bool:
    return not is_alpha(s)


def not_ascii(s: str) -> bool:
    return not is_ascii(s)


def not_alphanum(s: str) -> bool:
    return not is_alphanum(s)

def not_decimal(s: str) -> bool:
    return not is_decimal(s)



def not_digit(s: str) -> bool:
    return not is_digit(s)

def not_lower(s: str) -> bool:
    return not is_lower(s)


def not_numeric(s: str) -> bool:
    return not is_numeric(s)

def not_space(s: str) -> bool:
    return not is_space(s)


def not_title(s: str) -> bool:
    return not is_title(s)



def not_upper(s: str) -> bool:
    return not is_upper(s)

def strip(s: str) -> str:
    return s.strip()

def strip_end(s: str) -> str:
    return s.rstrip()


def strip_start(s: str) -> str:
    return s.lstrip()


def unlines(xs: List[str]) -> str:
    return '\n'.join(xs) if all_str(xs) else ''

def unwords(xs: List[str]) -> str:
    return ' '.join(xs) if all_str(xs) else ''

def words(s: str) -> List[str]:
    return s.split() if is_str(xs) else []

