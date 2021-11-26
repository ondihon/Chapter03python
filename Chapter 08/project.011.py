buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Menu:')
print('A.	Tambah data buah')
print('B.	Beli buah')
jwb = str(input('Pilihan menu : '))

if jwb == "a":
    while True:
        print('Masukkan nama buah 		: ', end='')
        nama = input()
        if nama == '':
            break
        if nama in buah:
            print('nama buah sudah ada di dalam dictionary')
        else:
            print('Masukkan harga satuan		: ', end='')
            harga = int(input())
            buah[nama]=harga
            print('Data buah :')
            for x, y in buah.items():
                print(x, '(harganya Rp', y, ')')
if jwb == "b":
    h = 0
    while True:
        x = input('Nama buah yang dibeli : ')
        if x in buah:
            y = int(input('Berapa Kg : '))
            j = buah.get(x)
            t = y * int(j)
            h = h + t
            w = input('Beli buah yang lain (y/n) ? ')
            if w == "n":
                break
        else:
            print('nama buah tidak ditemukan')
    print('-------------------------------------------')
    print('Total harga : ' + str(h))
