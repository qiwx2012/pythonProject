import www.orm as orm
from www.models import User,Blog,Comment
import time
import asyncio
import aiomysql
import sys


# def test(loop):
#   yield from orm.create_pool(loop=loop,user='root', password='123456', db='python_db')
#   u =  User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#   yield from u.save()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()

if __name__ == "__main__":

    # 创建异步事件的句柄
    loop = asyncio.get_event_loop()


    # 创建实例
    @asyncio.coroutine
    def test():
        yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='123456', db='python_db')
        user = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank',admin=True)
        yield from user.save()
        r = yield from User.find('11')
        print(r)
        r = yield from User.findAll()
        print(1, r)
        r = yield from User.findAll(id='12')
        print(2, r)
        yield from orm.destroy_pool()


    loop.run_until_complete(test())
    loop.close()
    if loop.is_closed():
        sys.exit(0)