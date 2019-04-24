class First(object):
    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            func(*args, **kwargs)
            func(*args, **kwargs)

        return wrapper_do_twice

    def sayHi(self):
        print('Hello, my dear!')

    sayHi() = do_twice(sayHi)


class Second(object):
    u = 2

    def methodS(self):
        print('This is method from Second')


class Third(First, Second):
    name = 'Kate'

    def my_name(name):
        print(name)

    my_name().func

    def __call__(self, *args, **kwargs):
        print(self.i, args, kwargs)


#next
def my_decorator(func):
       def wrapper_func():
           print('Here we start')
           func()
           print('Here we rend')
       return wrapper_func()
def someth(self):
    print('Amd here we are')

someth = my_decorator(someth)

print(someth)

@my_decorator
def plus_one(self):
    print(1)


class Second(object):
   u = 2

   def methodS(self):
       print('This is method from Second')


class Third(First, Second):
   def __call__(self, *args, **kwargs):
       print("Hello, sir!")
       self.func(*args, **kwargs)