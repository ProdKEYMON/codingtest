def solution(cards1, cards2, goal):
    answer = []
    n, m = len(cards1), len(cards2)
    i = j = 0
    
    for w in goal:
        if i < n and w == cards1[i]:
            answer.append(cards1[i])
            i += 1
        elif j < m and w == cards2[j]:
            answer.append(cards2[j])
            j += 1

    return 'Yes' if answer == goal else 'No'