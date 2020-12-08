a = 0
for a in range(100):
    a+=1
    if (a % 7 == 0):
        continue
    elif(a % 10 == 7):
        continue
    elif(a // 10 == 7):
        continue
    else:
        print(a)
