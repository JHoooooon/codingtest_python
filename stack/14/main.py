"""
*   표 편집

업무용 소프트웨어를 개발하는 니니즈웍스의 인턴인 앙몬드는 명령어 기반으로 표의 행을 선택, 삭제, 복구하는 프로그램을 작성하는 과제를 맡았습니다. 

단, 한 번에 한 행만 선택할 수 있으며, 표의 범위(0행 ~ 마지막 행)를 벗어날 수 없습니다. 이때, 다음과 같은 명령어를 이용하여 표를 편집합니다.

-   "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
-   "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
-   "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
-   "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

*   제한사항

-   5 ≤ n ≤ 1,000,000

-   0 ≤ k < n

-   1 ≤ cmd의 원소 개수 ≤ 200,000

-   cmd의 각 원소는 "U X", "D X", "C", "Z" 중 하나입니다.

-   X는 1 이상 300,000 이하인 자연수이며 0으로 시작하지 않습니다.

-   X가 나타내는 자연수에 ',' 는 주어지지 않습니다. 예를 들어 123,456의 경우 123456으로 주어집니다.

-   cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다.

-   표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않습니다.

-   본문에서 각 행이 제거되고 복구되는 과정을 보다 자연스럽게 보이기 위해 "이름" 열을 사용하였으나, "이름"열의 내용이 실제 문제를 푸는 과정에 필요하지는 않습니다. "이름"열에는 서로 다른 이름들이 중복없이 채워져 있다고 가정하고 문제를 해결해 주세요.

-   표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.

-   원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.

-   정답은 표의 0행부터 n - 1행까지에 해당되는 O, X를 순서대로 이어붙인 문자열 형태로 return 해주세요.

*   문제 이해

-   n   =   행 개수
-   k   =   시작 위치 (표는 0 부터 시작)
-   cmd =   명령어 배열 
    -   "U X" 는 위로 X 만큼 이동 
    -   "D X" 는 아래로 X 만큼 이동
    -   "C" 는 현재 있는 위치를 제거
    -   "Z" 는 이전 삭제 복구
-   결과는 모든 명령을 수행한 후, 표의 상태
    -   삭제되지 않은 행    O
    -   삭제된 행           X

*   구현할 코드 정리

-   current_idx 변수 생성   
    -   처음은 k 로 시작
    -   이후 변경시 currnet_idx 가 변경

-   undo_list 배열 생성
    -   "Z" 시 index 값을 저장

-   table_list 문자열 생성   
    -   값은 O 로 할당
    -   cmd 순회
        -   current_idx 를 기준으로 배열 처리 
        -   "C" 명령시 current_idx 위치값을 "X" 로 표시 및 current_idx 를 undo_list 에 append
            -   만약, current_idx 가 n - 1 이라면, current_idx =- 1
            -   그렇지 않다면                      current_idx += 1
            -   이동한 값이 "X" 값이라면, "X" 를 건너띄고 그 다음으로 이동
        -   "Z" 명령시 undo_list 를 pop
            -   pop 된 index 값을 "O" 로 변경   
            -   current_idx 값은 +- 1
                -   pop 된 index 가 current_idx 보다 작으면 += 1
                -   pop 된 index 가 current_idx 보다 크면 -= 1
        -   "U N" 명령시 current_idx -= N
            -   current_idx 가 0 보다 작다면 current_idx = 0
            -   이동한 idx 가 "X" 라면 건너띄고 그다음 idx 로 currnet_idx -= 1
        -   "D N" 명령시 current_dix += N
            -   current_idx 가 n - 1 보다 크다면 current_idx = n - 1
            -   이동한 idx 가 "X" 라면 건너띄고 그다음 idx 로 currnet_idx += 1

-   변경된 table_list 반환

---------------------------

*   문제점

-   풀이 실패

-   "X" 값을 건너띄는 부분
    -   pop 된 인덱스만큼 순회를 해야 하는데, 이는 비용이든다 (O(N^2))
    -   해당 pop 된 인덱스 만큼 건너띄고 current_idx 를 업데이트하는 방법 구현못함
    -   첫번째 원소와 마지막 원소에 대한 처리

-----------------------------

*   책에서의 풀이

-   인덱스만 연산
    -   N = 4, k = 2 일때 

    -   cmd 명령할 up, down 처리할 배열 생성
        -   up = [i - 1 for i in range(N)]
            up = [-1, 0, 1, 2]
            이렇게 하는 이유는, up 시 idx = 3 에서 2, 1, 0 으로 선택되므로, 마지막 3 은 없어도 된다
            대신, 0 에서 up 시에 처리할 로직으로 -1 을 넣는다.

        -   down = [i + 1 for i in range(N)]
            down = [1, 2, 3, 4]

            조금더 쉽게 이해하려면 가운데에 중간값을 넣어보면 왜 이렇게 했는지 이해가 간다
            up      = [-1, 0, 1, 2]
            k       =   0  1  2  3
            down    = [ 1, 2, 3, 4]

            위를 보면 0 1, 0 1 2, 1 2 3, 2 3 4 로 연결되는것을 볼 수 있다
            k 의 값이 1 이면 k 의 up 은 0, down 은 2 이다
            위의 up, down 은 이러한 특성을 만든것이다

    -   이는 다음처럼 계산된다(k = 2)
        -   cmd = "U 1" 은 다음처럼 계산된다
            k = up[k]   #   1
        -   cmd = "D 1" 은 다음처럼 계산된다
            k = down[k] #   3
        -   [1, k, 3] 순으로 정렬되어있으므로, k 의 up 은 1 이며, down 은 3 이 맞다 
            이 부분은 리스트의 idx 를 통해 k 값으로 접근하면 그에 매칭되는 값을 찾는데 유용하다

    -   이는 "C" 일때도 유용하게 사용된다
        -   k = 2 일때 cmd = "C"
            up[down[k]] = up[k]
            down[up[k]] = donw[k]

            -   up[down[k]] 를 보면 down[k] = 3 이고, up[k] = 1 이다.
                즉 [-1, 0, 1, 2] 에서 [-1, 0, 1, 1] 로 변경한다

            -   down[up[k]] 는 up[k] = 1 이므로 down[1] = 2 이고 down[k] = 3 이다.
                즉 [1, 2, 3, 4] 를 [1, 3, 3, 4] 로 변경한다

                살펴보면 다음과 같다

                up      =   [-1, 0, 1, 1]
                down    =   [ 1, 3, 3, 4]

                이는 [0, 1, 3] 으로 만든것과 같다

            -   끝값에 대해서 처리하는 로직이 필요하다
                k = 3 일때 다음처럼 처리된다

                k = 3 이면 up[k] = 2 이 되고, down[k] = 4 이다 (여기서 4 는 의미 없는 수이다) 
                - 게다가 이대로 적용하면 up[down[k]] 일때, up[4] 가 되므로, out of range 이다   

                이를 해결하기 위해, 양끝에 가상의 공간을 넣는다

                up = [-1, 0, 1, 2, 3, 4]
                down = [1, 2, 3, 4, 5, 6]

                여기서 up 은 -1 과 4 가 가상의 공간이며,
                down 은 1 과 6 이다

                k 는 N - 1 까지의 정수이므로, 0 부터 3 까지 처리된다
                이는 가상의 공간으로 시작 인덱스가 + 1 되었으니, k = k + 1 한 인덱스를 적용한다

                이렇게 하면 k = 4 일때(이는 이전인덱스인 k = 3 과 시작 인덱스 + 1 을 합산한 인덱스이다)
                -   down[k] = 5 이고 up[5] = 4 이므로, out of range 가 아니다

    아무래도 나중에 한번더 살펴볼 문제인듯 싶다.
    구현 코드는 solution.py 에 있다

"""

def execute_cmd(n: int, k: 0, cmd: str):
    #   삭제된 행의 인덱스를 저장하는 리스트
    deleted = []

    #   링크드 리스트에서 각 행 위아래의 행 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    #   현재 위치를 나타내는 인덱스
    k += 1

    #   주어진 명령어 리스트를 하나씩 처리
    for cmd_i in cmd:
        if cmd_i.startswith('C'):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            action, num = cmd_i.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):   
                    k = down[k]

        print(up, down)

execute_cmd(4, 2, ['C', 'U 2', 'C'])

def solution(n, k, cmd):
    currnet_idx = k
    table_list = ["O"] * n
    undo_list = []

    for command in cmd:
        currnet_idx, table_list, undo_list = execute_cmd(n, command, currnet_idx, table_list, undo_list)

    return "".join(table_list)


