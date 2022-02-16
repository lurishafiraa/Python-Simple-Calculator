print("SIMPLE CALCULATOR")
print('-----------------')
print('fitur - fitur :')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('-----------------')

angka1 = float(input('Masukkan angka pertama : '))
angka2 = float(input('Masukkan angka kedua : '))

# Logic
def penjumlahan(angka1, angka2):
    return angka1+angka2

def pengurangan(angka1, angka2):
    return angka1-angka2

def perkalian(angka1, angka2):
    return angka1*angka2

def pembagian(angka1, angka2):
    return angka1/angka2

fitur = int(input('Pilih fitur : '))
if fitur == 1:
    print('hasil penjumlahan adalah : ', penjumlahan(angka1, angka2))
elif fitur == 2:
    print('hasil pengurangan adalah : ', pengurangan(angka1, angka2))
elif fitur == 3:
    print('hasil perkalian adalah : ', perkalian(angka1, angka2))
elif fitur == 4:
    print('hasil pembagian adalah : ', pembagian(angka1, angka2))
else:
    print('fitur tidak tersedia :( ')





