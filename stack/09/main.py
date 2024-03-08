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

    while(decimal != 0):
        binary = decimal % 2
        decimal = decimal // 2
        stack.append(str(binary))

    bin = ''

    while(stack):
        bin += stack.pop()

    return int(bin)