import random

num = random.randint(0, 100);

guess = input("Please guess the number (between 0 - 100):")
guess = int(guess)
time = 0;

while True:
    time += 1
    if guess < num:
        guess = input("Too small, try it again:")
        guess = int(guess)
    elif guess > num:
        guess = input("Too big, try it again:")
        guess = int(guess)
    else:
        break

print(f"Bingo, you got it in {time} try(tries)!")