#python文件的执行顺序
print('test1')
def fun1():
    print('fun1')
def main():
    print('main')
if __name__=='__main__':
    fun1()

