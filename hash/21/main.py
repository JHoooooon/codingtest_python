"""
*   할인 행사

XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다. XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며, XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인 경우에 대해 알아봅시다. 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다. 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다. 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.

정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

*   제한사항

-   1 ≤ want의 길이 = number의 길이 ≤ 10
        1 ≤ number의 원소 ≤ 10
        number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.

-   10 ≤ discount의 길이 ≤ 100,000

-   want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
        1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12

*   입출력 예

want	                                   number	        discount	                                                                                                                result

["banana", "apple", "rice", "pork", "pot"] [3, 2, 2, 2, 1]	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	3

["apple"]	                               [10]	            ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]                            0

*   문제 풀이

1.  want 와 number 를 함쳐 want_count 객체를 만든다

2.  discount_list 를 선언

3.  discount 를 순회하여 의 idx + idx + 10 까지 자른다 
    -   만약 자른 값의 길이가 want 길이보다 작으면 break 
    -   자른 배열을 계수정렬한다
    -   계수정렬된 객체는 discount_list 에 append 

4.  discount_list 를 순회하여, want_count 의 값과 같은지 확인 
    -   want_count 의 key 값이 필요하므로 필연적으로 want 값을 내부에서 순회한다
    -   같다면, answer += 1

5.  answer 반환

-   O(N^2) 으로 discount 순회가 100,000 번이라면, 
    최악이 100,000,000,000 + 100,000,000,000 이 되므로 적합하지 않다

-   다시 생각해보자

want_count 객체는 다음과 같다

{ 'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1 }

discount_list 는 다음과 같다

[
    {'chicken': 1, 'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2}, 
    {'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2, 'pot': 1}, 
    {'apple': 2, 'banana': 3, 'rice': 2, 'pork': 2, 'pot': 1}, 
    {'banana': 3, 'rice': 2, 'apple': 2, 'pork': 2, 'pot': 1}, 
    {'rice': 2, 'apple': 2, 'pork': 2, 'banana': 3, 'pot': 1}, 
    {'apple': 2, 'pork': 2, 'banana': 3, 'rice': 1, 'pot': 1}, 
    {'pork': 2, 'banana': 3, 'rice': 1, 'pot': 1, 'apple': 1}, 
    {'banana': 3, 'pork': 1, 'rice': 1, 'pot': 1, 'apple': 1}, 
    {'pork': 1, 'rice': 1, 'pot': 1, 'banana': 2, 'apple': 1}, 
    {'rice': 1, 'pot': 1, 'banana': 2, 'apple': 1}
]

discount_list 에서 want_count 를 모두 가진 idx 는 2, 3, 4 이므로 result 는 3 이다
지금 현재 discount_list 는 모든 값을 가진다.

여기서 조금더 생각해보면, discount_list 의 계수객체들을, want 값에 맞추어 처리가능하다

[
    {'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2}, 
    {'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2, 'pot': 1}, 
    {'apple': 2, 'banana': 3, 'rice': 2, 'pork': 2, 'pot': 1}, 
    {'banana': 3, 'rice': 2, 'apple': 2, 'pork': 2, 'pot': 1}, 
    {'rice': 2, 'apple': 2, 'pork': 2, 'banana': 3, 'pot': 1}, 
    {'apple': 2, 'pork': 2, 'banana': 3, 'rice': 1, 'pot': 1}, 
    {'pork': 2, 'banana': 3, 'rice': 1, 'pot': 1, 'apple': 1}, 
    {'banana': 3, 'pork': 1, 'rice': 1, 'pot': 1, 'apple': 1}, 
    {'pork': 1, 'rice': 1, 'pot': 1, 'banana': 2, 'apple': 1}, 
    {'rice': 1, 'pot': 1, 'banana': 2, 'apple': 1}
]     

python 은 javascript 의 객체와는 다르게, dict 끼리의 비교시 원소의 값이 같으면 True 를 반환한다
이는 내부적으로 얕은비교를 하는듯하다.

-   discount 의 길이는 N 번 순회 == O(N)
-   discount_list 는 N 번 순회 == O(N)
-   이후 discount == want_count 는 10 개로 고정된 dict 를 순회하니 O(10) == O(1)

-   O(N) + O(N) * O(1) = O(N)
"""

def solution(want, number, discount):
    answer = 0
    discount_len = len(discount)
    want_len = len(want)
    want_count = {}
    discount_list = []

    for idx in range(want_len):
        want_count[want[idx]] = number[idx]

    # 여기서 관과한것이 있다
    # 특정일 기준으로 원하는 제품과 수량이 일치할 경우이다
    # 그러므로
    # discount_len - 9 를 하여 10 이 되지 않는 기간을 빼고 처리해야 한다
    # 10일간 쇼핑을 할수 있어야 하기 때문이다
    #
    for idx in range(discount_len):
        discount_count ={}
        list = discount[idx:idx + 10]

        if len(list) >= want_len:
            for item in list:
                if item in want:
                    if item in discount_count:
                        discount_count[item] += 1
                    else:
                        discount_count[item] = 1
                else:
                    continue
        else:
                break

        discount_list.append(discount_count)

    for discount in discount_list:
        if discount == want_count:
            answer += 1

    return answer

solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
)