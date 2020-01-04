def km(a):
    h = a / 1000
    return h

a = float(input("masukan angka: "))
print("jarak dalam kilometer : ",a)
print("jarak dalam meter : ",km(a))


import sys

print('the command line argument:')
for i in sys.argv:
  print(i)


import mymodule

mymodule.hitung(5,4)