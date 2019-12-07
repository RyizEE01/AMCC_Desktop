angka1 = int(input('masukan angka: '))
angka2 = int(input('masukan angka: '))
print('operator :  \n1.penjumlahan \n2.pengurangan \n'
        '3.perkalian \n4.pembagian')
pilihan =  int(input('masukan operator: '))
if pilihan == 1:
    tambah = angka1+angka2
    print('hasilnya adalah', tambah)
elif pilihan == 2:
    kurang = angka1-angka2
    print('hasilnya adalah', kurang)
elif pilihan == 3:
    kali = angka1*angka2
    print('hasilnya adalah', kali)
elif pilihan == 4:
    bagi = angka1/angka2
    print('hasilnya adalah', bagi)
else:
    print('maaf anda kurang beruntung')
    