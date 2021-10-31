def sum(*mydata):
    sum = 0
    for data in mydata:
        sum += data
    print(mydata)
    print('Nilai total: ', sum)

def average(*mydata):
    sum = 0
    i = 0
    for data in mydata:
        sum += data
        i += 1
    rata2 = sum/i
    print(mydata)
    print('Nilai rata-rata: ', rata2)

def maksimum(*mydata):
    print(mydata)
    print('Nilai terbesar:', max(mydata))

def minimum(*mydata):
    print(mydata)
    print('Nilai terkecil:', min(mydata))




