# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
coffee ="Coffee"
coffee_price="3.50"
coffee_qty="2"
coffee_total= coffee_price*coffee_qty

muffin = "Muffin"
muffin_price="2.10"
muffin_qty= "3"
muffin_total= muffin_price*muffin_qty

water= "Water"
water_price= "1.05"
water_qty= "4"
water_total= water_price*water_qty

subtotal = coffee_total + muffin_total + water_total
tax = subtotal * 0.06
total = subtotal + tax

store = "========== RECEIPT ==========\nItem\tPrice\tQty\tTotal"
print(store)
print(f"{coffee}\t${coffee_price: .2f}\t{coffee_qty}\t${coffee_total: .2f}\n"
      f"{muffin}\t${muffin_price: .2f}\t{muffin_qty}\t${muffin_total: .2f}\n"
      f"{water}\t${water_price: .2f}\t{water_qty}\t${water_total: .2f}\n")
print("------------------------------------")
print(f"{Subtotal}\t\t${}")