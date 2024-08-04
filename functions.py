def yell(txt):
    return txt.upper()

print(yell('Hello'))
print('\n')
#============================================
bark=yell
print(bark('wolf'))
print('\n')
#=========================================

print(bark.__name__) # применяется внутренний идентификатор, чтобы определить на какую функцию ссылается bark для отладки
print('\n')
#=========================================

funcs=[bark, str.lower, str.capitalize]
print(funcs)

for i in funcs:
    print(i, i('HeLLo World'))
print('\n')
#=========================================

def greet(func):
    greeting=func('Hi, I am Python program')
    # print(greeting)
    return greeting

print(greet(yell))

print('\n')

#=========================================

def whisper(txt):
    return txt.lower() + '....'

print(greet(whisper))

print('\n')
#=========================================




