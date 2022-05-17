import threading
import time


def square(numbers):
    print('calculate square numbers !!!')
    for number in numbers:
        time.sleep(1)
        print('square of {} is {}'.format(number, number ** number))


def cube(numbers):
    print('calculate cube numbers !!!')
    for number in numbers:
        time.sleep(1)
        print('cube of {} is {}'.format(number, number ** number))


arr = [2, 3, 8, 9]
t = time.time()
thread1 = threading.Thread(target=square, args=(arr,))
thread2 = threading.Thread(target=cube, args=(arr,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Done in  : ", time.time() - t)
print("I have done with all my work now !!!")
