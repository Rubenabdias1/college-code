class Fraction:
    def __init__(self, top, bottom):
        if(not isinstance(top, int)):
            raise ValueError("The value provided for top (%s) is not an integer"%top)
        if(not isinstance(bottom, int)):
            raise ValueError("The value provided for bottom (%s) is not an integer"%bottom)

        common = self.gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __add__(self, other):
        newNum = self.num * other.den + \
                 self.den * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)

    def __sub__ (self, other):
        newNum = self.num * other.den - \
                 self.den * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    
    def __mul__(self, other):
        newNum = self.num  * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)

    def __truediv__(self, other):
        newNum = self.num  * other.den
        newDen = self.den * other.num
        return Fraction(newNum, newDen)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __ne__(self, other): 
        if(isinstance(other, Fraction)):
            return self.num != other.num or self.den != other.den 
        return False

    def __gt__(self, other):
        return self.num / self.den > other.num / other.den

    
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __lt__(self, other):
        return self.num / self.den < other.num / other.den
    
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def gcd(self, m, n):
        while m % n != 0:
            oldM = m
            oldN = n
            m = oldN
            n = oldM % oldN
        return n
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        

    
