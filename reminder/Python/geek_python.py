python3 # вызов интерпретатора

vscode visual studio code
vs code настройка
Урок 6 python extension и далее остановка на 8
 ctrl + ` ### вызов терминал в vscode также переключение между текстом и терминалом
 ctrk + b #боковая панель убрать поставить
 ctrl + tab ## переключение 
1 расширения =  python = install потом просто перезагрузи его

2 в правом нижнем углу vs code выберите интерпретатор
python 3.8 выбери 
справо появиться уведомление установите linter pylint позволяет видеть ошибки до запуска кода
ctrl + shift + m ### позволяет увидеть есть ли проблемы панель problems снизу view = problems

3 view = command palette =  ctrl + shift + p = lint = все команды lint (возможно надо выбрать on) = select linter = выбери pylint (самый популярный)

4 настройка шрифта = справо внизу шарнир = setings = text editor = font size 21 
настройки шрифта терминала = справо внизу шарнир = setings = features = terminal = font size 18 

5 русификация
плагин Russian Language Pack for Visual Studio Code установи его

6 настройка github
https://habr.com/ru/post/490754/#github

7 alt !!!!проблема с курсором исчезает при alt - shift смене языка просто меняю на ctrl + shift
https://ru.stackoverflow.com/questions/901929/vs-code-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%D1%83-alt
нlастройки = параметры = окно = custom menu bar alt focus (в поиске menu) галочку сними и alt  появиться
=====================
Итого
1 типы данных
int # числа
float # c плавающей точкой 
str # цифры
none #не определенное значение
() кортеж
[] список
{}  словари
boolean
2 print(type(a)) # показывает тип переменной если к пример a = '10' str!!!!!!
  print(type(int(a))) ## тип переменной которую будет преобразовывать в число из '10' в 10 как пример
3 my_set = set(my_list) # покажет не повторяющиеся значения hello  holo в случайном порядке 
4 print(int(a)) ## Преобразование переменной в число, если a = "10", но если a = "text" то нет


5 Ошибка Keyerror # проблема возможна с ключом словаря
6 Nameerror # проблема с переменной ключом
7 SyntaxError: invalid syntax # проблема с синтаксисом

======================
ТИПЫ ДАННЫХ

Теория
1 Объявление переменных
x = 1
y = 2
Hello = 'Hello, Bee'
list_dict = {"one": 1,  ## словарь с ключами
    "two": {            # список
    ["hello", 2]
}}

2 списки словари кортеж 
типы данных
int # числа
float # c плавающей точкой 
str # цифры
none #не определенное значение
() кортеж
[] список
{}  словари
boolean



my_list = []
my_list = ["Hello", 2, [1, 3, 4], {"one": 1}, 313, ] # [] квадратные скобки могуи быть там числа, строки, списки, словари
# в списке могут быть несколько списков

Кортеж # () список но не изменяемый объявил 5 значений больше уже не сделаю
a = ("s") # это не кортеж, это строка будет!!!!!!!
a = ("s",) # () tuple это уже кортеж так как есть запятая 
print(type(a)) # покажет тип переменной tuple  кортеж 

print(type(a)) # показывает тип переменной !!!!!!

3 my_set = set(my_list) # покажет не повторяющиеся значения hello  holo в случайном порядке 

4 словари
my_dict = {"one": 1}
my_dict2 = {
	"one": 1,
	"two": 2,
	"three": 4,
	4: "four"
}
В словаре как значения может быть списки и другие словари



Практика

1 Работа с целыми числами

a = 2
y = 4

a + y 
a - y 
a **y # 2 в четвертой степени
a * y 
a / y 
a % y # остаток от деления 10 % 3 = 1 (из 3 мы можем одно получить целое число 9 ближе к 10, поэтому 10 - 9 = 1)

Пример
a = 2
y = 4

print(a - y)
# -2 вывод и так далее
int / float можно работает не во всех языках

2 Сравнения
a == y
a != y
a >= y
a <= y
a < y
a > y
Результат True или False

3 a = "10" # все это строка 
  y = 4 
print(int(a)) ## Преобразование переменной в число, если a = "10", но если a = "text" то нет

   
4 float 
a = 3.33
y = 4
print(int(a)) 
print(type(int(a)))
print(type(a))

3 # вывод 
<class 'int'>
<class 'float'>

==============================
строки
1 a = "" что-то в кавычках
a = 'Hello'
a = "adsds"
a = "sdsad \n \tjdjadj dsdsadsa" ## \n c другой строки, \t табуляция
a = """       #только с тройными кавычками так можно делать
dasdasdasd
adsdadada
adsdadada
"""
print(a)
dasdasdasd
adsdadada
adsdadada

2 Сложение строк
a = 'Hello'
x = "adsds"

print(a + x)
Helloadsds ## вывод
print(a + ' ' + x)
Hello adsds ## вывод с пробелом
print(a * 2) 
HelloHello

3 Обращение по индексу
1
a = 'Hello'
x = "adsds"

print(a[0]) # в питоне можно обращаться по индексу 0 первый символ
H # вывод

2 
a = 'Hello geek Hello Hello'
x = "adsds"

print(a[3:10])  # по 10 индекс он не учитывается
# lo geek вывод
print(a[3:]) ### от третьего индекса до конца
#lo geek Hello Hello
print(a[:5]) # по 5 символ
#Hello
print(a[-7:])
#o Hello # выведит с конца
print(a[1::3]) ## шаг каждый третий индекс
# eoe l l вывод каждый третий индекс 
print(a[::3]) # сначало строки какждый третий символ
#Hlgkeoeo
print(a[::]) # просто ведит всю строку от начало до конца
#Hello geek Hello Hello
print(a[::-1]) ## строка перевернеться задом на перед
# olleH olleH keeg olleH 

3 len() применяется как со списками строками словарями и т.д., и другие способы
a = 'Hello geek Hello Hello'
x = "adsds"
 
print(len(a)) 
# 22 символа длина строки переменной a
print(a.upper()) # все в верхнем регистре
# HELLO GEEK HELLO HELLO
print(a.lower()) # все в нижнем регистре
#hello geek hello hello
print(a.title()) ## все слова станут с заглавной буквы, поменяется только первая буква
# Hello Geek Hello Hello
print(a.count("He")) # сколько раз He входит в нашу строку 
# 3 раза He
print(a.find("ge")) # найдет на каком индексе находится значение "ge"
# 6 c этого индекса начинается значенеи ge
print(a[a.find("ge")::]) # просим от начало ge до конца вывести нам срез
# geek Hello Hello
print(a.replace("be",  "He")) # поменять местам "be" на "He" ? в начале показываем что меняем потом на что 
#Hello Heek Hello Hello ## Heek

# a = '///H/ello geek Hello Hello///' # если а будет иметь такое значение 
print(a.strip("/")) ## удалит в начале и в конце / в тексте трогать не будет
# H/ello geek Hello Hello

print(a.split(" ")) #!!!! разбиваем строку по определенным параметрам здесь пробел получим список с отдельными значениями
['Hello', 'geek', 'Hello', 'Hello'] ### получим список так слова поделили на пробелы отдельные значения при парсинге

4 Форматтирование строк
1
a = 'Hello geek Hello Hello  %s' % "abracadra"
x = "adsds"

print(a)  ## abracadra добавиться
# Hello geek Hello Hello abracadra 
2
a = 'Hello geek %s Hello Hello' %"abracadra" # Если поставить по середине, то по середине и поставиться
print(a) 
# Hello geek abracadra Hello Hello #вывод старый способ
3
a = 'Hello {} geek Hello Hello'.format("abracadra") # ставим {} в строке, в конце дописываем .format(значение), что хотим добавить
print(a) 
Hello abracadra geek Hello Hello

4
a = 'Hello {} {} geek {} Hello Hello'.format("abracadra", "abracadra", "abracadra") # ставим {} в строке несколько, должен в .format(значение) количестов раз прописать
print(a) 
# Hello abracadra abracadra geek abracadra Hello Hello ## три разаabracadra

5 
a = 'Hello {1} {0} geek {0} Hello Hello'.format("sam", "peace") # sam это 0 , 1 это peace индексы по индексу
print(a) 
# Hello peace sam geek sam Hello Hello ## peace в начале так как 1 в начале

6 Передача по переменным

a = 'Hello {name} {country} geek {city} Hello Hello'.format(name="sam",country="Belarus", city="Minsk") 
## по переменным обрати внимание, что после format()внутри скобок пробел не нужен
# можно и так name=2**2 # просто в выводе будет вы водить 4 
print(a) 
# Hello sam Belarus geek Minsk Hello Hello # подставит по переменным

x = "Hi {name}"
print(x.format(name="man"))
# Hi man ## просто добавляем к значение переменной ддругое значение переменной

7 формат f строки !!!!!

1 name = 10
y = f"asdasd {name}" # после f"..."  если между ними пробел то вывод с пробелом
print(y) 
# asdasd 10 

2
y = f"asdasd {2**2}" ### в скобках можно делать мат операции
print(y) 
# asdasd 4 ## вывод можно даже делать вычитания

======================================
Списки [] !!!!
списки a + b получаем один большой сприсок

1
a = [1, 123, 987, "hello", [1, 23, "hi"]] ## добавить можно числа, строки, список 
print(a)
# [1, 123, 987, 'hello', [1, 23, 'hi']]
print(a[::-1]) # :: вывести весь список от начало до конца, разворачиваем наш список задом наперед
# [[1, 23, 'hi'], 'hello', 987, 123, 1] # вывод 
print(a[2:4])
# [987, 'hello'] # помни с 2 по 4, 4 индекс не считается и не выводится
print(a[-1]) #вытаскиваю последний элемент
# [1, 23, 'hi']
print(a[-1][1]) ## выводим последний элемент (внутренний список) и одновременно обращаемся к его первому индексу 23 
# 23 

2 
a = [1, 123, 987, "hello", [1, 23, "hi"]] 
a.reverse() # эту функцию надо обявлять отдельно таким способом
print(a)  ## print(a.reverse()) ## так нельзя будет ошибка
#[[1, 23, 'hi'], 'hello', 987, 123, 1] # вывод
print(a[4])
#[1, 23, 'hi'] # вывод 4 элемента

a = [1, 123, 987, "hello", [1, 23, "hi"], 34] 
print(len(a))
# 6 элементов 

3 sorted
a = [1, 123, 987, "hello", [1, 23, "hi"], 34] 
#sorted(a)(и отдельно не сортирует)(создаст новоую переменную) и print(a) будет ошибка так как разные типы данных текст сложно сортировать возрастанию
b = [1, 34, 1234, 2, 5 ]
# sorted(b) # отдельно работать как reverse() работать не будет
print(sorted(b))
#[1, 2, 5, 34, 1234] # вывод будет отсортировано по возрастанию

b.sort() # но если сделать вот так
print(b) ## список числовой будет отсортирован по возрастанию
Вывод 
y = sorted(b) ## если делаю так то я должен объявить новую переменную у так как sorted(b) создает новоую переменную
a.sort() # сортирует текущий список

4 добавление, объдениние, сложение, удаление, поиск индекса, вставка
1

a = [1, 123, 987, "hello", [1, 23, "hi"], 34] 
b = [1, 34, 1234, 2, 5 ]
a.append("he") # добавил новое значение в список he
print(a) 
#[1, 123, 987, 'hello', [1, 23, 'hi'], 34, 'he'] # вывод добавился he

a.extend(b) # объядинил a со списком b
print(a)
# [1, 123, 987, 'hello', [1, 23, 'hi'], 34, 1, 34, 1234, 2, 5] 

y = a + b # списки можно слаживать, но для этого надо объявлять новую переменную y
print(y)
# [1, 123, 987, 'hello', [1, 23, 'hi'], 34, 1, 34, 1234, 2, 5] # по сути тоже самое что выше
# разница a.extend(b) меняет текущий объект a, сложение нужно создвать новую переменную

a.pop(-1) ## удаление последнего элемента 34
print(a)
#[1, 123, 987, 'hello', [1, 23, 'hi']] #без 34 

у = a.pop(-1) # мы удалим 34 со списка а, y станет 34 

2
a = [1, 123, 987, "hello", [1, 23, "hi"], 34] 
b = [1, 34, 1234, 2, 5 ]
a.remove(123) # удаляю 123  со списка а

print(a)
# [1, 987, 'hello', [1, 23, 'hi'], 34] # без 123 выведит 

y = a.index(34) # узнаю index 34 элемента, обязательно надо присвоить новое значение переменной
print(y)
#5 # выведит
print(a[5]) ## проверка выведит 34

a.insert(2, "hiho") ## вставка вместо элемента с списком 2 (987) ставим hiho, а 987 и остальные подвинутся вправо
print(a)
#[1, 123, 'hiho', 987, 'hello', [1, 23, 'hi'], 34]


==============================================
Словари Dict{} !!!!!!!
списки словари парсинг!!!!!
{ключь: занчение}

1 a = {"begeek":123, "beg":"123", 2:"sdf", 1:[1,32,412], "hello":{1:2}} # строки в кавычках, числа списки, сами словари
# "hello":{1:2} hello это ключь словаря другого словаря и пройдемя от 1 индекса до 2 в его значении
# значение может быть одинаковым но не ключи
print(a["begeek"]) ## смотрю значение ключа begeek помни про [begeek]
# 123
print(a[1]) # смотрю значения внутреннего списка
#[1, 32, 412]
print(a[1][0]) # обращаюсь к ключу 1, вывожу значения списка по индексу 0 будет 1
# 1 

2 
a = {"begeek":123, "beg":"123", 2:"sdf", 1:[1,32,412], "hello":{1:2}}

y = {
	"Hello":1,
	"Hi": 2,
	"one": 1, # запятые в словаер это очень серьзно
	"two":{ ### two ключь со словарем еще одним
		"one": 1,
		"two": 2,
		"info": { ##info ключь с еще одним словарем

		}

	}
}

print(y["two"]) # обращение к ключу two
#{'one': 1, 'two': 2, 'info': {}}
print(y["two"]["one"]) ## хочу выввести значение словаря two (ключь), ключь внутреннего словаря, которого one
# 1  значение
print(y.keys()) ## вывожу все ключи словаря y
# dict_keys(['Hello', 'Hi', 'one', 'two']) # вывод
print(y["two"].keys()) ## вывожу все ключи вложенного словаря
# dict_keys(['one', 'two', 'info']) # вложенный словарь смотрим значения two
print(sorted(y)) # отсортированный список
# ['Hello', 'Hi', 'one', 'two']
y.clear() # очистил словарь
print(y)
# {} # вывод пустой словарь переменной y, но y переменная осталось 

y.update({1:23})  # добавление в конец словаря нового ключа с новым значение
print(y)
# {'Hello': 1, 'Hi': 2, 'one': 1, 'two': {'one': 1, 'two': 2, 'info': {}}, 1: 23} # в конеце словаря добавили 1: 23

del y["Hi"] ## удаляем с словаря конкретный ключь и его значение
print(y)
# {'Hello': 1, 'one': 1, 'two': {'one': 1, 'two': 2, 'info': {}}} # Hi c его значением пропало

print(y.keys()) ## выдергиваем все ключи с словаря !!!!
# dict_keys(['Hello', 'Hi', 'one', 'two']) # выдергиваем все ключи
print(y.values()) ## выдергиваем все значения ключей
#dict_values([1, 2, 1, {'one': 1, 'two': 2, 'info': {}}])
print(y.items()) ## выдергиваем все значения ключи и значения
# dict_items([('Hello', 1), ('Hi', 2), ('one', 1), ('two', {'one': 1, 'two': 2, 'info': {}})])
print(y.get("Hi")) ## получить значение ключа Hi из списка 
#2
print(y["Ho"]) # ошибка такого ключа нету 
#KeyError: 'Ho'
print(y.get("Ho")) ## так ошибки не будет из-за того что нету в списке данного ключа 
# None удобно делать проверку none и тогда ошибки не будет и не надо делать исключения


3 
a = {"begeek":123, "beg":"123", 2:"sdf", 1:[1,32,412], "hello":{1:2}} # строки в кавычках, числа списки, сами словари
# "hello":{1:2} hello это ключь словаря другого словаря и пройдемя от 1 индекса до 2 в его значении
# значение может быть одинаковым но не ключи

y = {
	"Hello":1,
	"Hi": 2,
	"one": 1,
	"two":{ ### two ключь со словарем еще одним
		"one": 1,
		"two": 2,
		"info": { ##info ключь с еще одним словарем

		}

	}
}

b = y
print(b)
# {'Hello': 1, 'Hi': 2, 'one': 1, 'two': {'one': 1, 'two': 2, 'info': {}}} 
# выведит словарь которой под y, но есть одна проблема что если y словарь поменяется, то в b тоже поменяется
b["Hi"] = 10 # поменяем значение, таком случае в и y словарь тоже поменяется
# {'Hello': 1, 'Hi': 10, 'one': 1, 'two': {'one': 1, 'two': 2, 'info': {}}} 
b = y.copy() # чтобы такого не было делаем отдельную копию словаря y теперь два разных одинаковых словаря и можно менять 
# значения отдельно
b["Hi"] = 10  # поменяется только в словаре b, y словарь не поменяется

==================================
set множество тип данных 
1 
a = [1, 3, 33, 45, 1, 3, 33]
b = set(a) # позволит вывести список без повторяющихся значений 
print(b) 
# {1, 3, 45, 33} фигурные скобки останутся только уникальные элементы

2
a = [1, 3, 33, 45, 1, 3, 33]
b = [3, 5, 1313, 234] # позволит вывести список без повторяющихся значений 
y = set(a + b) # a + b сложили два списка получили один большой список, set уберет повторяющийся значения
print(y) 
# {1, 33, 3, 1313, 5, 234, 45} # один большой список с уникальными значениям
print(y, a + b)## выведим значения y(список) c уникальными значениями и a + b # один большой список
# {1, 33, 3, 1313, 5, 234, 45} [1, 3, 33, 45, 1, 3, 33, 3, 5, 1313, 234] # один уникальный список  и другой большой список с уникальными значениями

3 
a = [1, 3, 33, 45, 1, 3, 33]
y = set(a) # позволит вывести список без повторяющихся значений 
y.add(50) # потом в конце добавить значение 50 
print(y)
# {1, 33, 3, 45, 50} # в конце появится 50

4
a = [1, 3, 33, 45, 1, 3, 33]
y = set(a) # позволит вывести список без повторяющихся значений 
y.add(50) # потом в конце добавить значение 50 
y.discard(1) # удалить  элемент который равен 1, если указать 6 то ничего не будет так как такого значения нет
# y.clear() # очистит множество
print(y) ## 
# {33, 3, 45, 50} # 1 пропала


4.1 
b = set("dasada dadsad dsafgfgf jkjll") # можно  и строки смотреть выведить уникальные значения 
print(b)
# {'l', 'k', 'f', ' ', 'j', 's', 'd', 'a', 'g'} ## по буквам уникальные значения 
 

5
a = {1, 13, 234, 90, 2}
print(a)
# {1, 2, 234, 13, 90}
 
6 
a = {1, 13, 234, 90, 2}
b = {4, 3, 15, 50, 90}
y = a.union(b)# union объединяет объекты, при этом нужно создать новую переменную обязательно тк новый объект
# y = a | b # аналог команды выше вывод тот же 
print(y)
# {1, 2, 3, 4, 234, 13, 15, 50, 90} # просто объединил два множество в одно большое и поместил в переменную y
# у множества все значения уникальны поэтому в вывыде одно значение 90


7 
a = {1, 13, 234, 90, 2}
b = {4, 3, 15, 50, 90}
y = a.intersection(b)# узнаем какое из двух множеств одинаково 90 вывод будет где множества пересекаются
print(y)
# {90} # вывод 

8 
b = set("dasada dadsad dsafgfgf jkjll") # можно  и строки смотреть выведить уникальные значения 
print(b)
# {'l', 'k', 'f', ' ', 'j', 's', 'd', 'a', 'g'} ## в
 

=====================================
Boolean
True
False

1
a = True # тоже самое что а = 1 
print(a) # true выведит
print(int(a)) ## преобразуем в цифру выведит в единицу
#True вывод
#1

2 a = True # тоже самое что а = 0 
print(a) # false выведит
print(int(a)) ## преобразуем в цифру выведит в 0
#False
# 0




=========================================================================================================
Циклы, обработка ошибок, условные выражения

условные выражения
1 if  если

some = 11
if some == 10: ## если some равно 10 то напиши нам следующие:
 	print(some) ## ничег не произойдет так как some равно
if some != 10: # если some не равно 10 
	pass
if some > 10:  # если some больше 10
	pass
if some <= 10: # если some меньше либо равно 10
if not some: # если не some true то сделай это 
	print(some) # но ничего не будет так как some имеет значение это true 

2 if some > 0 and some != 15: # если some более 0 но меньше 15 сработает если все условия выполняться
	print(15) ## напиши на 15 это тело цикла

3 some = [1, 3, 4, 5]

if 1 in some:  # я проверяю есть ли в списке значение 1 то тогда напечатай "ok" !!!!! проверяю список
	print("ok") # вывод ок но если выше указать 2 ничего не произойдет

4 if "last" in "inlastendworld": ## опять проверяю есть ли в строке значение last в строке inlastendworld
	print("ok") #  ок напечатает так как last входит в нашу строку

5 
some = [1, 3, 4, 5]
some_dict = {1:"one", "two": 2} # словарь первый ключь число второй ключь строка

if 1 in some_dict: # если есть 1 в словаре some_dict (именно в ключах!!!) то напиги ок
	print("ok") # ok

if "two" in some_dict: # аналок того что выше только с друшим ключом !!!!!
	print("ok") # ok

if 1 in some_dict.keys(): # тоже аналог !!!!!
	print("ok") # тоже ok

6 Проверяем длину

some = [1, 3, 4, 5]
some_dict = {1:"one", "two": 2} # словарь первый ключь число второй ключь строка

if len(some) < 3: # сначало находит длину списка, потом сравниваес < 3
	print ("error") #ничего не будет так как список более 3 
======================================
while # редко применяется, но применяется в бесконечных циклах
1
some = 10 

while some != 30:
	print("ok", some)
	some +=1 ## чтобы цикл не был бесконечным будет просто постоянно добавлять 1 

#10 # вывод от 10 до 29 вывод будет 30 не будет не равно
..
#29

while True: ## бесконечный цикл пока True
	print("True")
	some += 1  

2 ввод пользователя !!!!!!! так можно проверять пароли и так далее

some = input("enter a text:") # функция input предлогает ввести данные, данные которые введет user сохраняться в переменную some!!!
some_true = False


while not some_true: ## если у нас не some_true то выполняй цикл  !!!!!!
	if len(some) != 5: # считаем длину, потом сравниваем если не равно != 5 !!!! 
		some = input("введите текст заново, но не более 5 символов") # то предложить ввести пользователю еще данные 
	# будет постоянно предлогать ввести текст
	elif len(some) == 5: ### если равно 5  то 
		some_true = True ## тогда это True
		print("спасибо, что вы с нами")

=================================================
1 for

for text in hello: # hello это своего рода список если словарь то записываем ключи
print(text)
text # вывод так как в hello 5 букв
text
text
text
text

2 
for text in range(10): # здесь пройдемся по индексам
	print(text) # пройдет по индексам 
0
1
2
3
4
5
6
7
8
9

3 индексы
for text in range(5, 10): # здесь пройдемся по индексам от 5 до 10, пройтись только по 5 индексам
	print(text) 
5
6
7
8
9

4 hello
some = ["h", "e", "l", "l", "o"] # тоже самое что hello ниже 

for text in range(len("hello")): # здесь пройдемся по индексам от 5 до 10, пройтись только по 5 индексам
	print("hello"[text]) # здесь hello тоже самое что список, text могу итерваться по индексу
h
e
l
l
o

16:28
