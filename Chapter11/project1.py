from datetime import*

def ttg():
    print('contoh ttg: 20-01-2021')
    a = input('Masukan ttg awal: ')
    b = input('Masuakan ttg akhir: ')
    x = datetime.strptime(a, '%d-%m-%Y')
    y = datetime.strptime(b, '%d-%m-%Y')
    c = y - x
    hari = c.days
    print('selisih hari: ', hari)

ttg()
