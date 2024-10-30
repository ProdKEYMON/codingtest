import numpy as np
def solution(num_list, n):
    answer = [[]]
    a = np.array([num_list])
    answer = a.reshape(len(num_list)//n, n).tolist()
    return answer