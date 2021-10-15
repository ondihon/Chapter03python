#tampilan
kode=str(input('Masukan Kode Karyawan       :'))
nama=str(input('Masukan Nama Karyawan       :'))
golongan=input('Masuakn Golongan            :')
#perhitugan golongan
if golongan == "A":
    gp=10000000;
    pt=2.5;
if golongan == "B":
    gp=8500000;
    pt=2.0;
if golongan == "C":
    gp=7000000;
    pt=1.5;
if golongan == "D":
    gp=5500000;
    pt=1.0;
print('=========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------')
print('Masukan Nama Karyawan       : ' + nama + (' (Kode: ' + kode + (')')))
print('Golongan                    : ' + golongan)
print('-----------------------------------------')
#perhitungan potongan gaji
print('Gaji Pokok                  : Rp ' + str(gp))
pth=gp*pt*0.01;
print('potongan (' + str(pt) + ('%)             : Rp ') + str(pth))
print('----------------------------------------- -')
#perhitugan gaji bersih
gb=gp-pth
print('Gaji Bersih                 : Rp ' + str(gb))
