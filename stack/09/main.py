"""
소괄호는 짝을 맞출 열린 괄호 '(' 와 닫힌괄호 ')' 로 구성된다
문제는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 준다

이때 소괄호가 정상적으로 열고 닫혔는지 판별하는 solution() 함수를 구현하라

만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False 를 반환하라

*   제약조건
    -   열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄된다
    -   상쇄 조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 한다
    -   더 상쇄할 필요가 없을 때 까지 상쇄를 반복한다

"""

def solution(decimal: int):
    stack = []

    #   O(logN)
    #
    #   N 이 0 이 될때까지 2 로 나누므로,
    #   logN 이다
    while(decimal != 0):
        #   2 로 나눈 나머지
        binary = decimal % 2
        #   2 로 나눈값을 decimal 에 할당
        decimal = decimal // 2
        #   stack 에 문자열로 만들어 push
        #   int 는 str 과 concatation 이 안된다
        stack.append(str(binary))

    #   만들어질 bin 문자열
    bin = ''

    #   stack 이 비면, False
    #   bin += stack.pop() 할때마다 객체가 생성된다고 한다
    #   객체 생성에 의해 O((logN)^2) 라고 하는데,
    #   while 문을 반복하므로 O(N) 이다
    #   O(logN) * O(N) = O(logN^2) 가 된다고 보면 된다
    #
    while(stack):
        #   stack 을 pop 하여 bin 에 합친다
        #   만들어진 배열상의 순서가 꺼꾸로 합쳐진다
        bin += stack.pop()

    #   이진수 반환
    return int(bin)

