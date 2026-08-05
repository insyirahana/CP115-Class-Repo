item_name = input("Item name: ")
item_price =float(input("Item price : "))

quantity = 3
tax_rate  = 0.06

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal;", subtotal)
print("Tax:", tax)
print("Total Cost:", total)
