from random import randint
answer = randint(1, 100)
count = 0
while True:
    try:
        guess = int(input("Guess my number (from 1 to 100):"))
    except:
        print("Invalid input, try it again!")
    else:
        count += 1
        if guess == answer:
            break;
        elif guess > answer:
            print("Too large, try it again!")
        else:
            print("Too small, try it again!")
print(f"Bingo! You got it with {count} tries!")
