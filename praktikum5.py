a = {
  "Ari": '081267888',
  "Dina": '087677776',
}
print(a)

#tampilkan kontak Ari
print ('Ari :', a['Ari'])

#Menambahkan kontak Riko
a['Riko'] = '087654544'
print('Riko : {}'.format(
  a.get('Riko')
))

#buah kontak dina 
a['Kontak Baru Dina'] = '088999776'
print('Kontak  Baru Dina : {}'.format(
  a.get('Kontak Baru Dina')
))

#Tampilkan Semua Nama 
for key in a.keys ():
    print(key)

#Tampilkan Semua Nomer
for value in a.values():
    print(value)

#Tampilkan Daftar Nama dan Nomer 
for item in a.items ():
    print(item)

#Hapus Kontak Dina
dina = a.pop('Dina')
print ('Dina :', a.get('Dina'))