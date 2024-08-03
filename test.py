txt=input('Введите текст: ')
symb=input('Какую букву нужно найти?: ')
num=txt.find(symb)
L=[]
while num!=-1:
    L.append(num)
    num=txt.find(symb,num+1)

if L==0:
    print('Такой буквы нет в тексте')
else:
    print(f'Позиции буквы {symb} в тексте: {L}')