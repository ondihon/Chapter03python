data = open('datamhs.txt', 'a')

while True:
    nim = input('Masukkan NIM: ')
    nama = input('Masukkan nama: ')
    al = input('Masukkan Alamat: ')
    dt = nim+"|"+nama+"|"+al+"|"+"\n"

    data.write(dt)
    
    s = input('Masih mau lanjut (y/n): ')
    if s in ('N', 'n'):
        break

data.close()
