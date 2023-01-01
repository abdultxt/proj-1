list1=['chilli milli','lays','kurlees','ding dong']
a=len(list1)
total=0
while a>0:
    for i in list1:
        print((i))
        b=int(input('PRice of the item is'))
        total+=b
    print(total)
    a-=1
    break