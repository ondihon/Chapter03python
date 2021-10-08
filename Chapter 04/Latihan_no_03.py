#menghitung berapa liter bensin yang diperlukan
print('_____berapa jarak tempuh mobil_____')
jarakAC=float(input('Jarak kota A ke C (km):'))
print('perbandingan nya 1:12 (1L untuk 12 Km)')
print('maka bensin yang diperlukan adalah')
totalbensin=jarakAC/12
print(totalbensin, 'L')
#menghitung berapa kali isi bensin
kapasitastangki=float(input('kapasitas tangki mobil(L):'))
isibensin=round(totalbensin/kapasitastangki)
print('miniamal mengisi bensin full sebanyak')
print(isibensin,' kali')

