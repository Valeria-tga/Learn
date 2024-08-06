def max_elemt(x,y):
    if x>y: return x
    if x<y: return y
    if x==y: return 'числа одинаковые'

max=max_elemt

def main(func,number1,number2):
    return func(number1,number2)

numbers=list(input('Введите два числа через запятую: ').split(','))

number1 = int(numbers[0])
number2 = int(numbers[1])

print(main(max,number1,number2))