class RentShop():
    def __init__(self,totalbike):
        self.totalbike=totalbike

    def totalStock(self):
        print(f'total bike available at my shop is {self.totalbike}')
    def howmuchyouwant(self,q):
        self.remainingbike=self.totalbike-q
        if(q<=0):
            print('please enter positive value or greater than zero')
        elif(q>self.totalbike):
            print('please enter lesser vaue than available stock')
        else:
            print(f'the remaining bike are {self.remainingbike}')
            a=q*100
            print(f'the rent of {q} bikes are {a} rupees')

    # def price(self):
        

# obj1=RentShop(23)
# obj1.totalStock()
# obj1.howmuchyouwant(2)
# obj1.price()



while True:
    obj1=RentShop(43)
    uc=int(input('''
1-you wnat to see total stock?
2-how many bikes do you want to rent?
    '''))
    
    if(uc==1):
        obj1.totalStock()
        # break
    elif(uc==2):
        n=int(input('enter the amount'))
        obj1.howmuchyouwant(n)
        # break
    else:
        break