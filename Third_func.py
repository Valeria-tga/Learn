
def show(*val):
    print(type(val))
    print('Аргумент: ',val)
    print(val[1])

# print(show(1,2,3,['qwerty']))

#3

def ave_max_min(*val):
    ave,min,max=0,0,0
    for i in val:
        ave=ave+i
        if min>i:
            mim=i
        if max<i:
            max=i
    print(f'sum value = {ave}')
    ave=ave/len(val)
    return ave,min,max

result=ave_max_min(1,2,3,4,5,6,7)

print(f'average result = {result[0]} \nmin result = {result[1]} \nmax result = {result[2]}')
