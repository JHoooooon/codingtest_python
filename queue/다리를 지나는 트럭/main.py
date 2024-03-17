"""
*   다리를 지나는 트럭

트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

*   제한 조건

-   bridge_length는 1 이상 10,000 이하입니다.
-   weight는 1 이상 10,000 이하입니다.
-   truck_weights의 길이는 1 이상 10,000 이하입니다.
-   모든 트럭의 무게는 1 이상 weight 이하입니다.

*   문제 풀이

------- 잘못이해 -----------------

-   위의 예시같은 경우 
    (bridge_lenght = 2, weight = 10, truck_weight=[7, 4, 5, 6]) 이다 

-   현재 생각한 계산이 맞다면,

    -   2, 10 [7, 4, 5, 6]  이면
        -   [7, [4, 5], 6] 이고,
        -   1 + (1 + 1 + 2) + 1 + 2 = 8
    -   100, 100, [10,10,10,10,10,10,10,10,10,10] 이면
        -   [10,10,10,10,10,10,10,10,10,10]
        -   (100 + (1 * 10)) = 110
    -   100, 100, [10] 이면
        -   [10]
        -   (100 + 1) = 101

------- 잘못이해 -----------------

진짜, 이거 설명이 이상해서 여태까지 이부분때문에 고생했다...
문제가 이해가 안가니 풀수가 없는 문제이다

이책 다읽고 백준으로 옮기든지 해야 겠다! ㅡㅡ 

뭔가 len 값을 추출하고 처리하면 될것 같았는데, 잘 되지 않았다
queue 자료구조로 다음과 같이 처리해본다

0        _          _        [7, 4, 5, 6]   
1        _          7        [4, 5, 6]   
2        _          7        [4, 5, 6]   
3        7          4        [5, 6]   
4        7          4,5      [6]   
5        7,4        5        [6]   
6        7,4,5      6        []   
7        7,4,5      6        []   
8        7,4,5,6    _        []

여기서 중요한점은 트럭의 길이는 1 이고, 다리의 길이만큼 이동해야 한다는것이다
위의 예시에서 7 은 1초구간에서 다리에 진입하고, 3 초 구간에서 목적지로 넘어간다

1초 구간에서 목적지 길이만큼 + 2 한 3초가 걸린것이다

다음의 테스트 코드를 분석해본다

5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]

0        _                          _                 [2, 2, 2, 2, 1, 1, 1, 1, 1]   
1        _                          2                 [2, 2, 2, 1, 1, 1, 1, 1]   
2        _                          2, 2              [2, 2, 1, 1, 1, 1, 1]   
3        _                          2, 2              [2, 2, 1, 1, 1, 1, 1]   
4        _                          2, 2              [2, 2, 1, 1, 1, 1, 1]   
5        2                          2                 [2, 2, 1, 1, 1, 1, 1]   
6        2, 2                       2                 [2, 1, 1, 1, 1, 1]   
7        2, 2                       2, 2              [1, 1, 1, 1, 1]   
8        2, 2                       2, 2, 1           [1, 1, 1, 1]   
9        2, 2                       2, 2, 1           [1, 1, 1, 1]   
10       2, 2, 2                    2, 1              [1, 1, 1, 1]   
11       2, 2, 2, 2                 1                 [1, 1, 1, 1]   
12       2, 2, 2, 2, 1              1                 [1, 1, 1]   
13       2, 2, 2, 2, 1              1, 1              [1, 1]   
14       2, 2, 2, 2, 1              1, 1, 1           [1]   
15       2, 2, 2, 2, 1              1, 1, 1, 1        []   
16       2, 2, 2, 2, 1, 1           1, 1, 1           []   
17       2, 2, 2, 2, 1, 1, 1        1, 1              []   
18       2, 2, 2, 2, 1, 1, 1, 1     1                 []   
19       2, 2, 2, 2, 1, 1, 1, 1, 1                    []   

이역시 5 단위로 목적지에 도착하는것을 볼 수 있다

-   bridge_length 단위마다, 목적지 도착되어야 한다
-   시작은 1 초 부터 해당하는 truck 이 다리위에 들어간다
-   이 두부분을 추가적으로 고친다

"""
#   첫번째 실패
# def get_pending_trucks(bridge_length, truck_weights, weight):
#     pendings = []
#     pending = []
#     total_weight = 0

#     while len(truck_weights) > 0:
#         truck = truck_weights.pop(0)
#         total_weight += truck

#         if len(pending) == bridge_length or total_weight > weight:
#             truck_weights.insert(0, truck)
#             pendings.append(pending)
#             pending = []
#             total_weight = 0
#         else:
#             pending.append(truck)

#     pendings.append(pending)
#     return pendings

# def solution(bridge_length, weight, truck_weights):
#     times = 0
#     pendings = get_pending_trucks(bridge_length, truck_weights, weight)

#     if len(pendings) == 1:
#         times += bridge_length + len(pendings[0])
#     else:
#         for pending in pendings:
#             pending_len = len(pending)
#             if pending_len > 1:
#                 times += (bridge_length + (pending_len))
#             else:
#                 times += bridge_length

#     return times

#   두번째 실패

# def to_pending(bridge_length, weight, truck_weights):
#     max_weight = 0
#     pendings = []
#     pending = []

#     if len(truck_weights) == 1:
#         return [truck_weights]

#     while len(truck_weights) > 0:
#         truck = truck_weights.pop(0)
#         max_weight += truck

#         if len(pending) <= bridge_length and max_weight <= weight:
#             pending.insert(0, truck)
#         else:
#             truck_weights.insert(0, truck)
#             pendings.append(pending)
#             max_weight = 0
#             pending = []
    
#     pendings.append(pending)
#     return pendings

# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     pendings = to_pending(bridge_length, weight, truck_weights)
#     pendings_len = len(pendings)

#     for idx in range(pendings_len):
#         pending_len = len(pendings[idx])

#         if pendings_len == 1 and pending_len == 1:
#             time  = bridge_length + 1
#             break;
#         elif pendings_len == 1 and pending_len > 1:
#             time  = bridge_length + pending_len
#             break;
#         else:
#             if pending_len == 1 and idx != pendings_len - 1:
#                 time = bridge_length + 1
#             elif idx == pendings_len - 1:
#                 time += pending_len
#             else:
#                 time += (pending_len + (bridge_length - pending_len) + pending_len)
#     return time

def solution(bridge_length, weight, truck_weight):
    max_weight = 0
    times = 0 
    truck_weight_len = len(truck_weight)

    while len(truck_weight) > 0:
        if truck_weight_len == 1:
            return bridge_length + 1

        if truck_weight:
            truck = truck_weight.pop(0)
            max_weight += truck

            if max_weight < weight:
                times += 1
            else:
                if max_weight > weight:
                    truck_weight.insert(truck, 0)
                #   bridge 길이만큼 이동
                times += (bridge_length - times) + times
                max_weight = 0
                # time = 0
    # times += bridge_length
    print(times)

    return times

print(solution(
    # 100, 100, [10,10,10,10,10,10,10,10,10,10],
    # 100, 100, [10]
    2, 10, [7,4,5,6]
    # 5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]
    # 7, 7, [1, 1, 1, 1, 1, 3, 3]
    # 1, 1, [1, 1, 1]
))

