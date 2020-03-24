class Counter:
    count=0

    def __init__(self,cou):
        self.count=cou

    def plusone(self):
        self.count+=1

    def minusone(self):
        self.count-=1

counter1=Counter(0)
counter2=Counter(10)
print(counter1.count)
print(counter2.count)
counter1.plusone()
counter2.minusone()
print(counter1.count)
print(counter2.count)