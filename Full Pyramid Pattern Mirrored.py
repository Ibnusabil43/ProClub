n = 4

p = 2*n - 2
for i in range(n, -1 , -1):
    for j in range (p, 0, -1):
        print(end = " ")
    p = p + 1
    for j in range(i+1):
        print("* ", end="")
    print()