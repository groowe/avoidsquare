# another try on sqr
# this time with classes
import re

class Row():
    def __init__(self,bin_str):
        self.binstr = bin_str if type(bin_str) == str else bin(str(bin_str))[2:]
        self.side = len(self.binstr)
        self.possibilities = [[] for i in range(self.side-1)]
        self.tested = []
        self.ones = -1
        self.decstr = int(self.binstr,2)
        self.__count__()
        self.combine()

    def combine(self,to=''):
        selfself = False
        if not to:
            to = self.binstr
            selfself = True

        if to in self.tested:
            return
        for i in range(self.side-1):
            found = '0'
            b = self.side - ( i + 2 ) + (self.side*i)
            for item in range(2):
                stone = str(item) + '.{' + str(i) + '}' + str(item)
                st = stone + '.{' + str(b) + '}' + stone
                cb = '2' * (self.side * i)
                ss = self.binstr + cb + str(to)
                if re.search(st,ss):
                    found += '1'

            if not int(found) and to not in self.possibilities[i]:
                #print(ss,st)
                self.possibilities[i].append(self if selfself else to)
        self.tested.append(self if selfself else to)
        return

    def isin(self,item='',rownum=0):
        """ checks if item (Row) is in self.possibilities"""
        # safety check:
        #if not item or type(rownum) != int or not(0 <= rownum < s1elf.side ):
        #    return False
        return item in self.possibilities[rownum]

    def poss(self):
        return self.possibilities

    def __count__(self):
        """amount of ones in self.binstr"""
        self.ones = self.binstr.count('1')

    def c_ones(self):
        """amount of ones in string"""
        if self.ones < 0:
            self.count()
        return self.ones

    def dec(self):
        """decimal representation of binary string"""
        return self.decstr

    def __repr__(self):
        """string"""
        return self.binstr
