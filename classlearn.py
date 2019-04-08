class A(object):
    a1 = 1
    def method1(self, args, **kwargs):
        print('Hello from {}'.format(self), args, **kwargs)
class B(A):
    pass


b = B()
b.a1
1
b.method1(1)


class A(object):
    a1 = 1

    def __init__(self, *args, **kwargs):
        print("hello from init A", args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def method1(self, *args, **kwargs):
        print("hello from {}".format(self), args, kwargs)


a = A(1, b=12)


class B(A):

    def __init__(self, *args, **kwargs):
        print("Hello from B")


class C(object):
    a2 = 12

    def method2(self):
        print("This is method2 from class C")


class Z(A, C):
    pass


z = Z()


class A1(A):
    def method1(self, *args, **kwargs):
        super().method1(self, *args, **kwargs)
        self.method2()


a1 = A1()

class X(A1, C):
    pass
x = X()


class F(object):
    def __init__(self, a="aaa"):
        self.a = a

    def __call__(self, *args, **kwargs):
        print(self.a, args, kwargs)


f = F('ZZZ')
f