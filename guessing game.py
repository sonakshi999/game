import random
correct_number=random.randint(1,100)
print(correct_number)
guess_number=int(input("guess the number"))
attempt=1
while guess_number!=correct_number:
    attempt+=1
    if guess_number>correct_number:
        print("print lower")
        guess_number=int(input("enter again"))
    else:
        print("print higher")
        guess_number=int(input("enter again"))
else:
    print("correct guess, you took", attempt, "attempt")
