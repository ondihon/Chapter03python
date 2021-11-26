x = input('masukan nama file: ')
file = open(x, "a")
i = input('data yang mau ditambahkan: ')
file.write(i)
file.close()
j = input('mau lagi (y/n): ')
while True:
    if j == "y":
        file = open(x, "a")
        i = input('data yang mau ditambahkan: ')
        file.write(i)
        file.close()
        j = input('mau lagi (y/n): ')
    if j == "n":
        break
