n1=int(input('enter the first number you want :'))
n2=int(input('enter the second number you want:'))
def product(n1,n2):
    product=n1*n2
    if product<1000:
        return product
    else:
         return n1+n2  
result=product(n1,n2)
print(result)

