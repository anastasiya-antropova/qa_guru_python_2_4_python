#объявляем функцию и аргументы
def funcs():
    print("kokoko")

def print_message(message,end):
    print(message, end=end)
print_message("hello", end=", ")
print_message("world", end=". ")
print("")

#возвращаем значение
def lower_string (string:str):  #в скобках - типизация
    return string.lower()

def upper_and_lower_string (string:str):  #в скобках - типизация
    return string.upper(), string.lower()

print(lower_string("DSEdE"))
print(upper_and_lower_string("dfRRfdfRR"))

#переменное количество аргументов

def print_all_arguments(*args):
    for arg in args:
        print(arg)  #!!!вместо этого цикла можно просто написать print(*args) потому что и *args и новая строка есть в описании функции print
#NB print(*args) - вывод каждого элемента друг за другом, print(args) - вывод списка
print_all_arguments(1,2,3,4,5,6,7)

#словарик
def func_with_kwargs(**kwargs): #kwargs - именованные аргументы
    print(kwargs)

func_with_kwargs(key=123, second=321)



def wrapped_print(*args,**kwargs):
    print("Начинаем печать")
    print(*args,**kwargs)
    print("Заканчиваем печать")

wrapped_print("Печатаем", end="\n\n")


#функция - тоже объект, ее можно присваивать
def by_age(d):
    return d["age"]

by_age({"name":"Oleg", "age":32})

users=[
    {"name":"Oleg", "age":32},
    {"name":"Olga", "age":36},
    {"name":"Mol", "age":18},
    {"name":"Teg", "age":85},
    {"name":"Join", "age":45}
]

print(sorted(users,key=by_age)) #!передаем функцию внутрь другой функции без скобок как объект
print(max(users,key=by_age))