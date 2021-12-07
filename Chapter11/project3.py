from datetime import*
data = open('dtpeminjam.txt', 'r')

tgl = datetime.now()
tglnow = str(tgl.year) + '-' + str(tgl.month) + '-' + str(tgl.day)

print('SELAMAT DATANG DI PERPUSTAKAN MERDEKA')
print('=====================================')

Kode = input('Masukan Kode : ')
print('')
print('Data peminjam buku')

lisitdata = []
aslikmpl = []

dt = data.readlines()

for i in range(len(dt)):
    pecah = dt[i].split('|')
    datapc= {"kode": pecah[0], "nama": pecah[1], "buku": pecah[2], "tglawal": pecah[3], "tglkmpl": pecah[4]}
    lisitdata.append(datapc)


for i in range(len(lisitdata)):
    pecah1 = lisitdata[i]
    kode = pecah1['kode']
    nama = pecah1['nama']
    buku = pecah1['buku']
    tglawal = pecah1['tglawal']
    tglkmpl = pecah1['tglkmpl']
    if Kode == kode:
        print('Kode                : ', str(kode))
        print('Nama                : ', str(nama))
        print('Judul buku          : ', str(buku))
        print('Tgl awal peminjaman : ', str(tglawal))

        pecahlg = tglkmpl.split('\n')
        nilk = {"tgl": pecahlg[0], "kosong": pecahlg[1]}
        aslikmpl.append(nilk)
        j = aslikmpl[0]
        tglKmpl = j['tgl']
        
        print('Tgl maks peminjaman : ', str(tglKmpl))
        print('Tgl pengembalian    : ', str(tglnow))
        x = datetime.strptime(tglKmpl, '%Y-%m-%d')
        y = datetime.strptime(tglnow, '%Y-%m-%d')
        c = y - x
        hari = c.days
        if hari > 0:
            terlambat = str(hari)
            denda = int(terlambat) * 2000
            print('Terlamabat          : ', terlambat, 'HARI')
            print('Tgl pengembalian    : ', denda)
        if hari < 0:
            print('Terlamabat          : -')
            print('Tgl pengembalian    : -')

        
if Kode != kode:
    print('“KOde tidak ditemukan”')        


data.close()
