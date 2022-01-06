import math 

def solution(n, k):
    answer = 0
    
    # n을 k진수로 변환
    nk = ''
    while(n != 0):
        n, remainder = divmod(n, k)
        nk += str(remainder)
    nk = nk[::-1] 
    print('변환된 수', nk)    

    nk_nonzero = nk.split('0')
    
    len_nk = len(nk_nonzero)
    for i in range(len_nk):
        isP = True
        if nk_nonzero[i] == '':
            continue
        if int(nk_nonzero[i]) > 0:
            num = int(nk_nonzero[i])
            if num == 1:
                isP = False
                continue
            if (num != 2) and (num%2 ==0):
                isP = False
                continue
            
            if isP:
                cal = num ** 0.5
                cal = math.floor(cal)
                for i in range(3, cal, 2): 
                    if (num % i) == 0:
                        isP = False
                        break
            if isP:
                answer += 1
    print('답', answer)
    return answer
if __name__=='__main__':
    solution(437674, 3)
    solution(110011, 10)
