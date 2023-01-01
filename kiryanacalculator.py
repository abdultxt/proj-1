
sum=0
while True:
    a=(input('Enter the price of the item'))
    if(a=='q'):
        break
    else:
        sum+=int(a)
print(f'the total amount of the shopping is {sum}')
    
