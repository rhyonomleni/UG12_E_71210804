a = int(input("Masukkan angka: "))
for i in range(a):
    print(" "* (a-i)+" *"* (i+1))
for j in range(a-1):
    print(" "*(j+2)+" *"*(a-1-j))