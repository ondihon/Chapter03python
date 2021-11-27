mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
datamhs=[]
for i in range(len(mhs)):
    x = mhs[i].split(':')
    data = (x)
    datamhs.append(data)
print(datamhs)

print('=================================================================')
print('NIM	    NAMA MAHASISWA	    TGL LAHIR	    TEMPAT LAHIR')
print('-----------------------------------------------------------------')
for i in range(len(datamhs)):
    print(datamhs[i][0].ljust(12), end='')
    print(datamhs[i][1].ljust(24), end='')
    print(datamhs[i][2].ljust(16), end='')
    print(datamhs[i][3].ljust(1),)


print('=================================================================')
