import math

class Rational:

    def __init__(self, numerator, denominator=1): # Value 1 is a default value in case we do not pass it.
        '''Creates a rational from its numerator and denominator.'''
        self._numerator = numerator
        self._denominator = denominator

    def __eq__(self, other):
        '''Implementation of x == y'''
        return self._compare(other) == 0

    def __ge__(self, other):
        '''Implementation of x >= y'''
        return self._compare(other) >= 0

    def __gt__(self, other):
        '''Implementation of x > y'''
        return self._compare(other) > 0

    def __le__(self, other):
        '''Implementation of x <= y'''
        return self._compare(other) <= 0

    def __lt__(self, other):
        '''Implementation of x == y'''
        return self._compare(other) < 0

    def __str__(self):
        '''Returns a human-readable string.'''
        if self._denominator == 1:
            return f'{self._numerator}'
        else:
            return f'{self._numerator}/{self._denominator}'

    def __neg__(self):
        '''Implementation of -a'''
        return Rational(-self._numerator, self._denominator)

    def __add__(self, other):
        '''Returns the sum of two rationals'''
        return Rational(self._numerator * other._denominator + other._numerator * self._denominator, self._denominator * other._denominator)

    def __sub__(self, other):
        return Rational(self._numerator * other._denominator - other._numerator * self._denominator, self._denominator * other._denominator)

    def __mul__(self, other):
        return Rational.reducefract(Rational(self._numerator * other._numerator, self._denominator * other._denominator))

    def __truediv__(self, other):
        return Rational(float((self._numerator / other._numerator) / (self._denominator / other._denominator)).as_integer_ratio()[0], float((self._numerator / other._numerator) / (self._denominator / other._denominator)).as_integer_ratio()[1])

    def _compare(self, other):
        if self._denominator * other._denominator > 0:
            return self._numerator * other._denominator - self._denominator * other._numerator
        else:
            return -self._numerator * other._denominator + self._denominator * other._numerator

    def reducefract(self):
        def gcd(self):
            d = self._denominator
            k = 1/d
            n = self._numerator
            l = 1/n
            while d != 0:
                t = d
                d = n%d
                n = t
            return n
        greatest=gcd(self)
        self._numerator/=greatest
        self._denominator/=greatest
        return Rational(round(self._numerator), round(self._denominator))




if __name__ == '__main__':

    one = Rational(1) # Note: we can call the __init__ method with only one parameter!
    half = Rational(1, 2)
    twoThirds = Rational(2, 3)

    # To test implementation of __str__:
    print(f'The twoThirds variable: {twoThirds}')

    # To test implementation of + operator:
    print(f'Addition of rationals: 1 + 1/2 = {one+half}')

    # To test implementation of - operator:
    print(f'Subtraction of rationals: 1 - 1/2 = {one-half}')

    # To test implementation of * operator:
    print(f'Multiplication of rationals: 1/2 * 2/3 = {half*twoThirds}')

    # To test implementation of / operator:
    print(f'Division of rationals: 1/2 / 2/3 = {half/twoThirds}')

    # To test implementation of comparisons:
    L = [ Rational(1), Rational(5,3), Rational(4,7), Rational(-3,2), Rational(-50,3), Rational(12,7) ]
    for x in sorted(L):
      print(f'Next rational in sorted list is {x}.')

