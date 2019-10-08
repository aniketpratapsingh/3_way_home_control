#!/usr/bin/python

import pylirc


blocking = 0;





def setup():
    pylirc.init("pylirc", "./pylirc.conf", blocking)


def loop():
    while True:
        s = pylirc.nextcode(1)

        while (s):
            for (code) in s:
                print 'Command: ', code["config"]
            if (not blocking):
                s = pylirc.nextcode(1)
            else:
                s = []


def destroy():
    pylirc.exit()


if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()

