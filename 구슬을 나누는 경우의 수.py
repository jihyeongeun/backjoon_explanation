def solution(balls, share):
    n = 1
    sum1 = 1
    sum2 = 1
    sum3 = 1

    for i in range(1, (balls - share) + 1):
        sum1 *= n
        n += 1

    n = 1
    for i in range(1, share+1):
        sum2 *= n
        n += 1

    n = 1
    for i in range(1, balls+1):
        sum3 *= n
        n += 1
    answer = sum3 / (sum1 * sum2)
    return answer