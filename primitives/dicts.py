#словари
#заводим словарь

d = {
    "key": "value",
    123: "another",
    10: {"another": "first"},
    (1,2,3): "fafafa"

}
print(d[10])
print(d[(1,2,3)])
#print(d["browser"]) #ошибка

#функции словарей
print(list(d.keys()))
print(list(d.values()))
print(list(d.items())) # значения выводятся парами - кортежами, где есть ключ и значение

print(d.get("key"))
print(d.get("browser")) #возвращает None
print(d.get("browser", "chrome")) #если нет browser значения, делаем хром