def permutation(arr, r):
    result = []
    def permute(p, idx):
        if len(p) == r:
            result.append(p)
            return
        for i, data in enumerate(arr):
            if i not in idx:
                permute(p+[data], idx+[i])

    permute([],[])
    return result

def combination(arr, r):
    result = []
    def combinate(c, idx):
        if len(c)== r:
            result.append(c)
            return
        for i, data in enumerate(arr):
            if i > idx:
                combinate(c+[data], i)

    combinate([], -1)
    return result