def solution(n, k, cmd):
    #   삭제된 행의 인덱스를 저장하는 리스트
    deleted = []

    #   링크드 리스트에서 각 행 위아래의 행 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    #   현재 위치를 나타내는 인덱스
    k += 1

    #   주어진 명령어 리스트를 하나씩 처리
    for cmd_i in cmd:
        if cmd_i.startswith('C'):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            action, num = cmd_i.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):   
                    k = down[k]

        print(up, down)

    answer = ["O"] * n

    for i in deleted:
        answer[i - 1] = "X"
    
    return "".join(answer)
    
