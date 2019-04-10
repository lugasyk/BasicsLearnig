class First(object):
    def __init__(self, function):
        print("Hello, I'm here")
        self.function = function

    def methodF(self, *args, **kwargs):
        print('Hello from {}'.format(self), args, kwargs)


class Second(object):
    u = 2

    def methodS(self):
        print('This is method from Second')


class Third(First, Second):
    def __call__(self, *args, **kwargs):
        print("Hello, sir!")
        self.function(*args, **kwargs)

