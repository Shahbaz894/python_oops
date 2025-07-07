class Fraction:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '{} / {}'.format(self.x, self.y)
    
    def __add__(self,other):
        num=self.x*other.y + other.y*self.x
        den=self.x*other.y
        return '{} / {}'.format(num, den)

# Example usage
F = Fraction(4, 5)
F1 = Fraction(7, 8)
print(F+F1)

        