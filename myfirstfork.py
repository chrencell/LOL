print("Calculator")

user = int(input("Write the first number  "))

data = int(input("Write the second number  "))

lol = (input("Write the operation(+, -, *, /) "))

if lol == "+":
    print("Result: " , user + data)

if lol == "-":
    print("Result: ", user - data)

if lol == "*":
    print("Result: ", user * data)

if lol == "/":
    if data == 0:
        print ("Error: opps, u cant!")

    if data != 0:
        print ("Result: ", user / data)