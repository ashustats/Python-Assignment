class ashu:
    __a= 2
    def foo(self):
        print(self.__a)


class hi(ashu):
    __b=2
    def fun(self):
        print(self.__b)
obj=hi()
obj.fun()
obj.foo()

