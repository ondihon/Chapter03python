data = open('datamhs.txt', 'r')

listdata = []

dt = data.readlines()

for i in range(len(dt)):
    pcdt=dt[i].split('|')
    dataDict = {"nim": pcdt[0], "nama": pcdt[1], "alamat": pcdt[2]}
    listdata.append(dataDict)
print(listdata)

data.close()
