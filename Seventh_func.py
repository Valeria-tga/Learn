def rec(txt, index):
    result=''
    if index%2==1 and index<=len(txt)-1:
        print(index,'*',txt[index])
        rec(txt,index+1)
    elif index%2==0 and index<=len(txt)-1:
        rec(txt,index+1)
    return 'Конец проги'

text='Привет'
# print(len(text))

print(rec(text,0))

