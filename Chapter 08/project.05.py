bil = [2, 4, 5, 6]
def kuadrat(bil):
    g = []
    l = len(bil)
    x = 0
    while True:
        l -= 1
        y = bil[x]
        n = int(y)**2
        g = g + [n]
        if l == 0:
            break
        else:
            x += 1
            
    return g

kuadrat(bil)
hasil = kuadrat(bil)
print('bil = ' + str(bil))
print('setelah di kuadratkan ' + str(hasil))
