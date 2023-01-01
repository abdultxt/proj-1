class user():
    def __init__(self,name,age,gender):
        self.age=age
        self.gender=gender
        self.name=name
    def showdetails(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'gender is {self.gender}')


class bankcustomer(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        
        self.total_amount=0


    # def current(self):
        
    #         print(f'mcn{self.total_amount}')
    def total_money(self):
        print(f'your current balance is {self.total_amount}')

    def deposit(self,amount):
        self.total_amount=self.total_amount+int(amount)
        print(f'After deposit,you have now {self.total_amount} in your bank account')
    
    def withdraw(self,amount2):
        self.total_amount=self.total_amount-int(amount2)
        if(self.total_amount<=0):
            print('You are not able to withdraw')
        else:
            print(f'After withdraw,you have {self.total_amount} in your bank')

c1=bankcustomer('Talha',22,'Male')
c1.deposit(20)
c1.withdraw(5)
# c1.total_money()
# c1.showdetails()

            