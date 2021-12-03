NIM = input('Masukkan NIM yang mau dicari: ')
print('')
print('Data Mahasiswa')

data = open('datamhs.txt', 'r')

listdata = []

dt = data.readlines()

for i in range(len(dt)):
    pcdt=dt[i].split('|')
    dataDict = {"nim": pcdt[0], "nama": pcdt[1], "alamat": pcdt[2]}
    listdata.append(dataDict)


data.close()

for i in range(len(listdata)):
    pecah = listdata[i]
    nim = pecah['nim']
    nama = pecah['nama']
    alamat = pecah['alamat']
    if NIM == nim:
        print('NIM	:', str(nim))
        print('Nama	:', str(nama))
        print('Alamat	:', str(alamat))
        break

if NIM != nim:
    print('“Data mahasiswa tidak ditemukan”')


