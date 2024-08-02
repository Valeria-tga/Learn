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

#2

number=input('Enter Number: ')
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


print(f'result: {replace_nine(number)}')
