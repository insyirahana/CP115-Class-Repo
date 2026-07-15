kWh = int(input())
if kWh <= 100:
    totalBill = kWh * 0.3 
else:
    if kWh >= 101 and kWh <= 200:
        charge = 100 * 0.3 + (kWh - 100) * 0.5
    else:
        totalBill = 100 * 0.3 + 200 * 0.5 + (kWh - 200) * 0.75
totalBill = kWh * charge
# print(Expression)
