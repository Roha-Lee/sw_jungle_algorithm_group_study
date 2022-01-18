# Programmers - Hash - 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579#

def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []		# defaultdic 사용안하고 그냥 빈 배열 생성.
        genres_dict[genres[i]].append([i, plays[i]])	# 그 후에 append 시켜서 인덱스, 값 형태로 추가

    for g in genres_dict:	# 딕셔너리 값을 이용해서 list에 총합값을 저장.
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)	# 리스트에 저장한 값을 내림차순 정렬
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer

a = solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500] )
print(a)