print("Welcome to Tic Tac Toe")
def game_on(lst):
    print("   TIC TAC TOE")
    print("_________________")
    print("|| " + str(lst[0]) + " || " + str(lst[1]) + " || " + str(lst[2]) + " ||")
    print("|| " + str(lst[3]) + " || " + str(lst[4]) + " || " + str(lst[5]) + " ||")
    print("|| " + str(lst[6]) + " || " + str(lst[7]) + " || " + str(lst[8]) + " ||")
    print("'''''''''''''''''")


name1 = input("Enter the name of player 1")
name2 = input("Enter the name of player 2")

print("TIC TAC TOE")
print("_________________")
print("|| 1 || 2 || 3 ||")
print("|| 4 || 5 || 6 ||")
print("|| 7 || 8 || 9 ||")
print("'''''''''''''''''")
lst=["_","_","_","_","_","_","_","_","_"]
used=[]
running = True
while running:

    game_on(lst)
    #Player1 chance
    player1_choice=int(input("Enter number 1-9 for choosing to fill X"))-1
    if lst[player1_choice]=="_":
        lst.pop(player1_choice)
        lst.insert(player1_choice,"X")
    else:
        print("Already taken choice")
    game_on(lst)

    #Player2_chance
    player2_choice = int(input("Enter number 1-9 for choosing to fill O")) - 1
    if lst[player2_choice] == "_":
        lst.pop(player2_choice)
        lst.insert(player2_choice, "0")
    else:
        print("Already taken choice")
    game_on(lst)

    if lst[0]==lst[1] and lst[1]==lst[2]:
        if lst[0]=="X":
            print("Player 1 wins")
            running = False
        elif lst[0]=="O":
            print("Player 2 wins")
            running = False

    elif lst[3]==lst[4] and lst[4]==lst[5]:
        if lst[3]=="X":
            print("Player 1 wins")
            running = False
        elif lst[3]=="O":
            print("Player 2 wins")
            running = False
    elif lst[6]==lst[7] and lst[7]==lst[8]:
        if lst[6]=="X":
            print("Player 1 wins")
            running = False
        elif lst[6]=="O":
            print("Player 2 wins")
            running = False
        else:
            print("Draw")     
 

    elif lst[0] == lst[3] and lst[3] == lst[6]:
        if lst[0] == "X":
            print("Player 1 wins")
            running = False
        elif lst[0] == "O":
            print("Player 2 wins")
            running = False

    elif lst[1] == lst[4] and lst[4] == lst[7]:
        if lst[1] == "X":
            print("Player 1 wins")
            running = False
        elif lst[1] == "O":
            print("Player 2 wins")
            running = False
    elif lst[2] == lst[5] and lst[5] == lst[8]:
        if lst[6] == "X":
            print("Player 1 wins")
            running = False
        elif lst[6] == "O":
            print("Player 2 wins")
            running = False
        else:
            print("Draw")   
    lol = 0
    for i in lst:
        if i == "_":
            lol += 1

    if lol == 0:
        running=False
