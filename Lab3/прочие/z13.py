#cos(alpha)=(b**2+c**2-a**2)/2bc
from math import acos,degrees
def cosinustheor(s1,s2,s3):
    return acos((s2**2+s3**2-s1**2)/(2*s2*s3))
sides=[float(c) for c in input().split()]
angles=list()
angles.append(degrees(cosinustheor(sides[0],sides[1],sides[2])))
angles.append(degrees(cosinustheor(sides[1],sides[0],sides[2])))
angles.append(degrees(cosinustheor(sides[2],sides[0],sides[1])))
print(angles)