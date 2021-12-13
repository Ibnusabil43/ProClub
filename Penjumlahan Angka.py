def penjumlahan(x, y):
    var = list()
    for i in x:
        for j in x:
            if (i + j) == y:
                var.extend([x.index(i), x.index(j)])
                return var
    return []


a = [int(x) for x in input().split()]
b = int(input())
print(penjumlahan(a, b))