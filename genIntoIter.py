from operator import gt,lt

def as_iterator(f):
    def wrapper(max_v):
        return list(f(max_v))
        # 2 return [i for i in f(max_v)]
        # l = []
        # for i in f(max_v):
        #    l.append(i)
        #    return l

    return wrapper


@as_iterator
def gen(max_v):
    i = 0
    while i < max_v:
        i += 1
        yield i


def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    if start > stop:
        op = lambda x, y: x > y
    else:
        op = lambda x, y: x < y
    while op(i, stop):
        yield i
        i += step




def my_range2(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    if start > stop:
        op = gt
    else:
        op = lt
    while op(i, stop):
        yield i
        i += step



def my_range3(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    op = gt if start > stop else lt
    while op(i, stop):
        yield i
        i += step

# set is unque values

set([1, 2, 3]) - set([1, 2])