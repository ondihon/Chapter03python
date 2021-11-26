dataNilai = []
i = 1
print('masukan niali n : ', end='')
n = int(input())
while True:
    print('masukan data ke-' + str(i) + ' : ', end='')
    x = int(input())
    n = n - 1
    
    if n == 0:
        dataNilai = dataNilai + [x]
        break
    else:
        dataNilai = dataNilai + [x]
    i = i + 1

dataNilai.reverse()
print(dataNilai)
