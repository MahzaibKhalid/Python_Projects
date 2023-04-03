import random
num = random.randrange(1,10)
count=1
guess= int(input("Enter any Number:"))
while num!=guess:
    count+=1
    if guess < num:
        print("Guess is Low")
        guess  = int(input("Enter a Number:"))
    elif guess > num:
        print("Guess is High")
        guess  = int(input("Enter a Number:"))
    else:
        break

print("Your guess is correct")
print("Your guess the answer in ",count,"attempts")

