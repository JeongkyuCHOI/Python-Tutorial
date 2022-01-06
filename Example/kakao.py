'''
이용자의 ID가 담긴 문자열 배열 id_list, 
각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

2 ≤ id_list의 길이 ≤ 1,000
1 ≤ id_list의 원소 길이 ≤ 10
id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
1 ≤ report의 길이 ≤ 200,000
3 ≤ report의 원소 길이 ≤ 21
report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
id는 알파벳 소문자로만 이루어져 있습니다.
이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
자기 자신을 신고하는 경우는 없습니다.
1 ≤ k ≤ 200, k는 자연수입니다.
return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

'''
def solution_my(id_list, report, k):
    id_len = len(id_list)
    
    # 동일인 중복 신고 삭제
    sorted_report = list(dict.fromkeys(report))
    
    # 신고 당한 유저 검색 
    bad_user_list = [] 
    for report in sorted_report:
        bad_user = report.split(' ')[1]
        bad_user_list.append(bad_user)
    print('신고당한 유저', bad_user_list)
    
    # k번 이상 신고당한 유저 검색 
    reported_user_list = []
    for name in bad_user_list:
        if bad_user_list.count(name) >= k:
            reported_user_list.append(name)
    print('제제 당할 유저', reported_user_list)
    
    # 신고성공 email 받을 유저 검색
    user_list = []
    for report in sorted_report:
        user, bad_user = report.split(' ')
        if bad_user in reported_user_list:
            user_list.append(user)
    print('회신 받을 유저', user_list)
    
    # email 받는 횟수 카운트
    email_list = [0]*id_len
    for i, ids in enumerate(id_list):
        # total = reported_user_list.count(ids) + user_list.count(ids)
        total = user_list.count(ids)

        email_list[i] = total
    
    print('결과', email_list)
    return email_list

from collections import Counter

def solution(id_list, report, k):
    id_len = len(id_list)
    answer = [0] * id_len
    
    send_dict = {} 
    get_dict = {} 
    result_dict = {}
    for id in id_list:
        send_dict[id] = set()
        get_dict[id] = set()
        result_dict[id] = 0
    
    for repo in report:
        usr, bad_usr = repo.split(" ")
        send_dict.get(usr).add(bad_usr)
        get_dict.get(bad_usr).add(usr)
    for i in range(id_len):
        if len(get_dict[id_list[i]]) > k-1:
            for send in send_dict.keys():

                if id_list[i] in send_dict[send]:
                    result_dict[send] += 1 
    
    for i in range(id_len):
        answer[i] = result_dict.get(id_list[i])
    
    # print('정답', answer)
    return answer

if __name__=='__main__':
    solution(
            ["muzi", "frodo", "apeach", "neo"],
             ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
             2
             )
    solution(
            ["con", "ryan"],
             ["ryan con", "ryan con", "ryan con", "ryan con"],
             3
             )