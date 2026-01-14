master_password = input('Enter a master password? ')


def view():  # calling this function in any point of the code prints out the following:
    with open('passwords.txt', 'r') as f:  # 'r' means read only
        for line in f.readlines():
            data = line.rstrip()  # doesnt add a line space after the output runs
            user, pw = data.split('-')
            print('User:', user, 'Password:', pw)


def new():
    acc = input('Account name: ')
    password = input('New password: ')

    # with automatically closes the file. 'a' allows user to add anything to the end of a file and it makes a new file.
    with open('passwords.txt', 'a') as f:
        f.write(acc + "-" + password + "\n")


while True:  # ensures that the code is repeated again
    choice = input(
        'enter new to enter new password or view to view existing ones? enter q to quit  ')
    if choice == 'q':
        break  # breakes the while loop
    elif choice == 'view':
        view()
    elif choice == 'new':
        new()
    else:
        print('Invalid mode')
        continue
