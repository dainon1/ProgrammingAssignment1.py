#Dainon Harris 11-16-24  Calculating CSC 221 Book Cost
import math
num_books = int(input("Please enter the number of CSC 221 books purchased: "))
price = float(input("Please enter the price of each CSC 221 book purchased: "))
subtotal = float(num_books * price)
tax = float(.053)
total = float(subtotal + (subtotal*tax))
#Enter math module of ceil and floor value
ceiling = math.ceil(total)
floor = math.floor(total)
print("You bought", num_books,"books at $","%.2f"% price, "each.\n Your total with taxes is: $","%.2f"% total, "floor and ceiling")
print(id(num_books), id(price), id(subtotal), id(tax), id(total), id(ceiling), id(floor))


