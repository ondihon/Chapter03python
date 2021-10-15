#tampilan
kode=str(input('Masukan Kode Karyawan       : '))
nama=str(input('Masukan Nama Karyawan       : '))
golongan=input('Masuakn Golongan            : ')
status=input('Masukkan status             : ' )
if status == '1':
    sts='menikah';
    stsh=10/100;
    anak=float(input('Masukkan jumlah anak	    : '));
    nk=5/100*(anak);
if status == '2':
    sts='belum';
    stsh=0
    anak=0;
    nk=0;
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
print('Golongan                    : ' + str(golongan))
print('Status Menikah              : ' + str(sts))
print('Jumlah Anak                 : ' + str(anak))
print('-----------------------------------------')
print('Gaji Pokok                  : Rp ' + str(gp))
#tunjangan status
ts=(stsh)*gp;
print('Tunjangan Istri/Suami	   : RP ' + str(ts))
ta=(nk)*gp;
print('Tunjangan anak	           : Rp ' + str(ta))
print('----------------------------------------- +')
#perhitunga Gaji Kotor
gk=gp+ts+ta
print('Gaji Kotor                  : RP ' + str(gk))
#perhitungan potongan gaji
pth=gp*pt*0.01;
print('potongan (' + str(pt) + ('%)             : Rp ') + str(pth))
print('----------------------------------------- -')
#perhitugan gaji bersih
gb=gk-pth;
print('Gaji Bersih                 : Rp ' + str(gb))
