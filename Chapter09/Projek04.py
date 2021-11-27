
def acak(s, i):
    i = int(i)
    j=i
    while True:
        x = ''.join(random.sample(s,len(s)))
        data.append(x)
        i-=1
        if i == 0:
            print('=============================')
            print('HASILNYA')
            print('(' + s + ', ' + str(j) + ')' + ' -> ',end='')
            print(data)
            break
import random
data=[]
s=input(str('Masukan data : '))
i=input('Masukan jumlah perulangan : ')
acak(s, i)




