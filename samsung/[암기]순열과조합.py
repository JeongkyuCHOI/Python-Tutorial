# 순열 & 조합
# https://buyandpray.tistory.com/52
def permutation(arr, r):
    # 순열을 저장할 배열
    result = []

    # 순열 구하기
    def permute(p, idx):
        if len(p) == r:
            result.append(p)
            return

        for i, data in enumerate(arr):
            if i not in idx:
                permute(p+[data], idx+[i])

    permute([], [])
    return result

def combination(arr, r):
    # 조합을 저장할 배열
    result = []

    # 조합 구하기
    def combinate(c, idx):
        if len(c) == r:
            result.append(c)
            return

        for i, data in enumerate(arr):
            # 중복되지 않도록 새로 추가하는 원소의 인덱스가 큰 경우만 추가
            if i > idx:
                combinate(c+[data], i)

    combinate([], -1)
    return result
print(permutation([1,2,3], 2 ))
print(combination([1,2,3],2))