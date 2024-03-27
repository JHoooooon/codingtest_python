"""
🤯 직접 풀지 못한 문제 🤯

-   결국 답안을 보고 이해한후 풀게 된 문제..
-   알아야할 문제점
    -   Combinations 를 통한 각 원소의 조합
    -   Counter 를 사용하여 각 개수를 출력   
    -   max 값을 사용하여 Counter.values 중 가장 큰값을 가져와 비교
        -   계속적으로 while 문을 사용하여 max 값을 추출하려고 하는 습관이있다..
    -   순열, 조합 관련된 알고리즘을 익혀야 한다.

*   메뉴 리뉴얼

레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

손님 번호	주문한 단품메뉴 조합
1번 손님	A, B, C, F, G
2번 손님	A, C
3번 손님	C, D, E
4번 손님	A, C, D, E
5번 손님	B, C, F, G
6번 손님	A, C, D, E, H

가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

코스 종류	메뉴 구성	설명
요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

[문제]
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]

-   orders 배열의 크기는 2 이상 20 이하입니다.

-   orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
    -   각 문자열은 알파벳 대문자로만 이루어져 있습니다.
    -   각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.

-   course 배열의 크기는 1 이상 10 이하입니다.
    -   course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
    -   course 배열에는 같은 값이 중복해서 들어있지 않습니다.

-   정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
    -   배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
    -   만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
    -   orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

*   입출력

orders	                                            course	    result

["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	    [2,3,4]	    ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	    ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                            [2,3,4]	    ["WX", "XY"]

*   문제 이해
-   Point

    "이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다."

-   course 의 배열의 원소의 개수 만큼 원하는 주문중 가장 큰 주문의 집합을 반환
    -   만약 가장큰 주문의 집합이 여러개면 가장큰 모든 주문의 집함을 추가

-   course 가 [2, 3, 4] 이면 orders 에 주문된 주문건중 
    -   2개 메뉴중 가장 많이 주문한 메뉴 
    -   3개 메뉴중 가장 많이 주문한 메뉴
    -   4개 매뉴중 가장 많이 주문한 메뉴
    -   각 orders 마다 2개, 3개, 4개에대한 모든 경우의 수의 메뉴들을 조합하여 개수 처리 
    -   계수로 처리된 각 메뉴의 경우의수중 가장 많이 주문된 메뉴들을 가져와 배열에 담는다
    -   단 중복없음

*   코드정리

-   현재 내가 풀지 못한 문제이다
-   막혔던점.

-   각 원소값을 합성(Combination)하여 나올수있는 경우의 수를 저장한후, 합성된 개수를 세어 개수가 가장 높은값을 반환해야 한다 
    하지만 Combination 하는 과정에서 제대로 코드가 작성되지 않았다
    - 생각해 낸 것이 삼중 For 문으로 되더라..   

-   Combinations 함수를 제공하는데, 어떻게 구현되었을지 찾아보니, 재귀로 많이 사용하더라
-   확인해보니 결과값은 같다

    def combination(order, count):
        #1
        arr = sorted(order)
        result = []
        
        #2
        if count == 1:
            return arr

        for idx in range(len(arr)):
            #3
            value = arr[idx]

            #4
            rest = arr[idx + 1:]

            #5
            combination_arr = combination(rest, count - 1)

            #6
            for i in combination_arr:
                result.append(( value, *i ))

        return result

-   Combination 함수의 구현 코드를보면, 

1.  arr 를 받아 정렬한다
    -   sorted 를 사용하는데, 문자열도 배열로 만드는 좋은 효과가 있다

2.  count 값이 1 과 같으면, arr 를 반환한다
    -   기준이 될 값을 제외한 나머지를 이어 붙이므로, count 가 2 라면, count - 1 한 값인 1을 하나의 set 으로 만들어야 한다
        그러므로, 1 은 항상 남아야 하는 값이다

3.  value 값은 기준이 될 값이다.

4.  rest 값은 기준값을 제외한 나머지 배열이다

5.  combination 을 호출하여, 재귀 함수로써 작동시킨다
    -   2 번에서 count 값을 판별하여, 재귀 함수의 동작의 brakepoint 역할을 해준다
    -   그러므로, 재귀가 깊어질수록 count 값을 -1 해주어야 한다

6.  combination_arr 를 순회하여, 기준되는 값인 value 와, combination_arr 의 각 원소를 합친 튜플을 반환한다
    -   combination_arr 의 item 이 배열이라면, 재귀 함수가 깊어질수록, 중첩배열형태로 반환된다
        이러한 부분을 처리하기 위해 spread 문법과 같은 기능을 하는 * 을 사용하여 배열을 spread 시킨다
    -   처리된 결과 배열을 result.append 로 추가한다

7.  result 를 반환한다

-   여기서 중요한 부분중 하나는 tuple 로 처리하여 반환한다는것이다
    이는 counter 를 사용하여, 개수를 센 객체를 반환할때 배열은 key 값으로 사용되지
    못한다
    대신 tuple 을 사용가능하므로, 이러한 점을 고려해서 tuple 로 변환한후 반환한다
"""

# from collections import Counter
# from itertools import combinations;

def combination(order, count):
    arr = sorted(order)
    result = []
    
    if count == 1:
        return arr

    for idx in range(len(arr)):
        value = arr[idx]
        rest = arr[idx + 1:]

        combination_arr = combination(rest, count - 1)

        for i in combination_arr:
            result.append(( value, *i ))

    return result

def counter_func(manus):
    result = {}

    for manu in manus:
        if manu in result:
            result[manu] += 1
        else:
            result[manu] = 1

    return result

def solution(orders, course):
    answer = []

    for count in course:
        manu = []
        for order in orders:
            manu += combination(order, count)

        counter = counter_func(manu)
        print(counter)

        if (
            len(counter) != 0 and max(counter.values()) != 1
        ):
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))

    return sorted(answer)
    
solution(
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    [2,3,4],	
#     ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
#     [2,3,5]	    
)



