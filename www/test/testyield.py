def yieldTest(n):
    for i in range(n):
        yield call(i)
        print('i=',i)
    #做一些其它事情
    print('do something')
    print('end.')

def call(i):
    return i*2

#使用for循环
# for i in yieldTest(5):
#       print(i,',')

def func():
    for i in range(5):
        yield i
# f =func()
for i in func():
  print(i,',')





