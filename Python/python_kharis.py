0  ModuleNotFoundError: No module named 'lxml # решение ошибки 
1 python3 -m venv venv # в папке проекта
2 source venv/bin/activate # активировал 
3 pip install lxml
4 pip install requests



1 python3 # вызов REPL в консоли
2 python3 hello.py # запуск приложения
3 python3 -m idlelib.idle # открываю idle где можно создавать сохранять файлы и запускать их f5 запуск

4 1 #!/usr/bin/env python3              
""" путь к питону """
    print("Hello world")
  2 chmod +x hello.py # даю права на исполнение
  ./hello.py # запуск приложения

5.1 Справка 
python3 # справка по модулю в терминале ввожу
help()
help> keyword

6 >>> import keyword # узнаю про ключевые слова нельзя использовать как переменные
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 

7 dir(__builtins__) # узнать встроенные имена которые негодятся для переменных
===========================================================================
Глава ввод(int) вывод(print) данных


Вывод данных(print)
1 print("hello there")
hello there
2 >>> print("I'm", 10, 'years old') # обрати внимание здесь ввод строк и чисел 
I'm 10 years old     # запятые не видны они работаю как запятые

Ввод данных user(input)
1 name = input("Enter your name: ") 
""" пользователь вводит данные мы сохраняем в name а потом крутим вертим эту переменную name """
print(name)
 """переменная просто вводим название без кавычек что делаю с name"""

2 input всегда возвращаест строку

>>> value = input('Enter a number:')
Enter a number:2

>>> other = input('Enter another:' )
Enter another:3

>>> value + other
'23' ## неожиданный результат так как мы сложии строки а не числа
>>> type(value)
<class 'str'> ## говорит что тип строка

int(value) + int(other)
""" Превращаю строки в числа и складываю их"""
5 # вывод 2 + 3

6 Задание 
"""Запросить имя и поздороваться """
1 name = input("Enter your name: ") 
print('Hello', name)
Hello sam #вывод

2 ''' Запросить сколько лет и сказать сколько будет в следующем годуы '''
age = input('Enter your age: ')
next_age = int(age) + 1
print("Your age next year", next_age)


Итого:
вывод print , ввод input
====================================================================================
Глава ПЕРЕМЕННАЯ 
Состояние, изменение
Программирование можно с моделировать все.
Лапмочка может обладать состояением, вкл, выкл, яроксть_max, яркость_min, переход из одного состояния в другое 
это изменение. Ламочка(объект) которая обладает теми или иными свойствами(состояниями).

1 Переменные как метки
переменные используется для хранения состояния

status = "off" ## запоминаю состояние лампочки
""" переменная status "off" это строковый тип данных""" 

2 Когда выхожу из конкретной функции переменные этой функции исчезают. Когда объект никому не нужен, счетчик равен 0 его 
подвергают уборке мусора. Если на объект указывают переменные или другие объекты то счетчик положителен и все норм.
>>> import sys
>>> names = []
>>> sys.getrefcount(names)
2
""" Узнаю счетчик ссылок"""

3 Информация о людях состояния:
'''Бирка на корове это грубо говоря как переменная '''
имя 
возвращаест 
адрес

4 status = 'off'
print(status)
""" мы создали переменную status позже когда нам надо узнать ее значение мы обратимся к ней как выше """
'''У объекта есть значение "off", тип строка, индетификатор(местонахождение в памяти как пример id(a) )
создается переменная и связывается с ней '''

5 "120 watt" ## мы создали строковый объект но теперь не можем к нему обратиться

wattage = "120 watt" 
''' теперь можем обратиться по переменной это одно из состояний лампочки '''
incandescent = wattage
wattage = "25 watt"
print(incandescent, wattage)
120 watt 25 watt
''' обрати на вывод сначало 120, а потом уже то что мы поменяли '''

6 Повторное связывание переменных
num = 400
num = '400' 
''' теперь это строка то что выше num = 400 уборщик мусора уничтожит '''
''' переназначение переменных не лучшая практика запутывает '''

7 Нельзя называть переменную по ключевому слову
"""Узнать все ключевые слова """
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 

8 Имена переменных
1 переменная нижнего регистра
2 можно использовать _
3 нельзя чтобы начинались с цифр
4 имена переменных не могут переопределять встроенные функции

Пример:
goog = 4 # +
bAd = 5 # верхний регистр -
a_longer_variable = 6 # +

baD_Longer_Var = 7 # так не очень
3treepy = 5 # так нельзя начало с цифр
for = 4 # нельзя ключевое слово
compile = 4 #нельзя встроенная функция

9 Встроенные имена которые нельзя использовать
dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
  'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
   'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 
   'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 
   'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 
   'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 
   'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 
   'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
    'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', 
    '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
     'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 
     'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
      'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 
      'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
       'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
        'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str',
         'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
===============================================================================
Объекты:
1 индетификатор
2 тип
3 значение  

1 Индетифкитор
Определяет местонахождения в памяти компьютера
name = "Matt"
first = name
id(name)
140699256961456 # место хранения в памяти
id(first)
140699256961456 # будет один и тот же индетификатор

 Индетифкитор позволяет узнать время создания объекта и возможно ли их изменения
first is name
''' Узнаем указывают ли две переменные на один и тот же объект '''
True 
Две переменные указывают на один и тот же объект
name = "Matt"
first = name
name = 'Fred'

>>> id(name)
140699254219184 # изменился
>>>id(first)
140699256961456 # остался тот же 


2 ТИП объекта
1 строки
2 целые числа
3 числа с плавающей точкой
4 логические значения

Тип объекта это класс объекта, класс опеределяет состояние данных хранящихся в объекте, также методы(действия),
которые может выполнить объект
>>>type(name) # узнаем тип объекта
<class 'str'>

Объект                    Тип

Строка                    str
Целое число               int
Число с плавающей точкой  float
Список                    list
Словарь                   dict
Кортеж                    tuple
Функция                   function
Класс с определяемый пользователем type 
Экземляр класса           class 
Встроенные функция        builtin_function_or_method
type                      type 

Для того чтобы узнать относится ли объект к типу поддерживающему некоторую операцию можно использовать встроенные классы
str , int , float , list , dict и tuple

>>> str(0)
'0' # вижу сразу строку можно ли сделать строку из этого
>>> tuple([1,2])
(1, 2)
>>> list('abc')
['a', 'b', 'c']
====================
Изменяемость 
Словари списки изменяемы
Строки кортежи целые числа, числа с плавающей точкой неизменяемые типы
Пример
1
>>> age = 1000
>>> id(age)
140532846920080 ## индетификатор

>>> age = age + 1
>>> id(age)
140532846920016 # индетификатор новый уже

2 >>> names = [] # список
>>> id(names)
140532846969280

>>> names.append('Fred') # добавил значение 
>>> names
['Fred'] 
140532846969280 # старый  id значение
140532846969280
ый id значение

Пример 3 
name = "Matt"
first = name
age = 1000
print(id(age))
age = age + 1
print(id(age))
names = []
print(id(names))
names.appent['fred']
print(id(names))


Вывод 
139756435201008 # вижу id 
139756434595536
139756435022784
139756435022784



1 python3 -m idlelib.idle
файл создать сохрани этот код = f5 
dir() # тут увижу переменные names, name
name
"Matt"
names
['Fred']


Упражнения 61 страница
1 
numb = 25
id(numb)
print(id(numb))
# 94475134881856

numb = 25 + 20
id(numb)
print(id(numb))
# 94630171501248 # разные номера

2 age = []
#id(age)
#print(id(age))
#140030905938944

age.append(300)
id(age)
print(id(age))
#140386085933952

===================================
Числа

>>> type(2)
<class 'int'>
>>> type(2.0)
<class 'float'>
У чисел с плавающей точкой есть погрешность небольшая из-за округления

Сложение 

1
>>> 2 + 6
8
>>> result = _
>>> result
8
""" так как здесь нету переменной то результат сохраняется в _ присваиваем значение переменной result """

2 >>> .4 + .01
0.41000000000000003

3 
>>> 6 +.2
6.2 # если целое число плюс с плавающей точкой то будет число с плавающей точкой 

4 print('num: %s' % 2)
num: 2

5 
>>> "Python" * 3
'PythonPythonPython' # просто сделают одну строку с тремя зачениями

>>> '4' * 2 
'44' # просто 2 раза по 4 # одна строка 2 значениями по 4 

6 Преобразования
>>> int(2.6)
2
>>> float(3)
3.0

7 Вычитание 
>>> .25 - .2
0.04999999999999999
>>> 2 - 6 
-4
>>> 6 - .2
5.8
>>> 

8 Умножение 
>>> 6 * 2
12
>>> .25 * 12
3.0


Деление 
1 >>> 12 / 4
3.0

2 >>> 3 / 4
0.75

3 >>> 3 // 4 # целочисленное деление
0

Остаток 
(Деление по модулю, находим остаток)

1 
4 % 3
1 # 4 -3 = 1 нечетное число

2 
>>> 3 % 2 
1 # нечетно если результат равен 1 

3 
>>> 4 % 2 
0 # четное число если равен 0 

4 
>>> 3 % 3
0
>>> 2 % 3
2
>>> 1 % 3
1
>>> 0 % 3
0

5 
>>> -1 % 3
2
>>> -1 % -3
-1
>>> 1 % -3
-2
>>>  
""" Но лучше так не делать """

Страница 68










