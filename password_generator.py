import time
import random

random.seed(int(time.strftime('%S')))


LETTERS = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_letters = ['@', '#', '%', '^', '&', '*', '(', ')']

try:

    password_length = int(input("Enter Length of the Password: "))
    total_numbers_in_password = int(input("How many numbers you want in password: "))
    special_characters_in_password = int(input("How many special characters you want in password: "))

    while(True):
        if(total_numbers_in_password > password_length):
            print(f"Numbers:{total_numbers_in_password} Out Of Range ")
            total_numbers_in_password = int(input("How many numbers you want in password: "))
        elif(special_characters_in_password > password_length or total_numbers_in_password + special_characters_in_password > password_length):
            print(f"Special Character:{special_characters_in_password} Out Of Range ")
            special_characters_in_password = int(input("How many special characters you want in password: "))
        else:
            break
        
    number_of_letters_in_password = special_characters_in_password-total_numbers_in_password

    password = ""
    if total_numbers_in_password > 0:
        for i in range(0,total_numbers_in_password):
            password+=NUMBERS[random.randint(0,len(NUMBERS)-1)]

    if special_characters_in_password > 0:
        for i in range(0,special_characters_in_password):
            password+=special_letters[random.randint(0,len(special_letters)-1)]
            
    if number_of_letters_in_password > 0:
        for i in range(0,password_length - number_of_letters_in_password):
            password+=LETTERS[random.randint(0,len(LETTERS)-1)] 

    print("Your Password is: ",password)
except:
    print("Incorrect Input")
