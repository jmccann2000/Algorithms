import matplotlib.pyplot as plt
import quickSort as qs

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
y = [5,2,4,7,9,4,2,2,5,7,9,23,2,75,8,5,42,5,46,15,18,25,43,4,75,43]
plt.bar(x,y,width = 0.1)
plt.show()
qs.quickSort(y)
plt.bar(x,y,width = 0.1)
plt.show()
