# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:23:33 2020

@author: CSED
"""
import numpy as np
import time
import matplotlib.pyplot as plt

time_start1 = time.clock()
mat1=np.random.randint(10,100,(500,500))
#print( mat1,mat1.shape,sep="\n")
#print(np.dot(mat1,mat1))
#run your code
time_elapsed1 = (time.clock() - time_start1)
time_start2 = time.clock()
mat2=np.random.randint(10,100,(1000,1000))
#print( mat2,mat2.shape,sep="\n")
np.dot(mat2,mat2)
time_elapsed2 = (time.clock() - time_start2)
time_start3 = time.clock()
mat3=np.random.randint(10,100,(1500,1500))
np.dot(mat3,mat3)
#print( mat3,mat3.shape,sep="\n")

time_elapsed3 = (time.clock() - time_start3)
time_start4 = time.clock()
mat4=np.random.randint(10,100,(2000,2000))
np.dot(mat4,mat4)
time_elapsed4 = (time.clock() - time_start4)
#print( mat4,mat4.shape,sep="\n")
time_start5 = time.clock()
mat5=np.random.randint(10,100,(2500,2500))
#print( mat5,mat5.shape,sep="\n")
np.dot(mat5,mat5)
time_elapsed5 = (time.clock() - time_start5)
print( "time of matrix 500* 500 is {}".format(time_elapsed1))
print( "time of matrix 1000* 1000 is {}".format(time_elapsed2))
print( "time of matrix 1500* 1500 is {}".format(time_elapsed3))
print( "time of matrix 2000* 2000 is {}".format(time_elapsed4))
print( "time of matrix 2500* 2500 is {}".format(time_elapsed5))
x=[500,1000,1500,2000,2500]
y=list([])
y.append(time_elapsed1)
y.append(time_elapsed2)
y.append(time_elapsed3)
y.append(time_elapsed4)
y.append(time_elapsed5)
plt.plot(x,y)
plt.title(" Time vs size plots")
plt.xlabel("matrix size")
plt.ylabel( " execution time in ms")
#plt.show()
plt.savefig('lineplot1.png',dpi=600,format='png')
plt.scatter(x,y)
plt.title(" Time vs size plots")
plt.xlabel("matrix size")
plt.ylabel( " execution time in ms")
#plt.show()
plt.savefig('scatterplot1.png',dpi=600,format='png')
labels=[('Size'),('Time')]
rowscsv=list([])
rowscsv.append([500,time_elapsed1])
rowscsv.append([1000,time_elapsed2])
rowscsv.append([1500,time_elapsed3])
rowscsv.append([2000,time_elapsed4])
rowscsv.append([2500,time_elapsed5])
import csv
with open('lab1.csv',mode='w') as f:
    csvwriterobj=csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriterobj.writerow(labels)
    csvwriterobj.writerows(rowscsv)
    


