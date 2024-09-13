def f(fer, x=0.5):
    try:
        ret = fer * x * (1 - x)
        if arr:
            direcs.append(ret > arr[-1])
        arr.append(ret)
        f(fer, ret)
    except RecursionError:
        pass

direcs = []
arr = []
f(2.9)
up, down = direcs.count(True), direcs.count(False) - 1
