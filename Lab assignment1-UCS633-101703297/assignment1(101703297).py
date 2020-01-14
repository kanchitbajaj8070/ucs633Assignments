# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:09:01 2020

@author: CSED
"""

import matplotlib.pyplot as plt
x=np.arange(5)+1
y=np.random.randn(5)
plt.plot(x,y,label='lineplot',color='red')
plt.scatter(x,y,label='scatter plot',color='green')
plt.title(" y vs x")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
#plt.show()
plt.savefig('example1.png',format='png')
print(x,y)
import seaborn as sns
x1=np.arange(100)+1
y1=np.random.randint(0,5,100)
sns.boxplot(y1)