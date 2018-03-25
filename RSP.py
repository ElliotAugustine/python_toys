# Rock Scissors Paper
from random import choice


class RSP:
    rsp = ('R', 'S', 'P')
    win = 0

    def doit(self):
        you = be_nice()
        com = choice(RSP.rsp)
        if RSP.rsp.index(you) - RSP.rsp.index(com) == 2:
            RSP.win += 1
            r = 'won'
        elif RSP.rsp.index(you) - RSP.rsp.index(com) == 1:
            RSP.win -= 1
            r = 'lost'
        elif RSP.rsp.index(you) - RSP.rsp.index(com) == -1:
            RSP.win += 1
            r = 'won'
        elif RSP.rsp.index(you) - RSP.rsp.index(com) == -2:
            RSP.win -= 1
            r = 'lost'
        else:
            r = 'tied'
        print("You chose {} and the computer chose {} so you {}".format(you, com, r))

    def result(self):
        if RSP.win > 0:
            status = "won"
        else:
            status = "lost"
        print("You {} {} games more than the computer".format(status, RSP.win))


def be_nice():
    you = input("input R for rock, S for scissors and P for paper: ")
    if you not in RSP.rsp:
        print("Oh, Try Again!")
        you = be_nice()
    return you


if __name__ == "__main__":
    k = RSP()
    while abs(RSP.win) < 3:
        k.doit()
    k.result()