buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
x = input('Nama buah yang dibeli : ')
y = int(input('Berapa Kg : '))
j = buah.get(x)
t = y * j
print('-------------------------------------------')
print('Total harga : ' + str(t))

