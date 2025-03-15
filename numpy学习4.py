import numpy as np
from numpy import random
#数据分布
#1.生成随机数据
#伪随机数：随机数生成器的种子（通过生成算法生成的随机数，可以预测）
#真随机数：通过物理过程生成的随机数（通过外部数据获取，无法预测）
x=np.random.normal(170,10,250)#均值170，标准差10，250个数据
print(x)
y=np.random.rand(100)#浮点数
print(y)
z=np.random.randint(100,size=(6))#0-1之间的随机数组
print(z)
#用choice()方法基于给定的数组生成随机数据
arr=np.array([1,2,3,4,5])
newarr=np.random.choice(arr,size=(3,2),replace=True)#replace=True表示可以重复抽取
print(newarr)
#2.数据分布可视化
import matplotlib.pyplot as plt
#分布图distplot,直方图histplot,核密度估计kdeplot,拟合图fitplot
import seaborn as sns
#sns.distplot([0,1,2,3,4,5])
#plt.show()
x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(x)
#随机排列组合
arr=np.array([1,2,3,4,5])
newarr=random.permutation(arr)#返回一个新数组，为对原数组进行随机排列的结果（原数组保持不变）
print(newarr)
random.shuffle(arr)#对原始数组洗牌，即重新排列（改变原数组）
print(arr)