import random
angka_rahasia = random.randint(1, 10)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
while True:
  jawaban = int(input('\nTebakan Anda : '))

  if jawaban == angka_rahasia:
    print('Yeeee… Bilangan tebakan anda BENAR :-)')
    break # berhenti paksa
  else:
    print(
      'Hehehe… Bilangan tebakan anda terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar'
    )
