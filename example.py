class A(object):
    def __init__(self, value):
        self.value = value


class A(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


a1 = A(1)
a2 = A(1)
a1 is a2
False
id(a1) == id(a2)
False
a1 == a2
True


class B(object):
    def __getattr__(self, name):
        print(name)


b = B()
b.s
s


class MegaDict(dict):
    def __getattr__(self, name):
        return self[name]


d = MegaDict(s=1, b=12)
d['s']
1
d['b']
12
d.s
1