class Class1:
    a=0
    b=0

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __del__(self):
        print("Object's deleted")

obj=Class1(1,2)
print(obj.a, obj.b)