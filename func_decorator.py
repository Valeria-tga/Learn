# ПРимер функции декоратора

#Эта функция null_dec - это функция декоратор
def null_dec(func):
    return func

#===================================================

def greet():
    return 'Hello!'

greets = null_dec(greet)

print(greets())

print('\n')
#===================================================

@null_dec
def grat():
    return 'HELLO'

print(grat())

print('\n')
#===================================================

# Функция декоратор
def uppercase(func):
    def wrapper():
        original_text=func()
        modified_text=original_text.upper()
        return modified_text
    return wrapper

@uppercase
def qwerty():
    return 'hello world'

print(qwerty())

print('\n')
#===================================================

def A(h):
    return lambda x: h(x)*h(7-x)

def B(h):
    return lambda x,y: h(x,y)+h(y,x)

def C(h):
    return lambda x: h(x,10-x)


#Фунции с декоратором:

@A
def f(x):
    return 2*x-1

@B
def F(x,y):
    return (8-x)*(y+1)

@C
def H(x,y):
    return x*y


print('f(3) = ', f(3))
print('F(5,7) = ', F(5,7))
print('H(6) = ', H(6))


