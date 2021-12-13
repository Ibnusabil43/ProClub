n = 5

p = n - 1
for i in range(n):
    for j in range (p):
        print(end = " ")
    p = p - 1
    for j in range(i+1):
        print("* ", end="")
    print()