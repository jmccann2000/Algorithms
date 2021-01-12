# Bubble Sort algorithm on list of integers
# Speed:
#    Best:
#        Comparisons: O(n)
#        Swaps: O(1)
#    Average:
#        Comparisons: O(n^2)
#        Swaps: O(n^2)  
#    Worst:
#        Comparisons: O(n^2)
#        Swaps: O(n^2)

import matplotlib.pyplot as plt
import matplotlib.animation as anim

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def bubbleSort(array):
    for i in range(0, len(array) - 1):
        for j in reversed(range(i + 1, len(array) - 1)):
            if array[j] < array[j - 1]:
                swap(array, j, j - 1)

def altBubbleSort(array,i):
    copy=array
    j=len(array)
    while array != copy and i<j:
        if array[j] < array[j - 1]:
            swap(array, j, j - 1)
        j=j-1

def animate(array)




x = range(0, 10)
test = [5, 2, 3, 6, 7, 3, 4, 5, 2, 7]
i=0
j=len(test)
testFig = plt.figure()
plt.bar(x,test)
animation = anim.FuncAnimation(testFig,altBubbleSort,interval=50,fargs={test,i})
plt.show()
print(test)
bubbleSort(test)
print(test)
