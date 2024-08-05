
# Фнкция, которая выводит список с нечетными числами
def odd_list(list1):
    for i in list1:
        if int(i)%2==0:
            list1.remove(i)
    return list1

list1=list(input('Введите числа через запятую: ').split(','))
print(odd_list(list1))