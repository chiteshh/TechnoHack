import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Password = ""

print("Welcome to the Password Generator!")
letters = int(input("How many letters would you like to have in your password ?\n")) 
symbols = int(input(f"How many symbols would you like to have ?\n"))
numbers = int(input(f"How many numbers would you like to have ?\n"))

password_list = []

for char in range(1, letters + 1):
  password_list.append(random.choice(Letters))

for char in range(1, symbols + 1):
  password_list += random.choice(Symbols)

for char in range(1, numbers + 1):
  password_list += random.choice(Numbers)

random.shuffle(password_list)

for char in password_list:
  Password += char

print(f"Your password is: {Password}")