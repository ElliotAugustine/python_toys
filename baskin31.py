import random
from RSP import RSP
print("배스킨 라빈스 31!")


class Baskin(RSP):

    def declare(self, num, p='COM'):
        def numbering():
            n = 0
            while not n:
                try:
                    n = int(input("How many numbers are you going to say? "))
                except ValueError:
                    print("We need a number")
                    pass
            if n not in (1, 2, 3):
                print("You should input 1 or 2 or 3")
                n = numbering()
            return n
        if p == 'COM':
            n = random.randint(1, 3)
        else:
            n = numbering()
        if num + n > 31:
            n = 31 - num
        print("{} said {}".format(p, [num + x + 1 for x in range(n)]))
        return num + n

    def play(self):
        cur = 0
        players = ['YOU', 'COM']
        while abs(self.win) != 1:
            self.doit()
        if self.win < 0:
            players.reverse()
        p = players[1]
        print("First Player: {}".format(players[0]))
        while cur != 31:
            p = players[1-players.index(p)]
            cur = self.declare(cur, p)
        print("{} said 31 so {} won".format(p, players[1-players.index(p)]))


if __name__ == "__main__":
    bl = Baskin()
    bl.play()