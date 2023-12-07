class PerpusItem:
    def __init__(self, Judul, Subjek):
        self.Judul = Judul
        self.Subjek = Subjek

    def LokasiPenyimpan(self):
        return self.Subjek

    def info(self):
        return self.Subjek

class Buku(PerpusItem):
    def __init__(self, Judul, Subjek, ISBN, Pengarang, jmlHal, ukuran):
        super().__init__(Judul, Subjek)
        self.ISBN = ISBN
        self.Pengarang = Pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran

class Majalah(PerpusItem):
    def __init__(self, Judul, Subjek, volume, issue):
        super().__init__(Judul, Subjek)
        self.volume = volume
        self.issue = issue

class DVD(PerpusItem):
    def __init__(self, Judul, Subjek, Aktor, Genre):
        super().__init__(Judul, Subjek)
        self.Aktor = Aktor
        self.Genre = Genre

class Katalog:
    def cari(self):
        pass

class Pengarang:
    def __init__(self):
        self.nama

    def info(self):
        pass

    def cari(self):
        pass

buku = Buku("PEMROGRAMAN", "BUKU", "111-222-333-44-5", "LUKE", 100, "A4")
majalah = Majalah("KULYEAH", "MAJALAH", 200, 1)
dvd = DVD("WARKOP", "MOVIE", "PAIJO", "KOMEDI")

print(" -Informasi Buku-")
print("Judul              : ", buku.Judul)
print("ISBN               : ", buku.ISBN)
print("Pengarang          : ", buku.Pengarang)
print("Jumlah Halaman     : ", buku.jmlHal)
print("Ukuran             : ", buku.ukuran)
print("Lokasi Penyimpanan : ", buku.LokasiPenyimpan())

print("\n-Informasi Majalah-")
print("Judul              : ", majalah.Judul)
print("Volume             : ", majalah.volume)
print("Issue              : ", majalah.issue)
print("Lokasi Penyimpanan : ", majalah.LokasiPenyimpan())

print("\n-Informasi DVD-")
print("Judul              : ", dvd.Judul)
print("Aktor              : ", dvd.Aktor)
print("Genre              : ", dvd.Genre)
print("Lokasi Penyimpanan : ", dvd.LokasiPenyimpan())
