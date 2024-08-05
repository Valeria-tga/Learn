#1
import itertools


def cycle_list_limit(number2):
    number1=0
    while True:
        yield number1
        number1 +=1
        if number1>number2:
            number1=(number1)%(number2)


def check_lenght(list1,list2):
    if len(list1)==len(list2):
        return True
    elif len(list1)>len(list2):
        diff = len(list1)-len(list2)
        return list2, diff
    elif len(list1)<len(list2):
        diff = len(list2)-len(list1)
        return list1, diff


def full_list(list1,diff):
    result_list=list1
    for i in cycle_list_limit(len(list1)):
        result_list=result_list+list(list1[i])
        diff=diff-1
        if diff==0:
            break
    return result_list



# def main(list1,list2):


list1=list(input('Введите первый числовой список: ').split(','))
list2=list(input('Введите второй числовой список: ').split(','))

result=list(check_lenght(list1,list2))
print(result[0])
print(full_list(result[0], result[1]))

# 1,2,3,4,5,6,7
# print(check_lenght(list1,list2)[1])

# print(list_full)

# print(full_list()))

