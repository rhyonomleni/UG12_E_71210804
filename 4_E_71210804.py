def nilai_maksimal():
    terbesar = bilangan[0]
    terkecil = bilangan[0]
    for i in range(0, len(bilangan)):
        terbesar = max(terbesar,bilangan[i])
        terkecil = min(terkecil,bilangan[i])
    print("Nilai terbesar: ", terbesar)
    print("Nilai terkecil: ",terkecil)

#test case 1 
bilangan = [3, 20, 100, -35 ,50]
print(bilangan)
nilai_maksimal()

#test case 2
bilangan = [3, 20, 90, 35, 75]
print(bilangan)
nilai_maksimal()