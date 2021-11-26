nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
x = 0
pj = len(nilaiMhs)
nx = []
while True:
    j = nilaiMhs[x]
    v = j.values()
    l = list(v)
    na = (l[2] + 2 * l[3]) / 3
    nx = nx + [na]
    k = j.keys()
    lk = list(k)
    pj -= 1
    print(lk[0], l[0], lk[1], l[1], 'nilai akhir', na)
    if pj == 0:
        break
    else:
        x += 1
k = max(nx)
print('niali akhir tertinggi adalah ', k) 
