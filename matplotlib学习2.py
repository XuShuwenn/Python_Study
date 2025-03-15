#使用subplots函数,创建一个figure对象和一个子图对象
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
#散点图plt.scatter(x,y)
#支持颜色/尺寸/透明度：给每个点指定颜色和尺寸
colors=np.random.randint(100,size=(100))
sizes=10*np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')#颜色图谱
plt.colorbar()#显示颜色条
plt.show()
