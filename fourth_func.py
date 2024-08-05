
def text_gen(txt='текст', *val):
    # mas=val
    result=''
    for i in val:
        print(i)
        if i<len(txt)-1:
            result=result+txt[i]
        else: break
    return result

text=input('Введите какой-нибудь текст: ')
# numbers=input('Введите какие-нибудь числа: ')

print(text_gen(text,2,4,5))