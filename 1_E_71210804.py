awal = int(input("Masukkan awal deret: "))
akhir = int(input("Massukan akhir deret: "))
for i in list(range(awal,akhir)): 
    if i %2==0 and i %5 != 0 and i %9 != 0:
     print(i," ", end= "")