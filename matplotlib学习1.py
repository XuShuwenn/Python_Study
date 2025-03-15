import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 1.为绘图创建标签
# 2.为绘图创建标题
# 3.为绘图创建网格
matplotlib.rcParams['font.sans-serif']=['KaiTi']
xpoints=np.array([80,85,90,95,100,105,110,115,120,125])
ypoints=np.array([240,250,260,270,280,290,300,310,320,330])
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.title("运动手表数据",fontdict=font1)
plt.xlabel("平均脉搏",fontdict=font2)
plt.ylabel("卡路里消耗量",fontdict=font2)

plt.plot(xpoints,ypoints)
#plt.grid(axis='x')显示x轴网格
#plt.grid(axis='y')显示y轴网格
plt.grid()
plt.show()

"""
1.连线绘图plt.plot(xpoints,ypoints)
2.无线绘图plt.plot(xpoints,ypoints,'o')

3.多点绘图
xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])
plt.plot(xpoints,ypoints)
plot.show()

4.默认x点绘图:[1,2,3,4]

5.点参考,线参考,颜色参考,标记尺寸markersize/ms
6.还可设置格式化字符fmt:marker|line|color
eg. plt.plot(xpoints,ypoints,'o:r')

7.线型linestyle/ls
eg. plt.plot(xpoints,ypoints,linestyle='dashed')
线条颜色color
eg. plt.plot(xpoints,ypoints,color='r')
线条宽度linewidth/lw
eg. plt.plot(xpoints,ypoints,linewidth='20.5')
标记尺寸markersize/ms

"""