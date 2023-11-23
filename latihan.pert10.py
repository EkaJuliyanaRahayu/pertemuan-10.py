list = {
    "Arii" : "081267888", "Dina" : "087677776"
}
print("\nTampilkan kontak Arii :")
print(29*"=")
print(" {0:^2} |".format("Nama"), "Nomor Telepon ")
print("=================================")

# Tampilkan Kontak Ari
print(" {0:^2} |".format("Arii"), list["Arii"], "\n")

# Tambah kontak baru
list["Riko"] = "087654544"

# Ubah kontak Dina dengan nomor baru
list["Dina"] = "088999776"

# Tampilkan semua Nama
print("Tampilkan semua Nama :")
print("==================================")

# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("============================================")


for x in list.keys():
    print(" {0:^2} |".format(x))
print("\n")

# Tampilkan semua Nomor
print("Tampilkan semua nomor :")
print("==============================")

# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("==============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
    print("\n")
    
# Menghapus kontak Dina
print("Menghapus kontak Dina :")
print(29*"=")
del list["Dina"]

print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("===============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")
