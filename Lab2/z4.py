from math import sin
x=float(input('х='))
y=0
if x>0:
    y=sin(x)
else:
    y=6-x
print('Для х={0} y={1}'.format(x,y))