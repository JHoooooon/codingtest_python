"""
*  문자열 해싱을 이용한 검색 함수 만들기

문자열 리스트 string_list 와 쿼리 리스트 query_list 가 있을때 각 쿼리 리스트에 있는 문자열이
string_list 의 문자열 리스트에 있는지 여부를 확인해야 한다

문자열이 있으면 True, 없으면 False 가 된다

각 문자열에 대해서 문자열의 존재 여부를 리스트 형태로 변환하는 solution() 함수를 작성하라

*   제약조건

-   입력 문자열은 영어 소문자만 이루어져 있다
-   문자열의 최대 길이는 10^6 이다
-   해시 충돌은 없다
-   아래와 같은 문자열 해싱 방법을 활용해서 해싱 함수를 구현하라
-   다음식에서 p 는 31, m 은 1,000,000,007 로 한다
    -   hash(s) = (s[0] + s[1] * p + s[2] * p^2 .... + s[n - 1] * p^n - 1) mod m

*   입출력

string_list                               query_list                                             return
['apple', 'banana', 'cherry']             ['banana', 'kiwi', 'melon', 'apple']                   [True, False, False, True]

*   문제이해

-   query_list 의 문자열이 string_list 에 들어가 있으면 True 아니면 False 로 이루어진 배열을 반환
-   Hash 로 찾아서 처리해야함
    -   hash(s) = (s[0] + s[1] * p + s[2] * p^2 .... + s[n - 1] * p^n - 1) mod m
    -   구해진 hash 를 index 로 해서 저장
-   query_list 의 문자열에서, hash 값을 찾아서 있으면 True, 없으면 False

1.  hash 함수를 만든다
2.  hash 객체를 만든다
3.  answer 객체를 만든다 <- boolean 값을 저장하는 배열
4.  string_list 를 순회하여 hash 함수로 만든 key 를 hash 객체의 key 로, 값은 value 로 넣는다
5.  query_list 를 순회하여 hash 함수로 만든 key 가 hash 객체의 key 에 있다면 True, 아니면 False 를 answer 배열에 넣는다
6.  answer 객체를 반환

*   책에서는 위의 hash 방법대로 하지 않는다...


    -   for i in range(s_len):
            idx += (ord(s[i]) * p**i)
    
    -   hash(s) = (s[0] + s[1] * p + s[2] * p^2 .... + s[n - 1] * p^n - 1) mod m

    와 같을텐데...
    책에서는

    -   for i in range(s_len):
            idx = (idx * p + ord(s[i])) % m
    
    으로 한다.
    해싱 위의 공식으로 하라고 했으면서 다른 방식으로 구현한것 같다..
"""

def hash(s: str):
    s_len = len(s)
    p = 31
    m = 1000000007
    idx = 0

    for i in range(s_len):
        idx += (ord(s[i]) * p**i)
    
    return idx % m 

print(
    hash('apple')
)

def solution(string_list, query_list):
    answer = []
    hash_obj = {}

    for s in string_list:
        idx = hash(s)
        hash_obj[idx] = s

    for s in query_list:
        idx = hash(s)
        if hash_obj.get(idx):
            answer.append(True)
        else:
            answer.append(False)

    return answer

solution(
    ['apple', 'banana', 'cherry'],
    ['banana', 'kiwi', 'melon', 'apple'],
)