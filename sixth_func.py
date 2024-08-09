def func(x):
    return 2*x

def main(f, x):
    n=6
    def calc(n):
        return n*(f(x))
    return calc(n)

# print(main(func,6))


