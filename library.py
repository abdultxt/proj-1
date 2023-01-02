class Library():
    def __init__(self,name,listitem):
        self.name=name
        self.listitem=listitem
        self.lendDict={}

    def displayBook(self):
        print(f'you have the following books in {self.name}')
        for i in self.listitem:
            print(i)
        print(self.listitem)
    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            if user not in self.lendDict.values():
                self.lendDict.update({book:user})
                print('Congrats')
                print(self.lendDict)
                self.listitem.remove(book)
                print(self.listitem)
            else:
                print('One Person pick one book at a time')
        else:
            print('Not available')

    def addbook(self,bookname):
        self.listitem.append(bookname)
        print((self.listitem))
    

    def returnbook(self,book):
        self.listitem.remove(book)
        print(self.listitem)

while True:
    user_choice=int(input('''
    1-Display Books
    2-Lend Book
    3-Add Book
    4-Return Book
    'press q to quit'
    '''))
    l1=Library('TalhaLibrary',['Faster way to learn Python','Java','Javascript','C++','C'])
    if(user_choice==1):
        l1.displayBook()
    elif(user_choice==2):
        while True:
            user=input('Enter your name')
            book=input('Enter a book')
            l1.lendbook(user,book)
            a=input('press q to exit')
            if(a=='q'):
                break
    elif(user_choice==3):
        for i in range(0,1):
            a=input('enter a book you want to add in the library')
            l1.addbook(a)
    elif(user_choice==4):
        a=input('Enter a book you want to return')
        l1.returnbook(a)
    else:
        if(user_choice=='q'):
            break
