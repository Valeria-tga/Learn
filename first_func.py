#1


def cycle_list_limit(number2):
    number1=0
    while True:
        yield number1
        number1 +=1
        if number1>=number2:
            number1=(number1)%(number2)


def check_lenght(list1,list2):
    if len(list1)==len(list2):
        return True
    elif len(list1)>len(list2):
        diff = len(list1)-len(list2)
        return list2, diff, list1
    elif len(list1)<len(list2):
        diff = len(list2)-len(list1)
        return list1, diff, list2


def full_list(list1,diff):
    result_list=list1
    if len(list1) == 1:
        for i in cycle_list_limit(len(list1)):
            result_list = result_list + list(list1[i])
            diff = diff - 1
            if diff == 0:
                break
    else:
        for i in cycle_list_limit(len(list1)-1):
            result_list=result_list+list(list1[i])
            diff=diff-1
            if diff==0:
                break
    return result_list



def main(list1,list2):
    result_list=list()
    for i in range(len(list1)):
        mult=int(list1[i])*int(list2[i])
        result_list.append(mult)
    return result_list

list1=list(input('Введите первый числовой список: ').split(','))
list2=list(input('Введите второй числовой список: ').split(','))

result=list(check_lenght(list1,list2))
# print(result[0])
list_full=full_list(result[0], result[1])
# print(list_full)

print(f'Result lists: \n {list_full} \n {result[2]} \n')
print(f'Result: {main(list_full,result[2])}')

# 1,2,3,4,5,6,7


