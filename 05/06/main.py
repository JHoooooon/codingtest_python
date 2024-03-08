"""
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

*   입출력

dirs	        answer
"ULURRDLLU"	    7
"LULLLLLLU"	    7

*    코드 풀이 <실패>

-   같은 길을 갔는지 확인하는 방법
    1.  각 글자가 5 를 넘어서는 안된다

    2.  각 글자의 인덱스를 매핑한다
        -   예를 들어 "ULURRDLLU" 라고 가정한다
        -   { "U": [0, 2, 8], "L": [1, 6, 7], "D": [5], "R": [3, 4]}

    3.  각 글자가 나타내는 인덱스까지 자르고, 각 글자를 순회하여, 해당 글자의 반대되는 방향과 값이 일치하는지 확인 
        -   예를 들어 "ULURRDLLU" 라고 가정한다
            -   만약 글자의 개수가 5 를 넘어간다면 5 를 유지

            -   { "U": [0, 2, 8], "L": [1, 6, 7], "D": [5], "R": [3, 4]}
            -   이중 "U" 를 반복
                1.  U 에 일치하는 첫번째 인덱스는 0 이다
                    -   "U" 까지 자른다
                    -   각 문자의 개수를 센다
                    -   {"U": 1, "L": 0, "D": 0, "R": 0}"
                    -   "U" 와 "D" 의 값이 같은지 확인: False
                    -   "L" 과 "R" 의 값이 같은지 확인: False

                2.  U 에 일치하는 첫번째 인덱스는 2 이다
                    -   "ULU" 까지 자른다
                    -   각 문자의 개수를 센다
                    -   {"U": 2, "L": 1, "D": 0, "R": 0}"
                    -   "U" 와 "D" 의 값이 같은지 확인: False
                    -   "L" 과 "R" 의 값이 같은지 확인: False

                3.  U 에 일치하는 두번째 인덱스는 8 이다
                    -   "ULURRDLLU" 까지 자른다
                    -   {"U": 3, "L": 3, "D": 1, "R": 2}"
                    -   "U" 와 "D" 의 값이 같은지 확인: False
                    -   "L" 과 "R" 의 값이 같은지 확인: False

                4.  U 에 일치하는 두번째 인덱스는 8 이다
                    -   "U" 까지 자른다
                    -   {"U": 1, "L": 0, "D": 0, "R": 0}"
                    -   "U" 와 "D" 의 값이 같은지 확인: False
                    -   "L" 과 "R" 의 값이 같은지 확인: False

            -   { "U": [0, 0, 2, 8], "L": [0, 1, 6, 7], "D": [0, 5], "R": [0, 3, 4]}
            -   이중 "L" 를 반복
            1.  L 에 일치하는 첫번째 인덱스는 1 이다
                -  "LURRDL" 까지 자른다 
                -   {"U": 1, "L": 2, "D": 1, "R": 2}"
                -   "U" 와 "D" 의 값이 같은지 확인: True
                -   "L" 과 "R" 의 값이 같은지 확인: True
                -   각 값의 개수를 합치고, 해당 인덱스 이전의 값을 더한다 
                -   현재 L 의 첫번째 인덱스는 1 이므로 1 을 더하면 이전 문자까지 더하는것이다,
                -   결과는 6 + 1

-   같은길을 간 적이 없다면,
    1.  처음부터 끝까지 각 글자의 개수를 센다    
        -   "LULLLLLLU" 라고 가정
            -   만약 글자의 개수가 5 를 넘어간다면 5 를 유지
            -   {"L": 5, "U": 2, "R": 0, "D": 0}
            -   결과는 7 
        
-   실패원인
    1.  같은길을 잘못 계산
        -   테스트케이스로 UDLRDURL 을 하면 4 가 나와야 하는데 8 이 나온다
            -   이는 한번갔던길을 2번왕복하여, 4 * 2 의 값이 계산된다 

-   코드 재정리

    -  처음부터 좌표값을 저장하면 된다
        -   좌표값 저장으로는 한번갔던길 (LR), (UD) 일때도 고려해서 처리해야 한다
        -   좌표값을 고유해야 하므로, SET 으로 저장한다    
        -   저장된 SET 의 좌표는 한방향이 2개이므로 (LR), (UD) 최종 처음걸어본 길을 구하기 위해
            저장된 길이의 / 2 한 값이어야 한다

"""

# def get_mapping_idx(dirs: str):
#     """ 각 문자열의 인덱스를 매핑시킨 객체를 만드는 함수

#     Args:
#         dirs (str): dirs 문자열

#     Returns:
#         Dict[str, list[int]]: 인덱스를 매핑시킨 객체
#     """
#     mapping_idx = {'L': [], 'R': [], 'D': [], 'U': []}

#     for idx in range(len(dirs)):
#         if mapping_idx.get(dirs[idx]):
#             mapping_idx[dirs[idx]].append(idx)
#         else:
#             mapping_idx[dirs[idx]] = [idx]

#     return mapping_idx;

# def get_initial_location_len(dirs: str, dir: list):
#     """처음 가본 길의 길이를 계산하는 함수

#     Args:
#         dirs (str): dirs 문자열
#         dir (list): 매핑 시킨 객체에서 해당 원소의 리스트

#     Returns:
#         int: 길이
#     """

#     result = 0

#     for idx in range(len(dir)):
#         target_dirs = []
#         if idx + 1 < len(dir) :
#             target_dirs = dirs[dir[idx]:dir[idx + 1] + 1]
#         else:
#             target_dirs = dirs[dir[idx]:dir[idx]]

#         mapping_dirs = {"U": 0, "D": 0, "L": 0, "R": 0}

#         if len(target_dirs) == 1:
#             continue;
#         else:
#             for char in target_dirs:
#                 mapping_dirs[char] += 1

#             if  (
#                 mapping_dirs['U'] > 0 and
#                 mapping_dirs['D'] > 0 and
#                 mapping_dirs['L'] > 0 and
#                 mapping_dirs['R'] > 0 and
#                 mapping_dirs['U'] == mapping_dirs['D'] and
#                 mapping_dirs['L'] == mapping_dirs['R']):
#                 result = mapping_dirs['U'] + mapping_dirs['D'] + mapping_dirs['L'] + mapping_dirs['R'] + dir[idx]
#                 break;

#     return result

# def get_full_location_len(mapping_idx: dict):
#     """걸어본 전체 길이를 출력하는 함수

#     Args:
#         mapping_idx (dict): idx 를 매핑시킨 딕셔너리

#     Returns:
#         int: 전체 길이
#     """
#     result = 0

#     for char in 'UDLR':
#         char_len = len(mapping_idx[char])

#         if char_len > 5:
#             result += 5
#         else:
#             result += char_len

#     return result

# def solution(dirs):
#     answer = 0
#     mapping_idx = get_mapping_idx(dirs)

#     for char in dirs:
#         location_len = get_initial_location_len(dirs, mapping_idx[char])
#         if location_len > answer:
#             answer = location_len
    
#     if answer == 0:
#         answer = get_full_location_len(mapping_idx)

#     return answer
def is_valid_point(x: int, y: int):
    """
    point 값이 5 혹은 -5가 넘지않은 유효한 포인트로 변환해 주는 함수

    Args:
        point ( int ): 포인트 값
    Return:
        ( int ): 유효한 포인트값
    """
    if -5 <= x <= 5 and -5 <= y <= 5 :
        return True
    return False

def get_points(x: int, y: int, dir: str):
    """이동된 x, y 좌표값을 반환하는 함수

    Args:
        x (int): x 좌표
        y (int): y 좌표
        dir (str): 이동할 방향

    Returns:
        x(int), y(int): 변경된 x,y 좌표
    """
    if dir == 'U':
        y = y + 1
    elif dir == 'D':
        y = y - 1
    elif dir == 'L':
        x = x - 1
    elif dir == 'R':
        x = x + 1
    return x, y

def solution(dirs): 
    #   중복된 좌표값을 없애기 위한 set
    answer = set()
    #   초기화된 x, y 좌표
    x, y = 0, 0

    #   dirs 순회
    for dir in dirs:
        #   이동된 x, y 좌표
        moved_x, moved_y = get_points(x, y, dir)
        if is_valid_point(moved_x, moved_y):
            #   아래의 두 경우는 한번 지나간 경우도 포함하여 저장해야 한다
            #   set 객체에 x, y, moved_x, moved_y 저장
            answer.add((x, y, moved_x, moved_y))
            #   그 반대의 경우인 moved_x, moved_y, x, y 저장
            answer.add((moved_x, moved_y, x, y))

            #   이동된 좌표값을 x, y 에 할당
            x, y = moved_x, moved_y

            sorted(answer, reverse=True)

    #   모든 좌표값에서 2 를 나눈값을 반환
    #   하나의 길은 두가지의 경우의수를 가지므로 나누어줘야 한다
    return len(answer) / 2