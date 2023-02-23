import math


n, a, b, d = [int(x) for x in input().split()]

time1, time2 = 0, 0

# eida diya target er niche thake
time1 += (n//d)*b
# eida diya target er upre jaiga jump diya
time2 = math.ceil(n/d)*b

# then haita jawar hishab kri
n1 = n - (n//d)*d
n2 = math.ceil(n/d)*d - n



time1 += n1*a
time2 += n2*a

# eine minimum time 
print(min(time1, time2))