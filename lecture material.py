# Creation of a Purchase Receipt

g1name, g1price = "phone", 76
g2name, g2price = "car", 120
g3name, g3price = "satellite", 567
total_price = g1price + g2price + g3price  # sums the prices of purchased items
company_name = "Archibong Technologies"  # Declares Company Name
company_address = "Port Harcourt, Nigeria"  # Declares Company address
company_message = "Thank you for your patronage"  # Declares Company message
print("*" * 60)
print(f"\t\t{company_name.upper()} \n\t\t{company_address.title()}")
print("*" * 60)
print('\tProduct Name\t\tProduct Price')
print(f"\t{g1name.title()}\t\t\t\t{g1price}")
print(f"\t{g2name.title()}\t\t\t\t\t{g2price}")
print(f"\t{g3name.title()}\t\t\t{g3price}")
print("*" * 60)
print(f"\tTotal Price \t\t{total_price}")
print("*" * 60)
print(f"\t\t{company_message.upper()}")
print("*" * 60)


# Creation of a basic Arithmetic Calculator
User_que = input("Dear user what calculation would you love to perform? Kindly input one of the following 'sum', 'div', 'mult' or 'sub': ")
user_num1 = int(input("Kindly input the first number in integers: "))
user_num2 = int(input("Kindly input the second number in integers: "))
user_decision1, user_decision2, user_decision3, user_decision4 = "sum", "div", "mult", "sub"

if User_que == "sum":
    print( user_num1 + user_num2)
elif User_que == "div":
    print( user_num1 / user_num2)
elif User_que == "mult":
    print( user_num1 * user_num2)
elif User_que == "sub":
    print( user_num1 - user_num2)
else:
    print("Invalid arithmetic operation")