buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
h = 0
while True:
    x = input('Nama buah yang dibeli : ')
    y = int(input('Berapa Kg : '))
    j = buah.get(x)
    t = y * j
    h = h + t
    w = input('Beli buah yang lain (y/n) ? ')
    if w == "n":
        break
        
print('-------------------------------------------')
print('Total harga : ' + str(h))
