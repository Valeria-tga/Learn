#1


def check_lenght(list1,list2):
    if len(list1)==len(list2):
        return True
    elif len(list1)>len(list2):
        diff = len(list1)-len(list2)
        return 'list1', diff
    elif len(list1)<len(list2):
        diff = len(list2)-len(list1)
        return 'list2', diff

# def full_list(list1,list2)

# def main(list1,list2):


list1=list(input('Введите первый числовой список: ').split(','))
list2=list(input('Введите второй числовой список: ').split(','))

# print(check_lenght(list1,list2))
# print(check_lenght(list1,list2)[1])
