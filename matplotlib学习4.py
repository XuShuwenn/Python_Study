import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

#创建饼图，使用标签label参数
x=np.array([35,25,25,15])
mylabels=['苹果','香蕉','樱桃','橙子']
plt.pie(x,labels=mylabels)
plt.legend()
plt.show()

