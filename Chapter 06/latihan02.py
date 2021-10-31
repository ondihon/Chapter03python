def starFormation1(n):
    i = 1
    while (i <= n // 2):
        if n % 2 == 1:
            n += 1
        print('*' * (i))
        i += 1

def starFormation2(n):
    i = 1
    n = n // 2
    while (i <= n):
        print('*' * (n))
        n -= 1
n = int(input('masukan nilai n = '))
starFormation1(n)
starFormation2(n)
