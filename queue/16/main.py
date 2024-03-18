"""
*   기능개발

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


*   제약 조건   

-   작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
-   작업 진도는 100 미만의 자연수입니다.
-   작업 속도는 100 이하의 자연수입니다.
-   배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

*   입출력의 예

progresses	                speeds	            return
[93, 30, 55]	            [1, 30, 5]	        [2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

*   문제 분석

-   앞의 작업이 완료된 이후 뒤의 후속작업을 같이 배포가능하다
-   한번에 배포가 가능한 수를 배열로 리턴한다
-   배포는 하루에 한번만 가능하며, 하루의 끝에 이루어진다
-   result 배열을 선언한다
-   progresses 의 length 가 0 이 될때까지 순회한다
    -   progresses 는 speeds 의 각 idx 로 더하기 연산이 이루어진다   
        -   만약 가장 첫번째 원소가 100 이면, 다음 원소들이 100 인 progresses 까지 leftpop 한다 
        -   leftpop 한 index 값을 result 배열에 append 한다
-   result 를 반환한다 

"""

from collections import deque

def solution(progresses, speeds):
    result = []
    progresses_deque = deque(progresses)
    speeds_deque = deque(speeds)
    count = 0
    idx = 0

    while len(progresses_deque) > 0:
        speed = speeds_deque.popleft()
        progress = progresses_deque.popleft() + speed

        if (progress >= 100 and idx == 0):
            count += 1
        else:
            if count > 0:
                result.append(count)
            progresses_deque.append(progress)
            speeds_deque.append(speed)
            idx += 1
            count = 0

        if len(progresses_deque) == 0:
            result.append(count) 

        if len(progresses_deque) > 0:
            idx = idx % len(progresses_deque)

    return result

