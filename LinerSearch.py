l1=[22,2,4,5,6,8,9]
j=0
n=int(input("enter the number u want to b searched:"))
for i in range(len(l1)):
    if l1[i] == n:
        globals() ['j']=i
        print("the position of number  is" , j+1)
    elif n!=l1[i]:
        print('element not found')
        break
