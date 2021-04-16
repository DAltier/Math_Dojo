class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums) :
        self.result += num
        for var in nums :
            self.result += var
        return self
    def subtract(self, num, *nums) :
        self.result -= num
        for var in nums :
            self.result -= var
        return self


md1 = MathDojo()
x = md1.add(2).add(2,5,1).subtract(3,2).result
print(x)	

md2 = MathDojo()
y = md2.add(7).add(6,3).subtract(8).result
print(y)	

md3 = MathDojo()
z = md3.add(3,6,7,2).add(6,8,3).subtract(32,12).result
print(z)	


