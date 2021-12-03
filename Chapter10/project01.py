data = open('d:angka.txt','r')
dt = data.readlines()
h = []
for i in range(len(dt)):
    x = dt[i]
    y = x.split('\n')
    c = y[0]
    h.append(c)


gp = 0
gj = 0
for i in range(len(h)):
    N = h[i]
    N = int(N)
    if N%2 == 0:
        gp += 1
    if N%2 != 0:
        gj +=1
        
print(h)
print('Banyaknya bilangan genap: ', gp)
print('Banyaknya bilangan ganjil: ', gj)
data.close()
