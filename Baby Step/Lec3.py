# Loops in python: for, while
for i in range(8):
    print(i * 2)

password = "secret"
input_pass = ""

while input_pass != password:
    input_pass = input("Enter Password ")

print("Access Granted")