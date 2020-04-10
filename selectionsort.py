
def ssort(l1):
    for i in range(len(l1)-1):
        leastpos=i
        for j in range(i,len(l1)):
            if l1[leastpos]>l1[j]:
                leastpos=j
        temp=l1[i]
        l1[i]=l1[leastpos]
        l1[leastpos]=temp
        



l1=l1=[5,6,2,1,3,8,10,9,4,7]
ssort(l1)
print(l1)

                           
                

