import random
# no.players
# loop players
# want to play
'''
roll
add tem score
add to final score
'''
# check score
# 



def roll():
    val= random.randint(1,6)
    return val

def change_player(arr:list,cur:int)->int:
    no_players=len(arr)
    if cur==no_players-1:
        cur=0
    else:
        cur+=1
    return cur


def play(cur:int,score:list):
    temp=0
    yes=True
    while yes:
        y=True
        print(f"\nplayter no. {cur+1} would you like to roll")
        print(f"youre total score = {score[cur]}\nyou temp score is {temp}")

        while True:

            Q=input("if you want to play enter 1 else 0 and to exit enter 2 ")
        
            if Q.isdigit():
                Q=int(Q)
                if Q==2:
                    yes=False
                    y=False
                    break
                if Q==0:
                    yes=False
                    break
                elif Q==1:
                    break
                else:
                    print("if you want to play enter 1 else 0 ")
            else:
                print("if you want to play enter 1 else 0 ")
        if yes==False:
            break
        r=roll()
        print(f"\nyou rolled {r}")
        if r==1:
            temp=0
            yes=False
            break
        else:temp+=r
    score[cur]+=temp
    print(f"you turn ends next player\n")
    return score[cur],y


print("wellcome to roll the dice")
while True:
    players=input("enter the no of player 2-4: ")
    if players.isdigit():
        players=int(players)
        if 1<players<5:
            break
        else:
            print("no of player can be 2 to 4")
    else:
        print("enter a no.")

score=[0 for i in range(players)]
maxScore=50
cur=0
print(f"first one to {maxScore} wins")
while True:
    n,y=play(cur,score)
    # print(y,n)
    if n>=maxScore or y!=True:
        break
    cur=change_player(score,cur)
print(f"player no {cur+1} wins with {score[cur]} points")

# 


