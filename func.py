def addition(**dan):
     return print('this function is used to add the numbers and my first number is {}'.format(dan['num1']))
     #return sum(dan)'
addition(num1=10,num2=20)
def fruits(*chin,**china):
    return print('the argument from chin is {} and argument from china is {} '.format(chin[0],china['fruit1']))
fruits(11,12,13,14,15,fruit1='strawberry',fruit2='blackberry')
    