from random import randint
list1=[randint(-100,100) for i in range(randint(1,10))]
print('Unsorted list 1:',list1)
list2=[randint(-100,100) for i in range(randint(1,10))]
print('Unsorted list 2:',list2)
list1.sort(reverse=True)
print('Sorted list 1:',list1)
list2.sort(reverse=True)
print('Sorted list 2:',list2)
list3=list1+list2
print('Unsorted list 3:',list3)
list3.sort(reverse=True)
print('Sorted list 3:',list3)
