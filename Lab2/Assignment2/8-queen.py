state = [6,1,5,7,4,3,8,1]

attacking_pair = 0

i = 0
while(i<8):
    j = i+1
    while(j<8):
        if(state[i] == state[j]):  #checking horizontal similarity
            attacking_pair = attacking_pair + 1
        j = j+1

    j = i+1
    k = 1
    while(j<8):
        if( (state[i]+k) == state[j]):  #checking diagonal up
            attacking_pair = attacking_pair + 1
        j = j+1
        k = k+1

    j = i+1
    k = 1
    while(j<8):
        if( (state[i]-k) == state[j]):  #checking diagonal down
            attacking_pair = attacking_pair + 1
        j = j+1
        k= k+1

    i = i+1

print(attacking_pair)
