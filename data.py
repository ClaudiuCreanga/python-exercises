import numpy as np
import math


my_aray = np.array([0,1,2,3])
#print(my_aray.dtype)
str_array = my_aray.astype(str)
#print(str_array.dtype)

dim2_array = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,4]])
#print(dim2_array.ndim)
#print(dim2_array.shape)
#print(dim2_array[:1])
#print(np.mean(dim2_array, axis = 1))

#save array as text
#np.savetxt('document.csv',dim2_array,delimiter=',')

#generate array from text
#array_from_text = np.genfromtxt('document.csv',delimiter=',')

import matplotlib.pyplot as plt
import os

#create a directory
def create_directory():
    os.makedirs(cwd+"/images")
#create_directory()

#copy files from one location to another with shutil
def copy():
    import shutil
    shutil.copy2('/Users/claudiucreanga/Dropbox/IMG_4301.jpg',cwd+"/images")
#copy()


def reds_greens_image():

    files = [f for f in os.listdir(os.getcwd()+"/images") if f.endswith(".png")]
    redperimage = []
    greperimage = []

    for file in files:
        img = plt.imread(os.getcwd()+"/images/"+file)
        reds = img[:,:,0]
        redperimage.append(np.sum(reds))
        greens = img[:,:,1]
        greperimage.append(np.sum(greens))

    redperimage = np.array(redperimage, dtype=float)
    greperimage = np.array(greperimage, dtype=float)

    ratio = redperimage / greperimage

    plt.subplot(211)

    plt.plot(range(0,len(redperimage)),redperimage,'ro')
    plt.plot(range(0,len(greperimage)),greperimage,'go')

    plt.subplot(212)
    plt.plot(range(0,len(ratio)),ratio,'ko')
    plt.show()
#reds_greens_image()

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
#print(a[:,1:])
x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
#print(x[...,0])

a = np.array([
    [[1,  2],  [3,  4]],
       [[5,  6], [7,  8]],
       [ [9, 10], [11, 12]],
       [[13, 14], [15, 16]]])
# print(a[0,...,2]) is equal to print(a[0,2])
# ... is the elypsis which is the gap that takes the number of dimensions so that the next number is the last index.

def factorial(n):
    numbers = [f for f in range(1,n+1)]
    result = reduce(lambda x,y: x*y ,numbers)
    #or
    result = reduce(lambda x,y: x*y, [1]+range(1,n+1))
    print(result)
#factorial(30)

