#Insertion sort is optimized for a small seqence size, similiar to
#sorting cards in a hand. Usually runs in O(n^2) time. Best case with
#partially sorted sequence.
nums = [5,2,4,6,1,3,9,7,10,8]
print(nums)
print('Sorting...')

for j in range(0,len(nums)):
    key=nums[j]
    i=j-1
    while i>=0 and nums[i]>key:
        nums[i+1]=nums[i]
        i=i-1
    nums[i+1]=key

print(nums)
