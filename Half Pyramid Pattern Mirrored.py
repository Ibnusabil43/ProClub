n = 5

p = 2*n - 2
for i in range(n):
    for j in range (p):
        print(end = " ")
    p = p - 2
    for j in range(i+1):
        print("* ", end="")
    print()