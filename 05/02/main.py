"""
*   배열 제어하기

정수 배열을 하나 받고, 배열의 중복값을 제거하고 배열 데이터를 내림차순으로
정렬하여 반환하는 solution() 함수

*   제약조건

-   배열의 길이는 2 이상 1000 이하
-   각 배열의 데이터 값은 -100,000 이상 100,000 이하

"""

def solution(arr: list):
    #   set 함수는 해시알고리즘으로 O(N) 을 보장
    unique_list = list(set(arr))
    #   O(N log N)
    desc_unique_list = sorted(unique_list, reverse=True)
    
    return desc_unique_list
