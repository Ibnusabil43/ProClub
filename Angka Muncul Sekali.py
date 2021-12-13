def angka_sekali(x) :
    y = list()
    for e in set(x):
        if list(x).count(e) == 1:
            y.append(e)
    return y

angka = input()
print(sorted(angka_sekali(angka), reverse=True))