from datetime import*
data = open('dtpeminjam.txt', 'a')

print('SELAMAT DATANG DI PERPUSTAKAN MERDEKA')
print('=====================================')

while True:
    kode = input('Masukan Kode : ')
    nama = input('Masukan nama : ')
    buku = input('Masukan judul buku : ')

    x = datetime.now()
    y = x + timedelta(days=7)
    tglskrg = str(x.year) + '-' + str(x.month) + '-' + str(x.day)
    tglkmpl = str(y.year) + '-' + str(y.month) + '-' + str(y.day)
    dt = kode+"|"+nama+"|"+buku+"|"+tglskrg+"|"+tglkmpl+"\n"

    data.write(dt)

    pyn = input('Masih ada (y/n) : ')
    if pyn in ('n', 'N'):
        break

data.close()
