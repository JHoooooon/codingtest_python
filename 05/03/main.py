def solution(numbers):
    answer = []

    numbers_len = len(numbers)

    for i in range(numbers_len):
        for j in range(i + 1, numbers_len):
            answer.append(numbers[i] + numbers[j])

    sorted_answer = sorted(list(set(answer)))
    return sorted_answer