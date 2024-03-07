from time import time
from typing import Callable

def measure_time(func: Callable[[ list ], list], arr: list):
    start_time = time()
    func(arr)
    end_time = time()
    return end_time - start_time
