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
            -   current_idx 의 위치가 "X" 라면 그다음 idx 를 할당
        -   "Z" 명령시 undo_list 를 pop
            -   pop 된 index 값을 "O" 로 변경   
            -   current_idx 값은 변경되지 않음
        -   "U X" 명령시 current_idx -= X
            -   current_idx 가 0 보다 작다면 current_idx = 0
        -   "D X" 명령시 current_dix += X
            -   current_idx 가 n - 1 보다 크다면 current_idx = n - 1

-   변경된 table_list 반환
"""

def execute_cmd(n: int, cmd: str, current_idx: int, table_list: str, undo_list: list):
    undo_lst = undo_list.copy()
    table_lst = table_list
    crt_idx = current_idx
    cmd = cmd.split()

    if cmd[0] == "U":
        num = int(cmd[1])
        crt_idx -= num
        if crt_idx < 0:
            crt_idx = 0
    elif cmd[0] == "D":
        num = int(cmd[1])
        crt_idx += num
        if crt_idx > n - 1:
            crt_idx = n - 1
    elif cmd[0] == "C":
        undo_lst.append(crt_idx)
        if crt_idx == n - 1:
            crt_idx -= 1
        else:
            crt_idx += 1
    elif cmd[0] == "Z":
        if undo_list:
            undo = undo_lst.pop()

    return crt_idx, table_lst, undo_lst

# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# idx = k
# table_list = ["O"] * n
# undo_list = []

# idx, table_list, undo_list = execute_cmd(n, "D 2", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "U 3", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "D 4", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "U 2", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "Z", idx, table_list, undo_list)
# print(idx, table_list, undo_list)
# idx, table_list, undo_list = execute_cmd(n, "Z", idx, table_list, undo_list)
# print(idx, table_list, undo_list)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
idx = k
table_list = ["O"] * n
undo_list = []

idx, table_list, undo_list = execute_cmd(n, "D 2", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "U 3", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "D 4", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "U 2", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "Z", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "Z", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "U 1", idx, table_list, undo_list)
print(idx, table_list, undo_list)
idx, table_list, undo_list = execute_cmd(n, "C", idx, table_list, undo_list)
print(idx, table_list, undo_list)


def solution(n, k, cmd):
    currnet_idx = k
    table_list = ["O"] * n
    undo_list = []

    for command in cmd:
        currnet_idx, table_list, undo_list = execute_cmd(n, command, currnet_idx, table_list, undo_list)

    return "".join(table_list)


