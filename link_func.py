#Аргумент функции - функция и два числа
def display(f,a,b):
    for k in range(a,b+1):
        print("{0:4}".format(f(k)), end=" ")
    print("\n")


#Результат функции - функция (лямбда)
def mypow(n):
    return lambda x:x**n

#Аргументы функции - функции. Результат тоже функция
def apply(f,h):
    def calc(x):
        return f(h(x))
    return calc


#Определение функций

A=mypow(2)
B=mypow(3)
C=apply(lambda x: 2*x+1, lambda x: 2*x)

#Проверка результата

print('x ', end='')
display(lambda x: x,1,5)

print('A(x) ', end='')
display(A,1,5)

print('B(x) ', end='')
display(B,1,5)

print("C(x)", end='')
display(C,1,5)


#Определение функции

F=lambda f: lambda x: f(f(x))


#ПРоверка результата

print('F(x->x*x)(5): ', F(lambda x: x*x)(5))
print('F(x->2*x+1)(5): ', F(lambda x: 2*x+1)(5))

#========================================================================
