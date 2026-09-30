num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total_temp = 0

for i in range (num_days):
    temperature = float(input())
    total_temp += temperature
    
print(danger_days)
print(f"{average_temp:.1f}")


