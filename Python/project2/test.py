from random import *

'''
count = 0
def running_up_stairs(t, n):
    global count
    temp = []
    
    temp.append(0)
    
    count = count + 1
    temp.append(1)
    
    if n == 1:
        return count
    count += 2
    return running_up_stairs(t, n-1)
'''

def generate(n):
    temp = []
    for num in range(0, pow(2, n-1)):
        if num == n-1:
            temp.append(1)
        ran = randint(0, 1)
        if ran == 0 and len(temp) != 0:
            if temp[-1] == 0:
                continue
            else:
                temp.append(ran)
        else:
            temp.append(ran)
        
    print(temp)

generate(5)

'''
def running_up_stairs(t, n):
    
    total_item = []
    for num in range(0, pow(2, n)):
        temp = []
        for x in range(0, n):
            if x == n-1:
                temp.append(1)
            else:
                ran = randint(0, 1) 
                if ran == 0 and len(temp) != 0:
                    if 0 == temp[-1]:
                        continue
                    else:
                        temp.append(ran)
        if temp not in total_item:
            total_item.append(temp)
        print(temp)
    
    count = 0
    for k in total_item:
        if len(k) == n:
            count = count + 1

    print(total_item)
    return count

  
if __name__ == '__main__':
    count = running_up_stairs(1, 5)
    print(count)
'''