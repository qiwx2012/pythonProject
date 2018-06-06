#遍历字符串
s=' I love you more than i can say'
for i in s:
    print(i)
#遍历列表
l=['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']
for i in l:
    print(i)
#遍历字典
d={'a':'apple','b':'banana','c':'car'}
for key in d:
    #遍历字典的时候遍历的是key
    print(key,d.get(key))
#第二种遍历字典方式
for key,value in d.items():
    print(key,value)

#生成[1,10]10个数
for i in range(1,10):
    print(i)
#列表生成式
print([i for i in range(1, 11)])
# 强制转换为列表
print(list(range(1, 19)))

