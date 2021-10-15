import random
angka_rahasia = random.randint(1, 10)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
count = 10
while True:
  jawaban = int(input('\nTebakan Anda : '))
  if count < -1:
    count = 0

  if jawaban == angka_rahasia:
    print('Yeeee… Bilangan tebakan anda BENAR :-)')
    print('Score Anda: %d'%count)
    break # berhenti paksa
  else:
    print(
      'Hehehe… Bilangan tebakan anda terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar')
    count = count - 2
    
    
