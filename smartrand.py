import time


def rint(from_, to):
    last = str(time.time())[-1]
    while not (from_ <= int(last) <= to):
        last = str(time.time())[-1]
    return last
