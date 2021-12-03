hari = input("Hi Tutu, Silahkan Masukkan hari yang ingin anda telusuri: ")
senin = ["kelas ke-1 Algoritma Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK","kelas ke-5 Praktikum INLAN"]
selasa = ["kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indo","kelas ke-6 PKN"]
kamis = ["kelas ke-1 IMK","kelas ke-3 Logmat","kelas ke-4 Prktekkom"]
jumat = ["kelas ke-2 Sistem Basis Data","kelas ke-4 Praktikum Sistem Basis Data","kelas ke-6 INLAN"]
if hari == "senin":
    for i in range(len(senin)):
        print(senin[i])
elif hari == "selasa":
    for i in range(len(selasa)):
        print(selasa[i])
elif hari == "rabu":
        print("Hari rabu Anda tidak ada kelas kelas")
elif hari == "kamis":
    for i in range(len(kamis)):
        print(kamis[i])
elif hari == "jumat":
    for i in range(len(jumat)):
        print(jumat[i])

