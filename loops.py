#while

a=0
while a<10:
    print("Hi"+str(a))
    a+=1

#for. Итерируем списки и словари

i=0
for i in range(5,20,3):
    print(f"HHHHi {i}")

for element in [1,2,'dd']:
    print(element)


for i, element in enumerate([1,2,'dd']):
    print(i, element)

#словарь
for key, value in {"first":1, "second":2}.items():
    print(f"у ключа {key} значение {value}")


from .functions import print_message
print_message("123") #??? почему не печатает