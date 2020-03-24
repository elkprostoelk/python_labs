comp1={'rez':float(input('rez1=')), 'imz':float(input('imz1='))}
comp2={'rez':float(input('rez2=')), 'imz':float(input('imz2='))}
print(comp1)
print(comp2)
summa={'rez':comp1['rez']+comp2['rez'], 'imz':comp1['imz']+comp2['imz']}
pr={'rez':comp1['rez']*comp2['rez']-comp1['imz']*comp2['imz'], 'imz':comp1['imz']*comp2['rez']+comp1['rez']*comp2['imz']}
print('Сумма: ',summa)
print('Произведение:',pr)
