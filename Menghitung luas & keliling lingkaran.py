
print('============================================')
print('--------Gilar Sumilar (312210407)-----------')
print('Program Menghitung Luas & Keliling Lingkaran')
print('============================================')

r = float(input('\nMasukan nilai jari-jari : '))

phi = 3.14
diameter = 2*r

luas = phi*r*r
keliling = phi*diameter
print('\nLuas\t =', str("%.2f" % luas))
print('Keliling =', str("%.2f" % keliling))