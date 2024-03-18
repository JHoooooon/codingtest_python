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

*   이해

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

0    []                         []                    [2, 2, 2, 2, 1, 1, 1, 1, 1]
1    []                         [2]                   [2, 2, 2, 1, 1, 1, 1, 1]
2    []                         [2, 2]                [2, 2, 1, 1, 1, 1, 1]
2    []                         [2, 2]                [2, 2, 1, 1, 1, 1, 1]
3    []                         [2, 2]                [2, 2, 1, 1, 1, 1, 1]
4    []                         [2, 2]                [2, 2, 1, 1, 1, 1, 1]
5    []                         [2, 2]                [2, 2, 1, 1, 1, 1, 1]
6    [2]                        [2, 2]                [2, 1, 1, 1, 1, 1]
7    [2, 2]                     [2, 2]                [1, 1, 1, 1, 1]
8    [2, 2]                     [2, 2, 1]             [1, 1, 1, 1]
9    [2, 2]                     [2, 2, 1]             [1, 1, 1, 1]
10   [2, 2]                     [2, 2, 1]             [1, 1, 1, 1]
11   [2, 2, 2]                  [2, 1, 1]             [1, 1, 1]
12   [2, 2, 2, 2]               [1, 1]                [1, 1, 1]
13   [2, 2, 2, 2]               [1, 1, 1]             [1, 1]
14   [2, 2, 2, 2]               [1, 1, 1, 1]          [1]
15   [2, 2, 2, 2]               [1, 1, 1, 1, 1]       []
16   [2, 2, 2, 2, 1]            [1, 1, 1, 1]          []
17   [2, 2, 2, 2, 1, 1]         [1, 1]                []
18   [2, 2, 2, 2, 1, 1, 1]      [1]                   []
19   [2, 2, 2, 2, 1, 1, 1 , 1]  []                    []

1.  시간단위는 하나의 단위유닛이다 
2.  트럭 1대는 bridge_length 가 5 일때, 한번 이동하는데 걸리는 시간단위는 1 이다
3.  트럭이 진입할때, 1초 이며, 다리를 건너는데 걸리는 시간은 bridge_length 이다
4.  처음 삽입된 이후 1 ~ 5 초이후 6초가 되어야 목적지에 도착한다
5.  그다음 삽입된 이후 2 ~ 6 초 이후 7 초가 되어야 목적지에 도착한다
    and so on...

*   문제 풀이

-   문제가 완벽히 이해되었다 풀어보자!!

-   time 변수 선언
    -   초기값 0

-   truck_length 값을 합산할 total 을 선언
    -   초기값 0

-   bridge_length 길이를 가진 pendings 배열을 선언
    bridge_length = 5
    ['X', 'X', 'X', 'X', 'X']

-   truck_lengths 를 순회
    -   time 값에 1 을 합산
    -   truck_length 값 첫번째 값을 pop 한다
    -   pop 한 truck_length 값을 total 값에 합산한다  

-   pendings 배열의 첫번째 원소가 'X' 가 아니면,
    -   total 값에서 pop 한 원소의 값을 빼주어야 다음 insert 될 원소를 추가할수 있다
        -   pendings 에서 첫번째 원소 pop
        -   total - pop 한 첫번째 원소

-   total 이 width 보다 작거나 같으면,
    -   대기열에 해당 원소를 푸시해주어야 한다
        -   pendings 배열의 첫번째 원소를 pop
        -   해당 truck_length 값을 push
-   그렇지 않으면,
    -   pendings 배열의 첫번째 원소를 pop
    -   'X' 를 push
    -   truck_weights 에 0 번째 원소에 truck 을 다시 insert

-   순회완료되면 남은 pendings 배열의 개수를 time 에 더한다
    -   truck_weights 값이 0 이 될때까지 순회하므로,
        순회완료되면 마지막 집합은 pendings 배열에 들어가 있다
        그러므로 pendings 배열의 길이값을 time 에 더하면 원하는 값이
        나온다

-   time 반환

"""

def solution(bridge_length, weight, truck_weights):
    time = 0
    total = 0
    pendings = ['X' for _ in range(bridge_length)]

    while(len(truck_weights) > 0):
        time += 1
        truck = truck_weights.pop(0)
        total += truck

        poped_pending = pendings.pop(0)

        if poped_pending != 'X':
            total -= poped_pending

        if total <= weight:
            pendings.append(truck)
        else:
            total -= truck
            truck_weights.insert(0, truck)
            pendings.append('X')

    time += len(pendings)

    return time

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
