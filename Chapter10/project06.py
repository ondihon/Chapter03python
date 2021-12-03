data = open('teks asli.txt', 'r')
masuk = open('teks kode.txt', 'a')
acak = input('Masukan jumlah n: ')
asli = data.read()

hasil = []
print('Teks asli: ', end='')
print(asli)
for i in range(len(asli)):
    ubah = asli[i]
    x = int(ord(ubah))
    if x == 32:
        ganti = 32
        f = chr(ganti)
        hasil.append(f)
    if x != 32:
        ganti = x + int(acak)
        f = chr(ganti)
        hasil.append(f)

data.close()

tup = tuple(hasil)   
gabung = str('')

for i in range(len(tup)):
    gabung += tup[i]   



masuk.write(gabung)
masuk.close()

buka = open('teks kode.txt', 'r')
k = buka.read()
buka.close()
print('Teks kode: ', end='')
print(k)
