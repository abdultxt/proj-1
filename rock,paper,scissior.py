import random
comp=['Rock','Scissor','Paper']
youwin=0
compwin=0
while True:
    for i in range(1,6):
        print('Rock','Scissor','Paper')
        user=(input('Enter your choice'))
        
        print(f'user chose {user}')
        computer=random.choice(comp)
        print(f'computer chose {computer}')
    
        if(user==computer):
            print('Draw')
        elif((user=='Rock' and computer=='Scissor') or (user=='Paper' and computer=='Rock') or (user=='Scissor' and computer=='Paper')):
            youwin+=1
            print('User win')
        else:
            compwin+=1
            print('Computer win')
    print(f'Computer wins {compwin} times')
    print(f'User wins {youwin} times')
    a=input('Press Yes to play more and press anykey to exit the game')
    if(a=='Yes' or a=='yes' or a=='YES'):
        continue
    else:
        break