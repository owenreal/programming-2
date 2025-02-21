import time
import threading as thread

def print_nums(start, end, delay):
    for i in range(start, end):
        time.sleep(delay)
        print(i, " ")

def print_letters(delay):
    for letter in "abcdefghij":
        time.sleep(delay)
        print(letter)

t1 = thread.Thread(target=print_nums, args=(1, 11, 0.25))
t2 = thread.Thread(target=print_nums, args=(10, 21, 0.5))
#t2 = thread.Thread(target=print_letters, args=(1))
t1.start()
t2.start()

# wait for threads to complete before exiting
t1.join()
t2.join()