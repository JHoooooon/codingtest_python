"""
정수 배열을 정렬해서 반환

*   제약조건
    -   정수 배열의 길이는 2 이상 105 이하
    -   정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하

"""

from lib.measure_time import measure_time
from test import INPUT

def solution(arr: list) -> list:
    """sorted 를 사용한 정렬

    Args:
        arr (list): 배열

    Returns:
        list (int): 반환배열
    """

    #   O(N log N)
    return sorted(arr)

def bubble_sort(arr: list):
    """
    Bubble 정렬

    Args:
        arr (list): 배열

    Returns:
        list (int): 반환배열
    """
    n = len(arr)

    #   O(n^2)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[i] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#   10000 개의 배열
arr = list(range(10000))


print(measure_time(bubble_sort, arr))  #   8.231...초
print(measure_time(solution, arr))     #   0.00033...초