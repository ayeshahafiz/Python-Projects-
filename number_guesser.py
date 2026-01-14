import random

# r = random.randrange(1, 11)                 includes 1-10
# print(r)
# r = random.randint(0, 11)                   includes 1-11
# print(r)

guess = input('Type a number: ')

if guess.isdigit():                            # .isdigit makes sure its a number
    guess = int(guess)                         # to convert "4" to 4
    if guess <= 0:
        print('too low!')
        quit()
else:
    print('please enter a number next time')
    quit()

random_number = random.randint(0, guess)
print(random_number)

guesses = 0

while True:   # loops again and again
    guesses += 1
    user_guess = input('guess the number ')
    if user_guess.isdigit:
        user_guess = int(user_guess)
    else:
        print('type a number next time')

    if user_guess == random_number:
        print('you got it!')
        break  # breaks the loop
    elif user_guess > random_number:
        print('your number was way too large')
    else:
        print('your number was too small')


# another way to print a sentence without the +
print('you got it in', guesses, 'guesses!')
