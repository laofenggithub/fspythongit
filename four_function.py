def times(x, y):
    return x * y


x = times(3.14, 4)


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = "spam"
s2 = "scam"
print intersect(s1, s2)
print [x for x in s1 if x in s2]
x = intersect([1, 2, 3], (1, 4))
print x
# 450页
