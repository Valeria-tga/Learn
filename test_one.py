#1

# def age():
#     now_year=int(input('Enter current year: '))
#     birth_year=int(input('Enter year of your birthday: '))
#     return now_year-birth_year
#
# print("Your age: ", age())


#2

# def dist():
#     dist_miles=int(input('Enter distance in miles: '))
#     dist_kilometer=dist_miles*1.6
#     return dist_kilometer
#
# print('Distance in kilometer is: ', dist())

#3

# def fun_degree_two():
#     count=int(input("Enter range list: "))
#     list_degree_two=[2**k for k in range(0,count)]
#     return list_degree_two
#
# print(fun_degree_two())


#4

# def fun_rest_free():
#     count=int(input("Enter range list: "))
#     list_rest_free=[5*k+3 for k in range(0,count)]
#     return list_rest_free
#
# print(fun_rest_free())


#5

def factorial():
    factorial = int(input("Enter number: "))
    if factorial < 0:
        return 'You enter negative number!'
    else:
        result,res = 1,1
        str_res = ''.join(str(k*result) for k in range(1,factorial+1))
        for k in range(1,factorial+1):
            res = res*k
        return [str(factorial)+'!', str_res, res]

lis=factorial()

print('Factorial of number ', lis[0], 'is', lis[1], '=', lis[2])