from random import randint
count = 0
while True:
    bil = randint(0, 10)
    print(bil)
    count = count + 1
    if bil == 5:
        print('jumlah perulangan : %d' %count)
        break
