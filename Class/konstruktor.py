class MyClass:
    def __init__(self, n='Белый'):
        self.name=n
        print(f'Результат метода __init__: {self.name}')
    def fun1(self, arg1):
        self.number=arg1
        self.number2=33
        self.result = self.number+self.number2
        print(f'Результат метода fun1: {self.result}')
    def __del__(self):
        print(f'Объект удален при помощи деструктора __del__: {self.name}')


A=MyClass()
B=MyClass('Черный')
C=MyClass('Зеленый')
A.name='Красный'


# Вывод:

# Результат метода __init__: Белый
# Результат метода __init__: Черный
# Результат метода __init__: Зеленый

# Объект удален при помощи деструктора __del__: Красный
# Объект удален при помощи деструктора __del__: Черный
# Объект удален при помощи деструктора __del__: Зеленый
