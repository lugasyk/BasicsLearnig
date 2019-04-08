[i for i in range(50) if i % 2]
[i for i in range(50) if i % 2]
[i for i in range(50) if (i > 0) and not (i % 50)]


d = dict(a=1, b=2)

or key in d:
print(key)
a
b
for key in d.keys():
    print(key)

a
b


for k,v in d.items():
    print(k, v)

a, b = 1, 2

s.append((1, 2, 3))
s.append((2, 4, 6))
s.append((6, 7, 1))
t = '{0} + {1} + {2} = {3}'
s
[(1, 2, 3), (2, 4, 6), (6, 7, 1)]
for i in s:
    print(i)

(1, 2, 3)
(2, 4, 6)
(6, 7, 1)
for i in s:
    a, b, c = i
    print(a, b, c)

1
2
3
2
4
6
6
7
1
for i in s:
    a, b, c = i
    s = sum([a, b, c])
    print(a, b, c, s)

1
2
3
6
2
4
6
12
6
7
1
14
t.format(1, 2, 3, 4)
'1 + 2 + 3 = 4'
for i in s:
    a, b, c = i
    s = sum([a, b, c])
    print(t.format(a, b, c, s))


ss = [(1, 2, 3), (2, 3, 5), (5, 6, 7)]
for i in ss:
    a, b, c = i
    s = sum([a, b, c])
    print(t.format(a, b, c, s))

for i in ss:
    a, b, c = i
    s = sum([a, b, c])
    print(t.format(a, b, c, s))

