#1

# number=int(input('Enter Number: '))


def count_digits(number):
    k=0
    while True:
        if number>0:
            number=number//10
            k=k+1
        else:
            return k


# print(f'Amount of digits in a {number}: {count_digits(number)}')

#2=========================================================

# number=input('Enter Number: ')
# print(number)

def replace_nine(number):
    result=''
    for i in number:
        if i!=0:
            rest=str(9-int(i))
            result=result+rest
        else:
            result=result+'9'
    return result


# print(f'result: {replace_nine(number)}')


#3===================================================

def equality_list(list1,list2):
    for i in list1:
        for j in list2:
            if i==j and list1[i]!=list2[j]:
                return 'A Lists are not equal because elements different' #Списки не равны
            else:
                break
        print('!')
    return 'A Lists are equal' #Списки равны


def equality_list_summ(list1,list2):
    if sum(list1)==sum(list2):
        print('sum')
        return equality_list(list1,list2)
    else:
        return 'A Lists are not equal because sum different' #Списки не равны


def list_condition(list1,list2):
    # Проверка равенства длины двух массивов
    if len(list1)==len(list2):
        print('condition')
        return equality_list_summ(list1,list2)
    else:
        return 'A Lists are not equal because len different' #Списки не равны

try:
    list1=list(input('Enter first list: ').split(',')) #Через запятую вводи числа
    list2=list(input('Enter second list: ').split(',')) #Через запятую вводи числа

    list1=list(map(int, list1))
    list2=list(map(int, list2))

    print(list_condition(list1,list2))
except ValueError:
    print('Вас попросили ввести список!')




