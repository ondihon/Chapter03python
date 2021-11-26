x = input('masukan nama file: ')
file = open(x, "r")
print('isi file', x, 'adalah: ')
print(file.read())
