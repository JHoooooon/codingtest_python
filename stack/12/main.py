"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

*   제한사항

prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

*   입출력의 예

prices	            return
[1, 2, 3, 2, 3]	    [4, 3, 1, 1, 0]

"""

#   O(N^2)
# def solution(s):
#     result = []
#     s_len = len(s)

#     for i in range(s_len):
#         if s[i] == 1:
#             result.append(s_len - 1)
#             continue

#         if i == s_len - 1:
#             result.append(0)
#             continue

#         for j in range(i + 1, s_len):
#             if s[j] < s[i]:
#                 result.append(j - i)
#                 break;
#             elif j == s_len - 1:
#                 result.append(s_len - 1 - i)
        
#     return result


def solution(s):
    s_len = len(s)
    result = [0] * s_len
    #   [0, 0, 0, 0, 0, 0, 0]
    #   [0, 0, 1, 0, 0, 0, 0]
    #   [0, 2, 1, 0, 0, 0, 0]
    #   [0, 2, 1, 0, 0, 0, 0]
    #   --
    #   [0, 2, 1, 1, 0, 0, 0]
    #   --
    #   [0, 2, 1, 1, 1, 0, 0]
    #   --
    #   [0, 2, 1, 1, 1, 1, 0]

    stack = [0]
    #   [0, 1]
    #   [0, 1, 2,]
    #   ---
    #   [0, 3]
    #   --
    #   [0, 4]
    #   --
    #   [0, 5]
    #   [0, 5, 6]
    #   --

    for i in range(1, s_len):
        while stack and s[i] < s[stack[-1]]:
            j = stack.pop()
            result[j] = i - j

        stack.append(i)
    while stack:
        j = stack.pop()
        result[j] = s_len - 1 - j

    return result