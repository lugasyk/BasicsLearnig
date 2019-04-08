class First(object):
    i1 = 2
    i2 = 5
    def __init__(self, *args, **kwargs):
        print('Hello from init First', args, kwargs)

    def methodF(self, *args, **kwargs):
        print('Hello from {}'.format(self), args, kwargs)

class Second(object):
    u = 2
    def methodS(self):
        print('This is method from Second')

class Third(First, Second, object):
    def __index__(self, i = 9):
        self.i1 = i

    def __call__(self, *args, **kwargs):
      print(self.i, args, kwargs)

