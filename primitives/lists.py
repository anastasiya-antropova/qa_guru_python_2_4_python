#списки

l=[1,2,3]
l[0]
l[0:3]
l[::-1]

ll=[1,2,"kk",[1,"jj"]]
print(ll[3][0])

#функции списков
[1, 2, 3].append(2) #добавление элеметна в список
[1, 2, 3].extend([2, 5, 8]) #совмещение списков
a=[1, 2, 3].pop(0) #на выходе 1, но она будет убрана из списка

b=sorted([1,2,3]) #! в переменную записывается новый порядок
[1,2,3].sort() #меняется сам список


#множества
s=set([1,2,3])

s={1, 2, 3, 3, 3}
ss={3, 4, 5}

print(s & ss) #пересечение часть множеств
print(s | ss) #объединение часть множеств

l=[1,2,3,3,4,5]
l=set(l) #преобразования списка во множество
k=list(set(l)) #преобразовали обратно - но ушли дубли 3
print(l)
print(k)