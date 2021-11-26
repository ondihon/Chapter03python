def ssnm():
    data = []
    while True:
        x = input('masukkan nama : ')
        data = data + [x]
        yn = input('masih lanjut (y/n) : ')
        if yn in ('N', 'n'):
            break   
    return data
x = 0
y = 0
data = ssnm()
ssnm()
data = sorted(data)
nm = []
jb = []
for i in range(len(data)):
    kl = len(data[i])
    nm = nm + [kl]

def lol(x, y):
    l = len(data)
    while True:
        l -= 1
        gb = (data[x], nm[y])
        jb.append(gb)
        x += 1
        y += 1
        if l == 0:
            break

def cetakdata():
    print('--------------------------')
    for i in range(len(jb)):
        print(jb[i][0], end='')
        print('(', jb[i][1], 'karakter )')
lol(x, y)
cetakdata()
