def solution(n, m, section):
    counter = 0
    while section:
        left = section[0]
        right = left + m
        while section and section[0] < right:
            del section[0]
        counter += 1
    return counter