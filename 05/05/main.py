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

def solution(N, stages):
    stage_counts = [0] * (1 + N + 1)
    pre_count = 0
    fail_rates = {}
    stages_len = len(stages)

    for stage in stages:
        stage_counts[stage] += 1

    for current_stage in range(1, N + 1):

        if stage_counts[current_stage] == 0:
            fail_rates[current_stage] = 0
        else:
            fail_rates[current_stage] = stage_counts[current_stage] / (stages_len - pre_count)
            pre_count += stage_counts[current_stage]

    answer = sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)
    
    return answer
