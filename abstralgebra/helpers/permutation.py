"""
    Generates all the permutations of the numbers from 1 to n
"""
def permute_n(n):
    if n == 1:
        return [{ 1: 1 }]

    curr_permutations = []
    prev_permutations = list(map(lambda x: list(x.values()),permute_n(n-1)))
    for i in range(n):
        for perm in prev_permutations:
            curr_perm = perm.copy()
            curr_perm.insert(i, n)
            curr_permutations.append(curr_perm)
    return list(map(lambda x: { i + 1: value for i, value in enumerate(x) }, curr_permutations))

"""
    Generates all the permutations of a list
"""
def permute(arr):
    if len(arr) == 1:
        return [{arr[0]: arr[0]}]
    
    curr_permutations = []
    prev_permutations = list(map(lambda x: list(x.values()), permute(arr[1:])))
    for i in range(len(arr)):
        for perm in prev_permutations:
            curr_perm = perm.copy()
            curr_perm.insert(i, arr[0])
            curr_permutations.append(curr_perm)
    
    return list(map(lambda x: { arr[i]: value for i, value in enumerate(x) }, curr_permutations))
    
        
    