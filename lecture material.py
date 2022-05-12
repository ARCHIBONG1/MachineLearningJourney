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


# Creating a shopping cart
from IPython.display import clear_output  # imports additional functions

# global list variable
cart = []


# creating a function for adding items to the cart
def add_item(item):
    clear_output()
    cart.append(item)
    print(f"{item}")


# creating a function for removing items from a cart
def remove_item(item):
    clear_output()
    try:
        cart.remove(item)
        print(f"{item} has been removed")
    except:
        print("Sorry we could not remove that item.")


# creating a function that displays the cart
def show_cart():
    clear_output()
    if cart:
        print("Here is your cart: ")
        for item in cart:
            print(f"- {item}")
    else:
        print("Your cart is empty. ")


# Claering the cart
def clear_cart():
    clear_output()
    cart.clear()
    print(" Your cart is empty.")


# creating the main fuction loop
def main():
    done = False

    while not done:
        ans = input("Quit/add/remove/show/clear: ").lower()
        if ans == "quit":  # Base Case
            print("Thanks for using out program")
            show_cart()
            done = True
        elif ans == "add":
            item = input("What would you like to add? ").title()
            add_item(item)
        elif ans == "remove":
            item = input("What would you like to remove? ").title()
            remove_item(item)
        elif ans == "show":
            show_cart()
        elif ans == "clear":
            clear_cart()
        else:
            print("Sorry that was not an option. ")


# Working with Classes
class Car():  # Declares a class
    sound1, sound2 = "Beep", "Honk"  # Assigns attribute
    colour1, colour2 = "Red", "Blue"

    def _init_(self, sound3, colour3):  # Dec;lares attribute 3 using the init method
        self.sound3 = sound3
        self.colour3 = colour3


print(Car1.sound1, Car1.colour1)  # prints the attributes of first instance: Note that the class wasnt first called
Car2 = Car() # Calls a second instance of the class
print(Car2.sound2, Car2.colour2) # Prints the attributes of second instance
Car2.sound2, Car.colour2 = "Beep", "Red" # Changes the attributes
print(Car2.sound2, Car.colour2) # Prints our attribute change
Car3 = Car("pipi", "black") # Declares a third instance of the class Car using personalised attribute courtesy of the init method
print(Car3.sound3)


class dog():  # Declares the class
    sound = "bark"  # Creates an attribute called sound

    def make_sound():  # static method
        print("bark")  #

    def make_sound_2(self):  # instance method
        print(self.sound)

    def show_age(self, age):
        print(age)


sam.make_sound()  # runs without being instantiated due to static method
sam = dog()
sam.make_sound2()  # only runs because the an instance of the class had been called
sam = dog()
sam.show_age(6)