way1 = [int(i) for i in input().split()]
rubbish = []
now_min = 1
def cut_list(l1, l2, now_min):
    temp = l1[:l1.index(now_min)] 
    for i in range(len(temp)):
        l2.insert(0, temp[0]); del temp[0]
    for i in range(l1.index(now_min) + 1):
        del l1[0]
    return now_min + 1    
def take_sequence(r, now_min):
    checker = 0
    for i in range(len(r)):
        if r[i] == now_min:
            r[i] = 0
            now_min += 1; checker += 1
        else:
            break
    del r[:checker]            
    return now_min

while len(way1) != 0:
    now_min = cut_list(way1, rubbish, now_min)
    now_min = take_sequence(rubbish, now_min)
if (len(rubbish) == 0) or (rubbish == list(range(min(rubbish), max(rubbish) + 1)) and min(rubbish) == now_min):
    print('Yes')
else:
    print('No')
input('Press enter to exit: ')    