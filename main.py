import string 
import random

characters = list(string.ascii_letters + string.digits + "!¡@#$%&*()^¿?")

def generate_password():
    password_length = int(input('How long would you like your password to be?'))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)

    print('Your password is: ' + password)

option = input('Do you want to generate a password? (y/n)')

if option == 'y' or option == 'Y':
    generate_password()
elif option == 'n' or option == 'N':
    print('Program ended.')
    quit()
else:
    print('Invalid input.')
    quit()