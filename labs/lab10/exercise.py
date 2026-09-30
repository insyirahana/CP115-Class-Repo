week = 1
while week <= 4:
    points = int(input(f"Week {week} points: "))
    if points >= 100:
        week += 2   # skip ahead a week
    else:
        week += 1