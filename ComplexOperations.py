import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, no):
        a = self.real + no.real
        b = self.imaginary + no.imaginary
        return Complex(a, b)
    
    def __sub__(self, no):
        a = self.real - no.real
        b = self.imaginary - no.imaginary
        return Complex(a, b)
        
    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        denom = no.real**2 + no.imaginary**2
        if denom == 0:
            return Complex(0, 0)
        a = (self.real * no.real + self.imaginary * no.imaginary) / denom
        b = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(a, b)

    def mod(self):
        result = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(result, 0)
    
    def __str__(self):
        if self.imaginary == 0:
            return "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                return "0.00+%.2fi" % (self.imaginary)
            else:
                return "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary < 0:
            return "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        else:
            return "%.2f+%.2fi" % (self.real, self.imaginary)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
