Nama = input("Masukkan Nama : ")
NIM = input("Masukkan NIM : ")

print("NIM : "+NIM)
print("NAMA : "+Nama)
print("Pilihan")
print("1. Capucino")
print("2. Teh")
print("3. Exit")

Menu = input("Masukkan pilihan : ")

def pilih():
    if Menu == "1":
        print("Memilih Capucino")
    elif Menu == "2":
        print("Memilih Teh")
    elif Menu == "3":
        print("Cancel")
    else :
        print("Menu tidak tersedia")

def harga():
    if ((Menu == "1") or (Menu == "2")) :
        Harga = int(input("Masukkan harga : "))
        ppn = Harga*(10/100)
        print(Harga+ppn)
    else :
        return 0

pilih()
harga()
