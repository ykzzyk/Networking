import threading
from time import sleep

data = []

def get_input():
    data.append(input("Please enter your input here: "))
    #testing
    # print('done. data value:', data[0])

input_thread = threading.Thread(target=get_input)
input_thread.start()

#wrong location #1
#input_thread.join()

for i in range(10):
    print(i)
    sleep(2)
    
    #wroing location #2
    #if i == 6:
    #   input_thread.join()

#correct location
input_thread.join()

print('done. data value:', data.pop())
