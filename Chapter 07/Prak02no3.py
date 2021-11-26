def pembagian():
    try:
        #membuka dan mau mebaca file d:/data.txt
        file = open("c:/data.txt", "r")

        #baca baris pertama dari file
        # simpan ke dalam variabel bil1 sbg integer
        bil1 = int(file.readline())

        #baca baris pertama dari file
        #simpan kedalam variabel bil2 sbg integer
        bil2 = int(file.readline())

        #hitung dan tampilkan hasil bagi
        hasil = bil1/bil2
        print(bil1, 'dibagi', bil2, 'samadengan', hasil)

    except FileNotFoundError:
        print('file tidak ditemukan')
    except ZeroDivisionError:
        print('tidak boleh pembagain degan nol')

pembagian()

