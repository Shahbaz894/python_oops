class addition:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        
    def additon(self):
        return self.a + self.b
    
class minus:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def minu(self):
        return self.a - self.b
    
class result(addition,minus):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
        
        print('ye result class h')
        
d=result(80,30)

print(d.additon())
print(d.minu())
        