a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number:"))
class areas:
    """FUCTION TO CALCULATE AREA of SHAPES"""
    def __init__(self,variableA:int,variableB:int):
        self.a=variableA
        self.b=variableB
    def square(self):
        """FUCTION TO CALCULATE AREA OF SQUARE"""
        print("area of square :", self.a * self.a)
    def circle(self):
        """FUCTION TO CALCULATE AREA OF CIRCLE"""
        print("area of circle :",3.14 * self.a*self.a)
    def Triangle(self):
        """FUCTION TO CALCULATE AREA OF TRIANGLE"""
        print("area of triangle :",1/2 * self.a*self.b)
    def Rectangle(self):
        """FUCTION TO CALCULATE AREA OF RECTANGLE"""
        print("area of rectangle :",self.a*self.b)
    def sphere(self):
        """FUCTION TO CALCULATE AREA OF SPHERE"""
        print("area of sphere :",4 * 3.14 * self.a*self.a)
c=areas(a,b)
c.square()
c.circle()
c.Triangle()
c.Rectangle()
c.sphere()