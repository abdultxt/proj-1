cand1=input('Enter your candidate1\n')
cand2=input('Enter your candidate2\n')
vote_id=['101','102','103','104','105']
firstcand=0
secondcand=0
reject=0
voted=[]
while True:
    print(f'You have Two candidate name as following\n{cand1} and {cand2}')
    
    for i in range(len(vote_id)):
        voter=input('Enter your id\n')
        
        if(voter in vote_id):
            a=input('Cast the vote to the candidate\n')
            if(a==cand1):
                vote_id.remove(voter)
                firstcand+=1
            elif((a==cand2)):
                vote_id.remove(voter)
                secondcand+=1
            else:
                print('Cast the vote to the correct candidate\n')
                reject+=1
        else:
            print('Your are not register')
            reject+=1
        # if(voter in voter_id):
            
        #     voted.append(voter)
        # elif(voter_id==[]):
        #     print('Voting finish')
    print(f'{cand1} has {firstcand}')
    print(f'{cand2} has {secondcand}')
    print(f'rejected vote are {reject}')
    break
