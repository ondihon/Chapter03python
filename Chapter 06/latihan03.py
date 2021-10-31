#memasukan niali n dan k
n = int(input('nilai n = '))
k = int(input('nilai k = '))
#perhitungan permutasi
list1=[]
i=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilpermutasi=(n-i)
        list1.append(hasilpermutasi)
        i+=1
        if ((n-i)+k)==n:
            break
#perhitungan kombinasi
list2=[]
j=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilkombinasi=(k-j)
        list2.append(hasilkombinasi)
        j+=1
        if (k-j)==0:
            break
#mengitung hasil
def hasil(data):
    r=1
    for x in data:
        r=r*x
    return r
#hasil
print(f'p({n}, {k})= {hasil(list1)}')
print(f'c({n}, {k})= {hasil(list1)/hasil(list2)}')
