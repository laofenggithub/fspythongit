#TempConvert.py
TempStr = input("please input temperature value: ")
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