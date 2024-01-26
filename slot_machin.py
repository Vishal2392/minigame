import random
def spin():
    line=["A","B","C"]
    current_spin=[str(random.choice(line)),str(random.choice(line)),str(random.choice(line))]
    return current_spin

# spin()

def deposit()->int:
    while True:
        amount=input("enter the amount you would like to deposit: ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("enter a no bigger than 0")
        else:
            print("please enter a no.")
    return amount

credit=deposit()

while credit>=1:
    print(f"your current credit is {credit}")
    while True:
        bet=input("how much would you like to bet")
        if bet.isdigit():
            bet=int(bet)
            if bet>0 and bet<=credit:
                break
            elif bet==0:
                break
            else:
                print("enter a no in range of you credit")
        else:
            print("please enter a no.")
    if bet==0:
        break
    credit-=bet
    roll=spin()
    print(roll)
    if roll[0]==roll[1]==roll[2]:
        credit+=bet*2
        print(f"your bet has been increased to {bet*2} and deposited and now you credit is {credit}\n")
    elif roll[0]=="A"and roll[1]=="B" and roll[2]=="C":
        credit+=bet*1.5
        print(f"your bet has been increased to {bet*1.5} and deposited and now you credit is {credit}\n")
    else:
        print("you lost the bet\n")
print("thank you for playing")