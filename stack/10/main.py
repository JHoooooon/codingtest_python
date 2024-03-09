"""
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

*   제한사항

s의 길이는 1 이상 1,000 이하입니다.
"""

def solution(s):
    s_len = len(s)
    answer = 0

    if s_len % 2 != 0:
        return 0

    for i in range(s_len):
        dup_s = s[i + 1:] + s[:i + 1]
        print(dup_s)
        stack = []

        for j in dup_s:
            if j == '(' or j == '[' or j == '{':
                stack.append(j)

            #   수정사항
            #   elif stack != []:
            elif stack:
                #   수정사항
                #   char = stack[len(stack)- 1]
                char = stack[-1]
                #   수정사항
                # if char + j == '()' or char + j == '[]' or char + j == '{}':
                if ((char == '(' and j == ')') or 
                    (char == '[' and j == ']')or 
                    (char == '{' and j == '}')):
                        stack.pop()
        #   수정사항
        if stack == []:
        # if not stack :
            answer += 1
        
    return answer