alas1 = 10
tinggi1 = 20
alas2 = 15
tinggi2 = 45
def luasSegitiga(alas1 , tinggi1):
    global luas1
    luas1 = alas1 * tinggi1 / 2
    return luas1
luasSegitiga(alas1 , tinggi1)
luas1 = (luasSegitiga(alas1 , tinggi1))
print('luas segitiga dg alas ', alas1,
      ' dan tingi ', tinggi1,
      ' adalah ', luas1)

def luasSegitiga2(alas2 , tinggi2):
    global luas2
    luas2 = alas2 * tinggi2 / 2
    return luas2
luasSegitiga2(alas2 , tinggi2)
luas2 = (luasSegitiga2(alas2 , tinggi2))
print('luas segitiga dg alas ', alas2,
      ' dan tingi ', tinggi2,
      ' adalah ', luas2)


def jumlah(luas1, luas2):
    global hasil 
    hasil = luas1 + luas2
    return hasil
print('jadi jumlah kedua segitiga adalah ', jumlah(luas1, luas2))





