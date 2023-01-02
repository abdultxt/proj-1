a=int(input('Enter any number then I will give you the factorial of it'))
total=1
while a>0:
    if(a==0):
        b=1
        total*=b
        print(total)
    b=a*1
    total*=b
    a-=1
print(total)

