print ('_____Rental Mobil_____')
print ('12 jam pertam Rp 200.000')
jam = 12
print('untuk jam berikutnya Rp 10.000')
menit = round(10000/60)
#Menghitung lama perjalan
print('waktu awal berangkat')
jam1=int(input('Jam:'))
menit1=int(input('Menit:'))
print('waktu sampai')
jam2=int(input('Jam:'))
menit2=int(input('Menit:'))
print('lama waktu sewa')
jam3 = jam2-jam1
menit3 = menit2-menit1
print('jam:', jam3)
print('jam:', menit3)
#Menghitung total tarif yang harus dibayar
jam4 = jam3 - jam
if(jam3 > 12):
    print('total harga= Rp', 200000+jam4*10000+menit3*menit)
