"""
https://school.programmers.co.kr/learn/courses/30/lessons/92342
양궁대회
"""


def calc_point(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_score += 10 - i
        else:
            lion_score += 10 - i
    return lion_score - apeach_score


# 지금쏘는 과녁 idx, 남은 화살 개수, 어피치점수, 내점수
def dfs(idx, n, apeach, lion):
    global answer, point
    if n < 0:
        return
    # 점수 계산
    if idx > 10:
        diff = calc_point(apeach, lion)
        if diff <= 0:
            return
        if diff > point:
            point = diff
            answer = [lion[i] for i in range(11)]
            answer[10] += n
        return

    # 상대가 쏜 점수보다 높이 쏴본다
    lion[10 - idx] = apeach[10 - idx] + 1
    dfs(idx + 1, n - lion[10 - idx], apeach, lion)
    lion[10 - idx] = 0
    dfs(idx + 1, n, apeach, lion)


def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    dfs(0, n, info, [0 for _ in range(11)])
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
