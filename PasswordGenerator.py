import random
import string

def generator(length,upper_case,lower_case,numbers,special_characters):
    character = ''
    if upper_case:
        character += string.ascii_uppercase
    if lower_case:
        character += string.ascii_lowercase
    if numbers:
        character += string.digits
    if special_characters:
        character += string.punctuation

    if character == '':
        return "Could not make password"

    password = ''.join(random.choice(character) for i in range(length))
    return password

print("Welcome to Password generator")
while True:
    length = int(input("Enter the length of the password: "))
    upper_case = input("Include uppercase in password?(Y/N) : ").upper() == 'Y'
    lower_case = input("Include lowercase in password?(Y/N) : ").upper() == 'Y'
    number = input("Include numbers in password?(Y/N) : ").upper() == 'Y'
    special_character = input("Include special character in password?(Y/N) : ").upper() == 'Y'
    password = generator(length,upper_case,lower_case,number,special_character)
    print("Your password is : ",password)

    if input("Do you want to generate another password?(Y/N) : ").upper() == "N":
      print("Tank You")
      break