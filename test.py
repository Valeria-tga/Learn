 # txt=input('Введите текст: ')
# symb=input('Какую букву нужно найти?: ')
# num=txt.find(symb)
# L=[]
# while num!=-1:
#     L.append(num)
#     num=txt.find(symb,num+1)
#
# if L==0:
#     print('Такой буквы нет в тексте')
# else:
#     print(f'Позиции буквы {symb} в тексте: {L}')


#======================================================================================

txt=f'Hello World'
sym=1234

print (f'{txt !r}') # печатает текст в кавычках благодаря инструкции r!
print (f'{txt !s}') # печатает текст !s это тоже самое что и функция str()
print (f'{sym !a}') # печатает текст

print (f'{sym:*<9}') # печатает текст
