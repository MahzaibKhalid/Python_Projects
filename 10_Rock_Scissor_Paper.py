import random

player1=input("Select Rock, Paper or Scissor: ").lower()
player2= random.choice(['Rock','Scissor','Paper']).lower()
print("Player 2 Selected:",player2)
if player1 == 'rock' and player2 == 'paper':
    print("Player 2 Won!")
elif player1 == 'paper' and player2 == 'scissor':
    print("Player 2 Won!")
elif player1 == 'scissor' and player2 == 'rock':
    print("Player 2 Won!")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won!")