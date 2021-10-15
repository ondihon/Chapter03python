print('____________Nilai Ujian____________')
#masukan nila ujian
a=int(input('Masukan nilai Bahasa Indonesia:'))
b=int(input('Masukan nilai IPA             :'))
c=int(input('Masukan nilai Matematika      :'))
#perhitungan remedial
if (a < 0) or (b < 0) or (c < 0):
    print('Maaf input ada yang tidak valid')
elif (a < 60) or (b < 60) or (c < 70):
    print('Status Kelulusan              : TIDAK LULUS')
else:
    print('Status Kelulusan              : LULUS')
