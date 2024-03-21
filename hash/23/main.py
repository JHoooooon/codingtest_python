"""
*   베스트앨범

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

*   제한사항

-   genres[i]는 고유번호가 i인 노래의 장르입니다.

-   plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.

-   genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.

-   장르 종류는 100개 미만입니다.

-   장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.

-   모든 장르는 재생된 횟수가 다릅니다.


*   입출력 예

genres	                                            plays	                        return

["classic", "pop", "classic", "classic", "pop"]	    [500, 600, 150, 800, 2500]	    [4, 1, 3, 0]

*   문제 풀이

1.  genres_dict, priority_dict 선언

2.  genres 를 순회
    -   genres_dict[grenres[idx] + " " + str(idx)] 에 plays[idx] 를 할당
        -   grenres[idx] + " " + str(idx) 를 통해 해당 장르의 index 를 식별자로 넣음 
        -   이후 sort 시에 plays[idx] 가 같은 장르가 있다면, 해당 식별자 작은순으로 자동 정렬됨
    -   priority_dict[genres[dix]] += plays[idx] 를 넣어서, genre 우선순위를 정하기 위한 총 합계를 할당

3.  priority_dict.item(), genres_dict.item() 을 값으로 오름차순 정렬
    - 할당된 변수 priority, genres_count

4.  priority 을 순회
    -   itme = priority_genre
    -   genres_count 를 순회
        -   정렬되어있으므로, 2번만 순회하며 가장 먼저나오는 2개의 값만 answer 에 push
            -   genres_count 의 key 값을 가져와, split 하여, genre 와 idx 값을 추출
            -   순회하며, key 값과 priority_genre 와 같으면 answer 에 idx push

5.  answer 반환

"""

def solution(genres, plays):
    answer = []
    genres_dict = {}
    priority_dict = {}

    for idx in range(len(genres)):
        genres_dict[genres[idx] + " " + str(idx)] = plays[idx]
        if genres[idx] in priority_dict:
            priority_dict[genres[idx]] += plays[idx]
        else:
            priority_dict[genres[idx]] = plays[idx]
    
    priority = sorted(priority_dict.items(), key = lambda item: item[1], reverse=True)
    genres_count = sorted(genres_dict.items(), key = lambda item: item[1], reverse=True)

    for priority_genre in priority:
        i = 0
        for key, _ in genres_count:
            if i > 1:
                break

            genre, idx = key.split()
            if priority_genre[0] == genre:
                answer.append(int(idx))
                i += 1

    return answer

solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 500, 800, 2500]
)