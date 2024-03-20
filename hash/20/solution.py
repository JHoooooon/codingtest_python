"""
*   책의 솔루션

-   hash 를 사용하여 해결한다

-   hash 로 해결하기 위해 계수정렬방법으로 처리한다
    -   데이터의 빈도수를 정렬한다.
    -   오름차순으로 각 인덱스를 빈도수 만큼 채워 출력하면 자연스럽게 오름차순으로 정렬한 배열이 나온다

-   (target - arr 의 원소) 가 계수정렬된 데이터가 존재한다면, 
    arr 의 원소 + (target - arr 의 원소) = target 이 된다
    그러므로 True 이다

-   아니면 False 이다
"""

#   O(N + M) 
def solution(arr, target):
    #   계수 정렬할 배열
    arr_count = [0 for _ in range(target + 1)]

    #   개수 정렬한다
    #   해당 원소가 target 보다 작거나 같으면
    #   개수 정렬 배열의 해당 원소에 1 값을 준다
    for i in arr:
        if i <= target:
            arr_count[i] = 1

    #   배열을 순회한다
    for i in arr:
        #   target - i 값을 하여, i 값과의 차이를 구한다
        t = target - i

        #   t 가 i 와 같지 않고(같은값이 더했을때 target 이 되는수 제외),
        #   t 가 0 보다 크거나 같고   
        #   t 가 target 보다 작거나 같고 (0 ~ target 까지의 수로 제한)
        #   arr_count[t] 가 1 이면 (arr_count[t] 가 있다면, 계수 정렬된 값이므로 i 와 더했을때 target 이 되는값이 나온다)
        #   True
        #   아니면 False
        if (
            t != i and 
            t >= 0 and
            t <= target and
            arr_count[t] == 1
        ):
            return True
    return False