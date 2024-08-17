class MyClass:
    def set(self, n):
        self.number = n
        print(f'Результат работы метода set: ', self.number)

A = MyClass()
A.set(100)
A.number = 200
print(A)
print(A.number)

