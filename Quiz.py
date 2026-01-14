print('Welcome to my maths quiz!')

question = input('Would you like to play? ')
if question.lower() != 'yes':                     # lower() makes sure every string is lower case
    quit()                                        # upper() makes every string capital
print("Okay! Let's play")

score = 0                         # allowing us to track the correct answers

answer = input('What is 1+1? ')
if answer == '2':
    print('correct')
    score += 1
else:
    print('wrong')

answer = input('What is 2+2? ')
if answer == '4':
    print('correct')
    score += 1
else:
    print('wrong')

answer = input('What is 3+3? ')
if answer == '6':
    print('correct')
    score += 1
else:
    print('wrong')

print('you got ' + str(score) + ' questions correct. ')
print('you got ' + str((score/3) * 100) + '%. ')
