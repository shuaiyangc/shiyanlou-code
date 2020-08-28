"""
for i in range(1,101):
    if i % 7 != 0 and i % 10 != 7 and i // 10 != 7: 
        print("1?100??7???????7????", i)
    i += 1 
"""

for i in range(1,101):
    if (i % 7 == 0) or (i % 10 == 7) or (i // 10 == 7): 
        continue
    else:
        print("1?100??7???????7????", i)
    i += 1 
