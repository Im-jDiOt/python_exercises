N = int(input())
cards = list(range(1, N+1))

while len(cards)>1:
    new = [] 

    if len(cards)%2==0:
        for i in range(int(len(cards)/2)):
            new.append(cards[2*i+1])
        cards = new
    else:
        for i in range(int((len(cards)-1)/2)):
            new.append(cards[2*i+1])
        new.insert(0, cards[-1])    
        cards = new    

print(cards[0])
