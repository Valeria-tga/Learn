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





