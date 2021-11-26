sayur = {'bayam', 'kangkung', 'wortel', 'selada'}
while True:
    print('Menu:')
    a = print('A. Tambah data sayur')
    b = print('B. Hapus data sayur')
    c = print('C. Tampilkan data sayur')
    print('')
    n = print('n untuk berhenti')
    j = str(input('Pilihan ada: '))
    
    if j == "a":
        x = str(input('nama sayur : '))
        sayur.add(x)
        
    if j == "b":
        try:
            y = str(input('nama sayur : '))
            sayur.remove(y)
        except KeyError:
            print('tidak ada nama sayur')
            
    if j == "c":
        print(sayur)
        
    if j == "n":
        break

