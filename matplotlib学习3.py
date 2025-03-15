import numpy as np
import matplotlib.pyplot as plt
"""
x=np.array(['A','B','C','D'])
y=np.array([3,7,2,5])
#plt.bar(x,y)
plt.barh(x,y)#水平柱状图
#设置颜色,条形宽度,条形高度(barh水平时)
"""
#设置直方图:hist()函数用一个数字数组来创建直方图
x=np.random.normal(170,30,250)#均值170，标准差30，250个数据
print(x)
plt.hist(x)

plt.show()