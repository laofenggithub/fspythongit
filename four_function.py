# edcoding=utf-8
# import __builtin__
#
#
# def times(x, y):
#     return x * y
#
#
# x = times(3.14, 4)
#
#
# def intersect(seq1, seq2):
#     res = []
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#     return res
#
#
# s1 = "spam"
# s2 = "scam"


# print intersect(s1, s2)
# print [x for x in s1 if x in s2]
# x = intersect([1, 2, 3], (1, 4))
# print x
# 450页 test
# print dir(__builtin__)

# x=88
# def func():
#     global x
#     x=99
# func()
# print x

# def func():
#     x = 4
#     action = (lambda n: x ** n)
#     return action
#
# #
# def func():
#     x = 4
#     action = (lambda n, x=x: x ** n)
#     return action
#
#
# x = func()
# print(x(2))
# def makeActions():
#     acts = []
#     for i in range(5):
#         # acts.append(lambda x:i**x) 嵌套作用域中的变量在嵌套的函数被调用时才进行查找
#         acts.append(lambda x, i=i: i ** x)
#     return acts
#
#
# acts = makeActions()
# print acts[0](2), acts[2](2), acts[4](2)

# python3 def tester(s):
#     state = s
#         def nested(label):
#         nonlocal state
#         print(label,state)
#         state+=1
#     return nested
# F = tester(0)
# F("aaa")
# F("bbb")
# python2.x的做法
# def tester(s):
#     global state
#     state = s
#
#     def nested(label):
#         global state
#         print(label, state)
#         state += 1
#
#     return nested
# F = tester(0)
# F("aaa")
# F("bbb")
# 类de解决方法
# class tester:
#     def __init__(self, start):
#         self.state = start
#
#     def nested(self, label):
#         print(label, self.state)
#         self.state += 1
#
# F = tester(0)
# F.nested('spam')
# F.nested('bbb')
# G = tester(42)
# G.nested('aaa')
# G.nested('ccc')
# print F.state
# print G.state

# 使用函数属性实现与nonlocal相同的效果，函数名nested是包围nested的tester作用域的一个本地变量
# def tester(s):
#     def nested(label):
#         print(label,nested.state)
#         nested.state +=1
#     nested.state = s
#     return nested
# F = tester(0)
# F('spam')
# F('bbb')
# G = tester(42)
# G('aaa')
# G('ccc')
# print F.state
# print G.state

# 类型属于对象，而不是变量名
# 分片 [:] 从头到尾的分片，就是一个拷贝

# 参数
# def f(*args):print(args)
# f()
# f(1)
# f(1,2,3,4)
# def f(**kwargs):print(kwargs)
# f()
# f(a=1,b=2)
# def f(a,*args,**kwargs):print(a,args,kwargs)
# f(1,2,3,x=1,y=2)
# 解包参数
# def f(a, b, c, d): print(a, b, c, d)
# args = (1, 2)
# args += (3, 4)
# f(*args)
# kwargs={'a':1,'b':2,'d':4}
# kwargs['c']=3
# f(**kwargs)
# f(*(1,2),**{'d':3,'c':4})
# f(1,*(2,3),**{'d':4})
# f(1,d=3,*(2,),**{'c':4})
# f(1,*(2,4),d=3)
# f(1,*(2,),c=3,**{'d':4})
# 第三部分，section 11
# L = [1, 2, 3, 4]
# while L:
#     # front, L = L[0], L[1:]
#     front = L.pop(0) # 原处修改
#     print(front, L)
# seq = [1, 2, 3, 4]
# a, *b = seq
# a, b, c, d, *e = seq
# print(e)
# L=[1,2,3]
# L.append([4,5])
# L.extend([6,7])
# L.extend({1,2}) #set 无序，没value只有key的dict
# print(L)
# print(type({1.2:1,2:2}[1.2]))
# 增强赋值是做原处修改的
# L=[1,2]
# M = L
# L = L+[3,4]
# print(L,M)
# L=[1,2]
# M=L
# L+=[3,4]
# print(L,M)
# L=[1,2]
# M = L
# L[len(L):] = [11,12,13] #L.extend([11,12,13])也是原处修改
# print(L,M)
# x=print('spam')
# print(x)
L = [1,2]
L.append(3)
print(L)
L = L.append(4)
print(L)
# x='spam'
# y=99
# z=['eggs']
# print(x,y,z,sep='...',file=open('data.txt','w'))
# text = '%s: %-.4f,%05d' % ('Result',3.14159,42)
# print(text)
# print('%s: %-.4f,%05d' % ('Result',3.14159,42))
# python2.6 's print
# x = 'a'
# y = 'b'
# print x,y
# print x,y,;print x,y
# print >> open('data2.6.txt','w'), x,y
# import sys
# sys.stdout.write('hello\n')
# import sys
# sys.stderr.write("bb"*20)
# import sys
# x=1;y=2
# print(x,y)
# sys.stdout.write(str(x)+' '+str(y)+'\n')
# open('temp2','w').write(str(x)+' '+str(y)+'\n')
# print(open('temp2','rb').read()) #python3显示的与2不一样
# from __future__ import print_function
# print('%s %s %s' % ('spam','bb','cc'))
# print('{0} {1} {2}'.format('spam','bb','cc'))
# 伪代码
# class FileMaker:
#     def write(self,string):
#         pass #do something
# import sys
# sys.stdout = FileMaker()
# print('something')
# myobj = FileMaker()
# print('something',file=myobj)
# print >> myobj,'something'
# a = raw_input() #python2.7
# sys.stdin