buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
v = buah.values()
lv = list(v)
x= max(lv)
n = 0
while True:
    k = buah.keys()
    lk = list(k)
    z = lk[n]
    r = buah.get(z)
    if r == x:
        print('buah yang paling mahal adalah ', z, x)
        break
    else:
        n += 1

