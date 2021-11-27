def bintang1(n):
    jarak = n+1
    for i in range(n//2+1):
        print(('*'*(2*i+1)).center(jarak))
def bintang2(n):
    jarak = n+1
    i = n//2-1
    while True:
         print(('*'*(2*i+1)).center(jarak))
         i -=1
         if i == 0:
             print(('*'*(2*i+1)).center(jarak))
             break
y = input('Masukan nilai n : ')
n = int(y)
bintang1(n)
bintang2(n)


