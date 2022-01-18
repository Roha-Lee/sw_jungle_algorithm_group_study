# Programmers - 힙(Heap) 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

# 03 19 26
# 0ms 시점에서 3ms , 1ms 시점에서 9ms, 2ms 시점에서 6ms

# Case 1
# 0~3 시작점 0이였기 때문에 3ms, 3~ 12  시작점 1ms 였기 때문에 11ms, 12~18 시작점 2ms였기 때문에 16ms
# 위 케이스의 경우 평균 작업시간 = 10ms = ((3+11+16) / 3)

# Case 2
# 0~3 시작점 0ms이기 때문에 3ms, C는 3~9 2ms이기 때문에 7ms, B는 9~18, 시작점 1ms이기 때문에 17ms
# 위 케이스의 경우 평균 작업시간 = 9ms = ((3+7+17) /3)

def solution(jobs):
    from heapq import heappush, heappop
    import operator

    current = 0
    answer = 0

    l = len(jobs)
    # jobs 배열 정렬 -> 0 = 작업 요청 시점, 1 = 작업 소요 시간
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))

    waitings = []   # waitings 배열에 jobs 저장
    heappush(waitings, (0, jobs.pop(0)))

    while waitings: # waitings 배열에 값이 존재하는 경우

        processing = heappop(waitings)[1]   # processing -> waitings의 1번인덱스 값 [0,3]같은 형태로 뽑음

        if processing[0] > current:    # 작업 요청 시간이 > current보다 클 경우
            current = processing[0] + processing[1] # current의 값에 processing의 요청 시점, 소요 시간 전부 가산
        else:
            current += processing[1]    #  current에 processing의 소요시간을 더해준다

        answer += (current - processing[0]) # answer에는 current에서 요청 시점을 뺀 값

        while True:
            if jobs and jobs[0][0] < current:   # jobs가 비어있지 않고, jobs의 요청 시점이 current보다 작으면
                heappush(waitings, (jobs[0][1], jobs[0]))   # waitings에 (jobs[0][1],jobs[0]) 값 넣어줌
                jobs.pop(0) # 그리고 jobs에서 맨앞의 값 빼주기
            else:
                if jobs and len(waitings) == 0: # jobs가 비어있지 않고, len(waitings) == 0 이라면

                    # loop until task with different start time     
                    prev = jobs[0][0]   # prev = jobs[0][0] 값 -> 작업 요청 시점
                    while jobs: 
                        job = jobs[0]   # job = jobs[0] 값  -> [요청시점, 소요시간]

                        if job[0] != prev:  # job[0] != prev?? 뭔의미지?
                            break

                        heappush(waitings, (job[1], job))   # waitings에 job[1] -> 소요시간, job(요청시점, 소요시간)
                        prev = job[0]   # prev = 요청시점으로 변경
                        jobs.pop(0)     # jobs의 맨앞(0)번째 pop

                break
    answer //= l    # answer = l로 나눔.

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]	))