def get_total(answers, student):
    """학생이 맞춤 총 점수

    Args:
        answers (list): 문제 정답 리스트
        student (list): 학생의 찍는 방식 리스트

    Returns:
        int: 맞춘 문제의 수 
    """
    total = 0
    #   answers 수
    answers_len = len(answers)

    #   찍는 학생 수
    pick_len = len(student)


    for i in range(answers_len):
        if answers[i] == student[i % pick_len]:
            total += 1

    return total

def get_top_score(total_nums):
    """최고 점수 학생 리스트를 얻는 함수

    Args:
        total_nums (list): 문제를 맞춘 총 점수 리스트

    Returns:
        list: 최고 점수 학생 리스트
    """
    top_score = []

    total_nums.sort(reverse=True)

    max = total_nums[0]

    # max = max(total_nums)

    for idx in range(len(total_nums)):
        if total_nums[idx] == max:
            top_score.append(idx + 1)

    return sorted(top_score);


def solution(answers):
    total_nums = []

    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    #   O(N^2)
    for student in students:
        total = get_total(answers, student)
        total_nums.append(total)
        
    #   O(N)
    return get_top_score(total_nums)
