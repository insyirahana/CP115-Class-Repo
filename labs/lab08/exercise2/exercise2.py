employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = overtime_hours * 35
gross = base_salary + overtime_pay 

if tax_status == "Single":
    if gross >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18

elif tax_status == "Married":
    if gross >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15

else:
    if gross >= 5500:
        tax_rate = 0.25
    else:
        tax_rate  = 0.19

net_salary = gross - (gross * tax_rate) - (gross * 0.11) - (gross * 0.005)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
