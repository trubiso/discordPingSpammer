import random
import time
from playsound import playsound
import os.path
import sys


def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        print("please input a parameter with your notification filename")
        exit(1)
    else:
        return sys.argv[index]


if __name__ == '__main__':
    filename = get_arg(1)
    if not os.path.exists(filename):
        print("file invalid (does not exist)")
    else:
        while True:
            randnumber = random.randint(1, 6)
            print("random number is " + str(randnumber))
            if randnumber == 6:
                print("played notification sound")
                playsound(filename)
            timetosleep = int(random.randint(0, 10) / randnumber)
            print("sleeping " + str(timetosleep) + " seconds")
            time.sleep(timetosleep)
