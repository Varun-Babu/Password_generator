import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("enter the amount of letters required"))
nr_numbers= int(input("enter the amount of numbers required"))
nr_symbols= int(input("enter the amount of symbols required"))
password = []
for char in range(1,nr_letters+1):
    rand_char = random.choice(letters)
    password += rand_char
for no in range(1,nr_numbers+1):
    rand_no = random.choice(numbers)
    password += rand_no
for sym in range(1,nr_symbols+1):
    rand_sym = random.choice(symbols)
    password += rand_sym
random.shuffle(password)
a=""
for i in password:
    a += i
print(f"your new password is {a} ")        