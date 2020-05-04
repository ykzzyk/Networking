#!/usr/bin/env python3

# Basic Python threading example
#
# Set script as executable via: chmod +x threads.py

import sys
import threading

# Python-style thread class
class ThreadDemo(threading.Thread):
    # The __init__() method is a constructor. It is run
    # when this class is instantiated. Do startup work here
    def __init__(self, name, startNum):
        threading.Thread.__init__(self)  # Required (don't ask why)

        # Set any variables you want in your constructor
        self.name = name
        self.startNum = startNum

    # The run() method of a Thread class is run when
    # thread.start() is called. Do real work here
    def run(self):
        print("Running thread '%s' starting at %d" % (self.name, self.startNum))
        i=self.startNum
        while(i < (self.startNum+10)):
            print(self.name + ", Count " + str(i))
            i=i+1

            # "Busy work" for demo program.
            # Otherwise, the threads will run so quickly
            # that they will finish before the scheduler
            # switches to a different thread
            j=0
            while(j<400000):
                j=j+1

        # To exit the thread, just return from the run() method
        

def main():
    print("Running in main()...")

    print("Launching two threads...")
    thread1 = ThreadDemo("Thread 1", 100)
    thread1.start()
    thread2 = ThreadDemo("Thread 2", 200)
    thread2.start()
    print("Launched two threads...")

    # Build up a list of all threads
    # (to make it easy to wait on them)
    all_threads=[]
    all_threads.append(thread1)
    all_threads.append(thread2)

    # Use the join() function to wait for a specific thread to finish
    # (i.e. thread1.join() or thread2.join())
    print("Waiting for all threads to finish")
    for one_thread in all_threads:
        one_thread.join()
    print("All threads have finished")

    print("Exiting main()...")


if __name__ == "__main__":
    sys.exit(main())
