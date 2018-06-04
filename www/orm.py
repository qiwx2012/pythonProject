import asyncio,logging
import aiomysql

# 定义一个log方法
def log(sql,args=()):
    logging.info('SQL:%s' % sql)

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        chartset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit','True'),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
#定义执行函数
@asyncio.coroutine
def execute(sql,args):
    log(sql)
    with (yield __pool) as conn:
        try:
            cur=yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected=cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected

#Select
@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with( yield from __pool) as conn:
        cur= yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or())
        if size:
            rs=yield from cur.fetchmany(size)
        else:
            rs=yield from cur.fetchall()
        yield from cur.close()
        logging.info('row returned: %s' % len(rs))
        return rs



