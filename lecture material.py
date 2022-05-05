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


def Name(name):  # Defines the function
    print(f"Hello {name}")  # States the operation of the function


Name("Archibong")  # Calls the function
# Using a function to square a series of numbers
num1 = [56, 65, 54, 44, 3, 24, 24, 22, 43]
def squares():
    for num in nums:
        print(num**2)


# Testing out the args for tuples
def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)


outputData("Archibong Goodluck", 5, True, "Jess")


# Testing out the kwargs for dictionary
def output(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])


output(name="Archibong Goodluck", num=5, b=True)



# Testing Tenary operator
def search(aList, el):
    return True if el in aList else False


result = search( [ "one", 2, "three" ], 2)
print(result)




# Testing out Global scope1
number = 4


def scope_test():
    number += 1 # Checking if the variable declared at a global scope is accessible within the function scope


scope_test() # Outputs error


# Testing out Global scope2
number = 4


def scope_test(number = 4 ):
    number += 1 # Checking if the variable declared at a global scope is accessible within the function scope


scope_test() # runs


# changing list item values by index
sports = [ "baseball", "football", "hockey", "basketball" ]


def change(aList):
    aList[ 0 ] = "Soccer"


print(f"Before altering: {sports}" )
change(sports)
print( f"After Altering: {sports}")
