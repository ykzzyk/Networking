def running_up_stairs(n):
    steps = 0
    if n == 2:
        steps = steps + 2
        return steps
    if n == 1:
        steps = steps + 1
        return steps
    if n == 0:
        return steps
    
    steps += 2
    
    return running_up_stairs(n-1) + running_up_stairs(n-2)

def judge():
    instance = int(input())
    results = []
    if instance > 5:
        raise ValueError("The limit is 5 instances!\n")
    while(instance):
        
        steps = int(input())
        if steps < 0 or steps > 22000:
            raise ValueError("steps should be in the (0, 22000)\n")
        result = running_up_stairs(steps)
        results.append(result)
        instance = instance - 1
    return results
    
if __name__ == '__main__':
    
    result = judge()
    for i in result:
        print(i)
    