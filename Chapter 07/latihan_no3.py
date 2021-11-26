print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')
def lol():
    try:
        global c
        global i
        global j
        data = int(input('masukan bilangan bulat: '))
        c += data
        i += 1
        j = input('mau lanjut gak (y/n): ')
        
    except ValueError:
        print('bukan bilangan bulat')
        j = input('mau lanjut gak (y/n): ')

c = 0    
i = 0    
while True:
    lol()
    if j == "y":
        lol()
    if j == "n":
        rat = c/i
        print('nilai rata ratanya adalah: ', rat)
        break
