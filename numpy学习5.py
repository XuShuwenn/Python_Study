import numpy as np
from numpy import random
import matplotlib.pyplot as plt
#1.二项分布
x=random.binomial(n=10,p=0.5,size=10)#n表示试验次数，p表示概率
print(x)
#2.泊松分布
#泊松分布与指数分布的关系：泊松分布是指数分布的一个特例，即当n趋于无穷大时，泊松分布就是指数分布
#泊松分布处理的是单位时间内随机事件发生的次数，而指数分布处理的是事件发生的时间间隔
x=random.poisson(lam=2,size=10)#lam表示事件发生率
print(x)
#3.正态分布
x=random.normal(loc=0,scale=1,size=10)#loc表示均值，scale表示标准差，size表示数组形状
print(x)
#4.均匀分布
x=random.uniform(size=10)
print(x)
#5.logistic分布
#logistic分布是一个连续概率分布，它的形状类似于正态分布，但是它有更重的尾巴
x=random.logistic(loc=0,scale=1,size=10)#loc表示均值，scale表示标准差，size表示数组形状
print(x)
#6.多项分布
x=random.multinomial(n=6,pvals=[0.1,0.2,0.3,0.4])
print(x)
#7.指数分布
x=random.exponential(scale=2,size=10)
print(x)
#8.卡方分布
x=random.chisquare(df=2,size=10)
print(x)
#9.伽马分布
x=random.gamma(shape=2,scale=2,size=10)
print(x)
#10.贝塔分布
x=random.beta(a=2,b=2,size=10)
print(x)
#11.拉普拉斯分布
x=random.laplace(loc=0,scale=1,size=10)
print(x)
#12.对数正态分布
x=random.lognormal(mean=0,sigma=1,size=10)
print(x)
#13.雷利分布（适用于 非负数据，用于描述随机向量的模长分布）
#雷利分布是一个连续概率分布，用于描述二维随机向量的长度
x=random.rayleigh(scale=2,size=10)
print(x)
#14.威布尔分布（Weibull Distribution）是一种常见的概率分布，用于表示生存时间数据。
#常用于可靠性分析、寿命建模、气象学、地震学等领域
x=random.weibull(a=1,size=10)
print(x)
#15.帕累托分布
#帕累托分布（Pareto Distribution）是一种概率分布，用于描述社会现象中的不平等现象（二八定律）
x=random.pareto(a=2,size=10)
print(x)
#16.拉兹夫分布
#拉兹夫分布（Laplace Double Exponential Distribution）是一个双峰连续概率分布
x=random.gumbel(loc=1,scale=1,size=10)
print(x)
#17.标准t分布
x=random.t(loc=0,scale=1,size=10)
print(x)
#18.半正态分布
#半正态分布（Half Normal Distribution）是一个正态分布的子集，其中所有值都是正的
x=random.halfcauchy(size=10)
print(x)
#19.瓦尔德分布
#瓦尔德分布（Wald Distribution）是一个连续概率分布，它是一个正态分布的逆
x=random.wald(mean=1,scale=2,size=10)
print(x)