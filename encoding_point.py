# edcoding=utf8

# reload(sys)
# sys.setdefaultencoding('utf8')
#
# s5 = '字节串str'
#
# s5.encode('utf8')
#等价于
# s5.decode('系统编码').encode('utf8')
import sys
print sys.getdefaultencoding()  # 输出ascii

s = u'华南理工大学'
print s[-2:] == '大学'   # 返回False，并有warning提醒
# 自动用系统默认编码帮第二个操作符decode。
reload(sys)# 这里需要重新加载sys的原因是：python在加载模块时候删除了sys中的setdefaultencoding方法（可能是处于安全起见），所以需要reload这个sys模块。
sys.setdefaultencoding('utf8')

print s[-2:] == '大学'  # 返回True

# 查看文件编码
#
# import chardet
# with open(filename,'r') as f:
#     data = f.read()
#     return chardet.detect(data)


# 1. ascii, unicode, utf8
#
#   ascii码：最早的编码，只有127个字符，包含英文字母，数字，标点符号和一些其它符号。一个字节表示一个字符。
#
#   unicode（统一码）：一个字节不够放，全世界有各种语言的字符需要编码，于是unicode给所有的字符都设定了唯一编码。通常都是用两个字节表示一个字符（有些生僻的字要用四个字节）。所以，要理解一点：下文中提到到的unicode编码是双字节编码（一个字符两个字节）。
#
#   uft8：对于ascii编码的那些字符，只需要1个字节，unicode给这些字符也设定2个字节，如果一篇文章全是英文（ascii字符），就浪费了很多空间（本来1个字节可以存储的，用了2个字节），所以产生了utf8。utf8是一种变长的编码方式，根据不同的符号变化字节长度，把ascii编码成1个字节，汉字通常编码成3个字节，一些生僻的字符编码成4~6个字节。

s1 = '字节串'
print type(s1) #输出　<type 'str'>，按照开头的encoding来编码成相应的字节。
print len(s1) #输出9，因为按utf8编码，一个汉字占3个字节，3个字就占9个字节。

s2 = u'统一码'
print type(s2) #输出　<type 'unicode'>，用unicode编码，2个字节1个字符。
print len(s2) #输出3，unicode用字符个数来算长度，从这个角度上看，unicode才是真正意义上的字符串类型


s = '机器学习'
print s[-2:] == '学习' # 返回false，平时写程序可能会以为相等

s = u'机器学习'
print s[-2:] == u'学习' # 返回true，这也是为什么说unicode是真正意义上的字符串类型
# 这两个方法就是在unicode和str之间用指定编码进行转换。
s3 = u'统一码'.encode('utf8')
print type(s3) # 输出　<type 'str'>

s4 = '字节串'.decode('utf8')
print type(s4) #输出　<type 'unicode'>

# encode的不正常使用：对str类型进行encode，因为encode需要的是unicode类型，这个时候python会用默认的系统编码decode成unicode类型，再用你给出编码进行encode。（注意这里的系统编码不是开头的encoding，具体例子见下文第5点）
#
# decode的不正常使用：对unicode类型进行decode，python会用默认的系统编码encode成str类型，再用你给出的编码进行decode。

