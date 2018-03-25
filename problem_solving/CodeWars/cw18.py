# 세 명의 미팅 스케쥴이 주어질 때 세명이 duration 시간 동안 만날 수 있는 최초의 시각 구하기

def get_start_time(schedules, duration):
    dic, end, endic = {}, 540, {}
    for i in range(len(schedules)):
        dic[i] = [(int(x[:2]))*60 + int(x[-2:]) for k in schedules[i] for x in k]
        endic[i] = end
    while end + duration <= 1140:
        for n in dic.keys():
            while dic[n] != [] and end + duration > dic[n][0]:
                dic[n].remove(dic[n][0])
                endic[n] = dic[n].pop(0)
        if end == max(endic[g] for g in endic.keys()):
            return '%s%s:%s%s'%(end//60//10,end//60%10,end%60//10,end%60%10)
        else:
            end = max(endic[g] for g in endic.keys())
    return None