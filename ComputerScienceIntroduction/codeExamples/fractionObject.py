### Try adding a reduce method 


class Fraction(object):
    """
      A number represented as a fraction
    """
    
    def __init__(self,  num: int,  denom: int) -> None:
        """  num and denom are integers"""
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
        
    def __str__(self) -> str:
        """ Returns a string representation self"""
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self, other) -> str:
        """ Returns a new fraction representing"""
        top = self.num * other.denom + self.denom  * other.num
        bott = self.denom * other.denom
        
        return Fraction(top, bott)
    
    def __sub__(self, other):
        """ Returns a new fraction representing """
        top = self.num * other.denom - self.denom *other.num
        bott = self.denom * other.denom
        
        return Fraction(top,  bott)
    
    def __float__(self) -> float:
        """ Returns a float value of the fraction"""
        
        return self.num / self.denom
    
    def inverse(self):
        """ Returns a new fraction representing  """
        return Fraction(self.denom, self.num)
    
a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b # c is a fraction objects
        
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
        
        