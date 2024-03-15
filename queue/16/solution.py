"""
*   책의 솔루션

-   각 일수를 구한 배열인 days_left 를 구한다
-   구해진 일수에서 첫번째 원소의 일수를 max_day 에 할당한다
-   각 원소들을 순회하며, max_day 보다 작거나 같으면 count 를 1씩 합산한다
-   만약 max_day 보다 크면, 
    -   max_day 를 days_left[idx] 로 할당한다
    -   이전 count 값을 answer 배열에 append 한다
    -   count 값은 1 로 초기화한다
-   같은 로직을 반복한다
-   마지막 idx 는 count 를 합산하고 끝나므로,
    합산된 count 를 append 하여 마무리한다
-   answer 를 반환한다

"""
from math import ceil

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days_left = [ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    max_day = days_left[0]
    count = 0

    for idx in range(n):
        if days_left[idx] <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = days_left[idx]
            count = 1

    answer.append(count)

    return answer;