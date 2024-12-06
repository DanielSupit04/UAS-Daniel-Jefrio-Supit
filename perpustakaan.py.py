import json

perpustakaan = []

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan Nama penulis buku: ")
    tahun_terbit = input("Masukkan tahun terbit: ")
    kategori = input("Masukkan kategori buku: ")
    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun_terbit,
        "kategori": kategori,
        "dipinjam": False
    }
    perpustakaan.append(buku_baru)
    print("Buku berhasil ditambahkan!")


def cari_buku():
    cari = input("Masukkan kata kunci pencarian (judul/penulis/kategori): ")
    hasil_pencarian = []
    for buku in perpustakaan:
        if cari.lower() in buku["judul"].lower() or cari.lower() in buku["penulis"].lower() or cari.lower() in buku["kategori"].lower():
            hasil_pencarian.append(buku)
    if hasil_pencarian:
        print("Hasil pencarian:")
        for buku in hasil_pencarian:
            print(buku)
    else:
        print("Buku tidak ditemukan!")

def pinjam_buku():
    judul = input("Masukkan judul buku yang ingin dipinjam: ")
    for buku in perpustakaan:
        if buku["judul"] == judul and not buku["dipinjam"]:
            buku["dipinjam"] = True
            print("Buku berhasil dipinjam!")
            return
    print("Buku tidak tersedia atau sudah dipinjam!")

def kembalikan_buku():
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
    for buku in perpustakaan:
        if buku["judul"] == judul and buku["dipinjam"]:
            buku["dipinjam"] = False
            print("Buku berhasil dikembalikan!")
            return
    print("Buku tidak ditemukan atau belum dipinjam!")

def tampilkan_buku_dipinjam():
    buku_dipinjam = [buku for buku in perpustakaan if buku["dipinjam"]]
    if buku_dipinjam:
        print("Daftar buku yang sedang dipinjam:")
        for buku in buku_dipinjam:
            print(buku)
    else:
        print("Tidak ada buku yang sedang dipinjam.")

def simpan_data():
    with open("perpustakaan.json", "w") as file:
        json.dump(perpustakaan, file)
    print("Data buku berhasil disimpan!")

def hapus_buku():
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    for i, buku in enumerate(perpustakaan):
        if buku["judul"] == judul:
            del perpustakaan[i]
            print("Buku berhasil dihapus!")
            return
    print("Buku tidak ditemukan!")

def load_data():
    global perpustakaan
    try:
        with open("perpustakaan.json", "r") as file:
            perpustakaan = json.load(file)
        print("Data buku berhasil dimuat!")
    except FileNotFoundError:
        print("File data buku tidak ditemukan. Dimulai dari data kosong.")

load_data()

while True:
    print("\nMenu Perpustakaan UNIMA:")
    print("1. Tambah buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Tampilkan Buku Yang Sedang Dipinjam")
    print("6. Simpan Data")
    print("7. Hapus Buku")
    print("8. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        cari_buku()
    elif pilihan == "3":
        pinjam_buku()
    elif pilihan == "4":
        kembalikan_buku()
    elif pilihan == "5":
        tampilkan_buku_dipinjam()
    elif pilihan == "6":
        simpan_data()
    elif pilihan == "7":
        hapus_buku()
    elif pilihan == "8":
        break
    else:
        print("Pilihan tidak valid!")