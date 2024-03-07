"""
-   실패율: 스테이지에 도달했으나 아직 클리어 하지 못한 플레이어수 / 스테이지에 도달한 플레이어수
-   N: 전체 스테이지의 개수
-   stages: 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열
-   실패율일 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 리턴

*   제한사항

-   N 은 1 ~ 500
-   stages 길이는 1 ~ 200,000
    -   1  이상 N + 1 이하의 자연수
        -   각 자연수는 사용자가 현재 도전 중인 스테이지 번호 
        -   단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어한 사용자를 나타낸다
-   실패율이 같은 스테이지가 있다면 작은 번호와 스테이지가 먼저 오도록 하면 된다
-   스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다

*   입출력

N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]

"""

def get_fail_rate(stages: list, current_stage: int):
    """stage 의 실패율

    Args:
        stages (list): stage 리스트
        stage (int): 실패율을 구할 stage
    Return:
        (float) 실패율
    """

    #   stages 의 길이
    stages_len = len(stages)
    #   해당 stage 에서 도전중인 사용자
    current_count = stages.count(current_stage)

    if current_stage == 1:
        #   스테이지가 1 이면
        #   실패율: 현재 스테이지 카운트 / 스테이지 개수
        return current_count / stages_len 
    else:
        #   실패율: 현재 스테이지 카운트 / 스테이지 개수 - 이전 스테이지 카운트
        return round(current_count / (stages_len - stages.count(current_stage - 1)), 3)

def get_answer(fail_rate):
    """실패율이 높은 스테이지를 내림차순으로 정렬

    Args:
        fail_rate (list): 실패율 리스트
    Return:
        (list): 오름차순으로 정렬된 스테이지 리스트
    """

    # for idx in fail_rate:

def solution(N, stages):
    answer = [0] * N
    pre_count = 0
    fail_rate = {}


    for idx in range(N):
        current_stage = idx + 1
        #   stages 의 길이
        stages_len = len(stages)
        #   해당 stage 에서 도전중인 사용자
        current_count = stages.count(current_stage)
        #   실패율: 현재 스테이지 카운트 / 스테이지 개수 - 이전 스테이지 카운트
        fail_rate[current_stage] = round(current_count / (stages_len - pre_count), 2)
        #   앞전의 stage 카운트와 현재 카운트를 합산
        pre_count += current_count
        
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)
    print(fail_rate)
    print(answer)
    
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])