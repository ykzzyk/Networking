
def ants(pole, n):
    MAX = MIN = 0
    for i in range(0, n):
        dis = int(input("The position of the ant: \n"))
        if dis <= 0 or dis >= pole:
            raise ValueError("The position of the ant is not valid")
        opp = dis
        rest_pole = pole - dis
        #find the minimum time
        dis = min(dis, rest_pole)
        if dis > MIN:
            MIN = dis
        #find the maximum time
        opp = max(dis, rest_pole)
        if opp > MAX:
            MAX = opp
    print(f'{MIN} {MAX}')


if __name__ == '__main__':
    instance = int(input("Please input the instance number: \n"))
    if instance > 1000000:
        raise ValueError("The limit is 1000000 instances!\n")
    
    count = 0
    for ins in range(0, instance):
        print(f"\n\ncase{ins+1}\n")
        if count < instance:
            pole = int(input("Please type in the length of the pole:\n"))
            if pole > 1000000:
                raise ValueError("The limit number is 1000000!\n")
            n = int(input("Please type in the number of the ants:\n"))
            if n > 1000000:
                raise ValueError("The limit number is 1000000!\n")   
            print("\t")
            ants(pole, n)
            count = count + 1
        else:
            break
    