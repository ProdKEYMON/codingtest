import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    a = arr1
    b = arr2
    answer = np.dot(a,b).tolist()
    return answer