Player1 = raw_input("Enter player1: ")
Player2 = raw_input("Enter Player2: ")
Player1 = raw_input("Player1: Choose Stone or Paper or Scissor=  ")
Player2 = raw_input("Player2: Choose Stone or Paper or Scissor=  ")
def Game():
    if Player1 == Player2:
        print("It's  a  Tie");
    elif Player1 == 'Stone':
        if Player2 == 'Scissor':
            print("Stone Wins");
        else:
            print("Paper Wins");

    elif Player1 == 'Scissor':
        if Player2 == 'Paper':
            print("Scissor Wins");
        else:
            print("Stone Wins");


    elif Player1 == 'Paper':
        if Player2 == 'Stone':
            print("Paper Wins");
        else:
            print("Scissor Wins");

    else:
        print("Enter valid option from Stone, Paper, Scissor");


Game()