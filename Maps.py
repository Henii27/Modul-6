# Membuat maps
data = {}

# Menambahkan data ke maps
data["nama"] = "Alice"
data["umur"] = 30
data["kota"] = "Jakarta"

# Mengakses data dari maps
print(data["nama"])  # Output: Alice
print(data["umur"])  # Output: 30

# Mengubah data dalam maps
data["kota"] = "Bandung"

# Menghapus data dari maps
del data["umur"]

# Memeriksa apakah key ada dalam maps
if "umur" in data:
  print("Key 'umur' ada dalam maps")
else:
  print("Key 'umur' tidak ada dalam maps")
