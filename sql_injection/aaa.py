# coding:UTF-8
import numpy as np

a = ((1, 4), (2, 5), (6, 6))
listMap = map(list, a)  # 将多元组数据转换成列表

x = []  # 创建空列表"x"
y = []  # 创建空列表"y"
for xpoints, ypoints in listMap:  # 将列表中的数据迭代出来,创建数组x,y
    x.append(xpoints)
    y.append(ypoints)
k = 0
p = 0
j = len(a)
if k == 0:
    s1 = x[k] * (y[k + 1] - y[j - 1])
    print s1

elif k <= j-1:
    s = x[k] * (y[k + 1] - y[k - 1])
    p += s
    k += 1
    print p

 elif k == j:
    s2 = x[j - 1] * (y[0] - y[j - 2])
    print s2
Add = abs((s1 + s2 + p) / 2)
# 随着“K”值的变化，三个“if"条件逐渐满足，你把三个“if"那边修改一下，使计算出来的Add结果为“1.5”
