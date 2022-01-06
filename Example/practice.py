def solution(participant, completion):

    participant.sort()
    completion.sort()
    for parti, compl in zip(participant, completion):
        if not parti==compl:
            answer = parti
            return answer

if __name__ =='__main__':
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])