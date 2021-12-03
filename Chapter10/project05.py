data = open('isibill.txt', 'r')
masuk = open('hasilbill.txt', 'a')
baris = data.readlines()

for i in range(len(baris)):
    pecah=baris[i].split('|')
    pc1 = pecah[0]
    pc2 = pecah[1].split('\n')
    pc2 = pc2[0]
    
    jumlah = int(pc1) + int(pc2)
    masukan = str(jumlah)+'\n'
    masuk.write(masukan)




data.close()
masuk.close()

