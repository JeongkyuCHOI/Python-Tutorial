def solution(fees, records):

    base_time = fees[0] # 180
    base_fee = fees[1] # 5000
    min_time = fees[2] # 10
    min_fee = fees[3] # 600
    
    map_dict = {}
    result_dict = {}
    for record in records:
        t, n, io = record.split(' ')
        time = t.split(':')
        print('타임', time)
        t = int(time[0]) * 60 + int(time[1])
        
        if n in map_dict.keys():

            inTime = map_dict[n]
            totalTime = t - inTime
            if n in result_dict.keys():
                result_dict[n] += totalTime
            else:
                result_dict[n] = totalTime
            del(map_dict[n])
        
        else:
            map_dict[n] = t
        
    for key in map_dict.keys():
        t = 59 + (23 * 60)

        inTime = map_dict[key]
        totalTime = t - inTime
        if key in result_dict.keys():
            result_dict[key] += totalTime
        else:
            result_dict[key] = totalTime
        del(map_dict[key])
        
    nums = []
    for key in result_dict.keys():
        nums.append(key)
    nums.sort

    answer = []
    
    for i in range(len(nums)):
        totalTime = result_dict[nums[i]]
        fee = 0 
        totalTime -= base_time
        fee += base_fee
        
        if totalTime > 0 :
            fee += (totalTime / min_time) * min_fee
            if (totalTime % min_time) > 0:
                fee += min_fee
            
        answer.append(fee)


    return answer

if __name__=='__main__':
    solution([180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])