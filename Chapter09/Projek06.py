nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

for i in range(len(nilai)):
    x = int(nilai[i]['mid'])
    y = int(nilai[i]['uas'])
    j = (x+(2*y))//3
    nilai[i]['na']= j

for i in range(len(nilai)):
    sts = int(nilai[i]['na'])
    if sts >= 60:
        nilai[i]['sts']='LULUS'
    if sts < 60:
        nilai[i]['sts']='TIDAK LULUS'

print('================================================================')
print('NIM        NAMA MHS        MID   UAS    NA       STATUS')
print('----------------------------------------------------------------')

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(11), end='')
    print(nilai[i]['nama'].ljust(13), end='')
    print(str(nilai[i]['mid']).rjust(6), end='')
    print(str(nilai[i]['uas']).rjust(6), end='')
    print(str(nilai[i]['na']).rjust(6), end='')
    print(' '.rjust(7),end='')
    print(nilai[i]['sts'].ljust(1))


print('================================================================')
