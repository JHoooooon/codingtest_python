"""
*   책의 솔루션

-   O(N) 이라고 한다
    N 은 discount 의 길이이며, 주어진 want 리스트에 기반하여 10 일동안 할인상품이
    원하는 제품과 일치하는지 확인하므로, 시간복잡도가 O(N) 이라 한다

-   discount 의 길이는 N 번 순회 == O(N)
-   내부 for 문은 10 번만 순회하니 O(10) == O(1)
-   이후 discount_10d == want_dict 는 10 개로 고정된 dict 를 순회하니 O(10) == O(1)
-   O(N) * O(1) * O(1) = O(N)
""" 

def solution(want, number, discount):
    answer = 0
    want_dict = {}

    for idx in range(len(want)):
        want_dict[want[idx]] = number[idx]

    # 여기서 관과한것이 있다
    # 특정일 기준으로 원하는 제품과 수량이 일치할 경우이다
    # 그러므로
    # discount_len - 9 를 하여 10 이 되지 않는 기간을 빼고 처리해야 한다
    # 10일간 쇼핑을 할수 있어야 하기 때문이다
    #
    #   이는 discount 의 len 값에 따라 O(N) 이다
    for i in range(len(discount) - 9):
        discount_10d = {}

        #   이는 10 를 순회하니 O(10) 으로 O(1) 로 계산된다
        for j in range(i, i + 10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1

        if discount_10d == want_dict: 
            answer += 1

    return answer


solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
)