import os
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """функция, которая складывает два числа"""

    return a + b


a = 2
b = 5
print(add(a, b))
