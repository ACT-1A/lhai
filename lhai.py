print("==============================================")
print("              PLAYER1 VS PLAYER2              ")
print("==============================================")

print("[1] = ROCK")
print("[2] = PAPER")
print("[3] = SCISSOR")

p1 = int(input("enter player 1:"))
p2 = int(input("enter player 2:"))

if p1 == 1 and p2 == 1:
    print("DRAW!")
elif p1 == 1 and p2 == 2:
    print("player 2 wins!")
elif p1 == 1 and p2 == 3:
    print("player 1 wins!")

elif p1 == 2 and p2 == 1:
    print("player 1 wins!")
elif p1 == 2 and p2 == 2:
    print("DRAW!")
elif p1 == 2 and p2 == 3:
    print("player 2 wins!")

elif p1 == 3 and p2 == 1:
    print("player 2 wins!")
elif p1 == 3 and p2 == 2:
    print("player 1 wins!")
elif p1 == 3 and p2 == 3:
    print("DRAW!")

else:
    print("invalid code!")