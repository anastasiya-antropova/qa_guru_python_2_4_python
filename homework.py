# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def beauty_print(func_name, *args):
    func_name = func_name.__name__.title().replace('_'," ").capitalize()
    arg = ", ".join(args)
    print(func_name, " - ", arg)

def open_browser(browser_name):
    beauty_print(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    beauty_print(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    beauty_print(find_registration_button_on_login_page, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https://www.google.com")
find_registration_button_on_login_page("https://www.google.com", "Sign in")
