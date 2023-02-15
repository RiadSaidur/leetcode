forcasts = list(map(float, input().split()))

rainyDays = 0

for forcast in forcasts:
  if forcast >= 0.8:
    rainyDays += 1

print(rainyDays)