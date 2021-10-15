count = 0
summ = 0
for i in range(100) :
    if i % 2 == 1 :
        print (i, end= ' ')
        count = count + 1
        summ = summ + i
print ()
print()
print('Banyaknya bilangan ganjil : %d' %count)
print ('Jumlah seluruh bilangan   : %d' %summ)
