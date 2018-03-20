# TempConvert.py
'''TempStr = input("please input temperature value: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("After convert value is {:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("After convert value is {:.2f}F".format(F))
else:
    print("error format!")


print("88"*8)
print(88*8)

TempStr = input()
if TempStr[0:3] in ['RMB']:
    RMB = eval(TempStr[3:]) / 6.78
    print("USD{:.2f}".format(RMB))
elif TempStr[0:3] in ['USD']:
    USD = eval(TempStr[3:]) * 6.78
    print("RMB{:.2f}".format(USD))

TempStr = input()
if TempStr[-1] in ['m']:
    _in = eval(TempStr[0:-1]) *39.37
    print("{:.3f}in".format(_in))
elif TempStr[-2:] in ['in']:
    _m = eval(TempStr[0:-2]) /39.37
    print("{:.3f}m".format(_m))
    '''
# turtle.pancolor("black")
import turtle,time
turtle.screensize()
'''
for i in range(1,5):
    turtle.circle(10*i)
'''
for i in range(9):
    turtle.forward(100)
    turtle.left(80)
time.sleep(3)