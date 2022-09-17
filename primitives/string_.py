s="i am 'test'!"
s='i am "test"!'
s='i am \'test\'!' #экранирование если одного типа кавычки
s="""i 
"am "'test'
!""" # вместо экранирования или ''' '''   #это 3 разных строки

#перенос строки
multiline_string="first\nsecond"

#сырые строки - никакие специмволы не работают
print(r"this is stri\ng")

#конкотинация - складывание строк - +

#индексы и слайсы
alphabet="abcdefg"
alphabet[1]
alphabet[0:3] #слайсинг
alphabet[0:-1:2] #с шагом
alphabet[::-1] #обр порядок


#оперирование - ПОСМОТРЕТЬ САМИМ
"first".format()

#форматирование
first="first"
second="second"
third="third"

print(f"{first} {second} {third.title()} {100}") #!современный способ форматирования строк
print("{third} {1} {0}".format(first, second, third=third.title())) #предыдущий способ форматирования строк
print("%s %s %s" % (first, second, third.title())) #более старый способ, но он есть в др языках. мощный изза какихто надстроек

#конвертация строки в число и наоборот - потенциальное место ошибок
str(123)
int("123456")

("first","second","third").split() #разделяем строку в список
