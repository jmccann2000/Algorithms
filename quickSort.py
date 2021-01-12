import random as rnd
import matplotlib.pyplot as plt

#Quick Sort algorithm on list of integers
#
#The partitioner function has been modified
#to allow the sorting algorithm to be graphed.
#
#Speed:
#    Best: O(nlog(n))
#    Average: O(nlog(n))
#    Worst: O(n^2)

def moveToFront(list,front,x):
    frontVal = list[front]
    xVal = list.pop(x)
    list.insert(front,xVal) 

def partition(list , start, stop):

    partitioner = list[start]
    partitionPos = start
    leftStart = start
    rightStop = stop
    print("Itteration for: ", start , "to", stop)

    while rightStop -leftStart >= 0 and partitionPos != stop:
        print(leftStart)
        elem = list[leftStart]
        if elem <= partitioner:
            moveToFront(list,start,leftStart)

            plt.bar(x,list,width = 0.1)
            plt.show()

            partitionPos += 1

        leftStart+=1
    return partitionPos

def quickSort(list, start, stop):
    testList = list[:]
    testList.sort()
    if stop -start > 0:
        partitionPos = partition(list, start,stop)

        quickSort(list, start, partitionPos-1)
        quickSort(list, partitionPos+1, len(list)-1)




y = []
for i in range(20):
    n = rnd.randint(1,20)
    y.append(n)

x = range(0,len(y))

quickSort(y,0,len(y)-1)
