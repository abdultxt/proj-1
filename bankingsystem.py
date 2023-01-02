class bankcustomer():
    def __init__(self,name):
        self.name=name
        self.total_amount=0


    # def current(self):
        
    #         print(f'mcn{self.total_amount}')
    def total_money(self):
        print(f'your current balance is {self.total_amount}')

    def deposit(self,amount):
        self.amount=amount
        self.total_amount=self.total_amount+self.amount
        print(f'After deposit,you have now {self.total_amount} in your bank account')
    
    def withdraw(self,amount2):
        self.amount2=amount2
        self.total_amount=self.total_amount-self.amount2
        if(self.total_amount<=0):
            print('You are not able to withdraw')
        else:
            print(f'After withdraw,you have {self.total_amount} in your bank')

while True:
    
    # c1=bankcustomer('Talha',10)
    # # c1.current()
    # c1.total_money()
    # c1.deposit(10)
    # c1.withdraw(30)
    a=input('''
    1-You want to see the current balance?
    2-You want to deposit the amount?
    3-You want to withdraw the amount?
    press 'q' to exit the program
    ''')
    c1=bankcustomer('Talha')
    if(a=='1'):
        c1.total_money()

    elif(a=='2'):
        dep=int(input('How much amount do you want to deposit?'))
        c1.deposit(dep)
    elif(a=='3'):
        withd=int(input('how much amount do you want to withdraw?'))
        c1.withdraw(withd)
    else:
        if(a=='q'):
            break
    
    