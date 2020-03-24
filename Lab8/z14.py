from math import sqrt
class Vector:
    x=0
    y=0
    z=0

    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x=x2-x1
        self.y=y2-y1
        self.z=z2-z1

    def printvect(self):
        print(self.x, self.y, self.z)

    def length(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    def plus(self, v2):
        v=Vector(0, 0, 0, 0, 0, 0)
        v.x = self.x + v2.x
        v.y = self.y + v2.y
        v.z = self.z + v2.z
        return v

    def minus(self, v2):
        v=Vector(0, 0, 0, 0, 0, 0)
        v.x = self.x - v2.x
        v.y = self.y - v2.y
        v.z = self.z - v2.z
        return v

    def skal_pr(self, v2):
        return self.x*v2.x+self.y*v2.y+self.z*v2.z

    def cosinus(self, v2):
        return self.skal_pr(v2)/(self.length()*v2.length())

ab=Vector(-2,1,5,2,0,3)
ac=Vector(-2,1,5,4,3,-1)
ab.printvect()
ac.printvect()
print(ab.length())
print(ac.length())
summa=ab.plus(ac)
razn=ab.minus(ac)
summa.printvect()
razn.printvect()
print(ab.skal_pr(ac))
print(ab.cosinus(ac))