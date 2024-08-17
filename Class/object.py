class Alpha:
    pass

class Bravo:
    pass

#Переменной присваивается имя класса
MyClass=Alpha
print(f'MyClass = {MyClass}')

#Создание объекта
A=MyClass()
print(f'A = {A}')

#Переменной присваивается имя класса
MyClass2=Bravo
print(f'MyClass2 = {MyClass2}')

#Создание объекта
C=MyClass2()
print(f'C = {C}')

# Получение ссылки на объект реализации класса
link_A=A.__class__
print(f'link_A = {link_A}')

link_C=C.__class__
print(f'link_C = {link_C}')

