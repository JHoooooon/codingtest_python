"""
*  두 개의 수로 특정값 만들기

n 개의 양의 정수로 이루어진 리스트 arr 와 정수 target 이 주어졌을때
이 중에서 합이 target 인 두 정수가 arr 에 있는지 찾고, 있으면 True, 없으면 False 
를 반환하는 solution 함수를 작성하시오

*   제약조건

-   n 은 2 이상 10000 이하의 자연수이다
-   arr 의 각 원소는 1 이상 10000 이하의 자연수이다
-   arr 의 원소 중 중복되는 원소는 없다
-   target 은 1 이상 20000 이하의 자연수

*   입출력

arr                     target              return
[1,2,3,4,8]             6                   True
[2,3,5,9]               10                  False
"""
from collections import deque 

#   O(N^2) 이다
#   O(N) 으로 해결하려고 했는데, 결국은 O(N^2) 가 되었다
def solution(arr, target):
    remain_arr = deque()
    queue = deque(arr)
    
    while(len(queue) > 0):
        first = queue.popleft()
        second = queue.popleft()
        isTarget = first + second == target

        if isTarget:
            return True
        else:
            remain_arr.append(second)
            queue.appendleft(first)
        
        if len(queue) == 1:
            queue = remain_arr
            remain_arr = deque()

        if len(queue) == 1 and len(remain_arr) == 0:
            break

    return False

print(solution(
    [1,1,1,1,1,2], 8
))