"""
Input : x = [3, 5, 7], a = 10, b = 5
Write a function compute_y : y = a * x + b
Assume : len(x) <= 10, 0 <= a <=20, 0 <= b <10 

Example Unit Test: compute_y(x, a, b)
ans = compute_y([2,4,5], 10, 2)
ans -> [2*10 + 2, 4 * 10 + 2, 5 * 10 + 2]
ans -> [22, 42, 52]

return List: Invalid []
"""

def compute_y(x, a, b):
    y = []
    for i in range(len(x)):
        #print(x[i])
        y.append(x[i]* a +b)
    return y
#(compute_y([1, 2], 3, 2))
assert compute_y([], 0, 0) == []
assert compute_y([1,1,1],1, 1) == [2, 2, 2]
assert compute_y([1, 2, 3], 0, 0) == [0, 0, 0]
assert compute_y([10, 20, 30, 40, 50, 60, 70, 80, 90], 2, 2) == [22, 42, 62, 82, 102, 122, 142, 162, 182]
