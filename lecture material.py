g1name, g1price = "phone", 76
g2name, g2price = "car", 120
g3name, g3price = "satellite", 567
total_price = g1price + g2price + g3price
company_name = "Archibong Technologies"
company_address = "Port Harcourt, Nigeria"
company_message = "Archibong Takeover"
print("*" * 60)
print(f"\t\t{company_name.upper()} \n\t\t{company_address.title()}")
print("*" * 60)
print('\tProduct Name\t\tProduct Price')
print(f"\t{g1name.title()}\t\t\t\t{g1price}")
print(f"\t{g2name.title()}\t\t\t\t{g2price}")
print(f"\t{g3name.title()}\t\t\t{g3price}")
print("*" * 60)
print(f"\tTotal Price \t\t\t{total_price}")
print("*" * 60)
print(f"\t\t{company_message.upper()}")
print("*" * 60)