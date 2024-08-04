shift=int(input('Введите сдвиг: '))
txt=input('Введите текст: ')

cipher=''

a=ord('а')
z=ord('я')
A=ord('А')
Z=ord('Я')

for i in txt:
    if (ord(i)>=a and ord(i)<=z) or (ord(i)>=A and ord(i)<=Z):
        i=chr(ord(i)+shift)
    elif ord(i)==z:
        i=chr(z+shift-1)
    elif ord(i)==Z:
        i=chr(Z+shift-1)
    cipher+=i

print('Шифр: ', cipher)

