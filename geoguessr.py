from keyboard import press_and_release as par
from random import randint as rand

while True:
    for _ in range(4):
        par(str(rand(0, 9)))
    par("enter")
    for _ in range(4):
        par("backspace")
