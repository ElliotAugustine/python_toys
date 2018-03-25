import math
class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        d, t = self.data, []
        n = len(d)
        for g in range(n):
            t.append([])
        for i, row in enumerate(d):
            if max(row)!=r or min(row)!=1 or len(set(row))!=r:
                return False
            for k, num in enumerate(row):
                t[k].append(num)
        for 
        n = len(d)
        if sqrt(n)**2!=n:
            return False
        valid(d, n)