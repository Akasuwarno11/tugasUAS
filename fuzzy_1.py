def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)
def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)
# variable input
class Permintaan():
    minimum = 2100
    maximum = 3500
    def turun(self, x):
        if x <= self.minimum:
            return 1
        elif x >= self.maximum:
            return 0
        else:
            return down(x, self.minimum, self.maximum)
    
    def naik(self, x):
        if x <= self.minimum:
            return 0
        elif x >= self.maximum:
            return 1
        else:
            return up(x, self.minimum, self.maximum)
class Persediaan():
    minimum = 100
    maximum = 250
    def sedikit(self, x):
        if x <= self.minimum:
            return 1
        elif x >= self.maximum:
            return 0
        else:
            return down(x, self.minimum, self.maximum)
    def banyak(self, x):
        if x <= self.minimum:
            return 0
        elif x >= self.maximum:
            return 1
        else:
            return up(x, self.minimum, self.maximum)
# variable output
class Produksi():
    minimum = 1000
    maximum = 5000
    permintaan = 0
    persediaan = 0
    def berkurang(self, a):
        return self.maximum - a * (self.maximum - self.minimum)
    def bertambah(self, a):
        return self.minimum + a * (self.maximum - self.minimum)
    def _inferensi(self):
        pmt = Permintaan()
        psd = Persediaan()
        data_inferensi = []
        # [R1] JIKA Permintaan TURUN, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        z1 = self.berkurang(a1)
        data_inferensi.append((a1, z1))
        # [R2] JIKA Permintaan TURUN, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERKURANG.
        a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        z2 = self.berkurang(a2)
        data_inferensi.append((a2, z2))
        # [R3] JIKA Permintaan NAIK, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERTAMBAH.
        a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        z3 = self.bertambah(a3)
        data_inferensi.append((a3, z3))
        # [R4] JIKA Permintaan NAIK, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        z4 = self.bertambah(a4) 
        z4 = self.bertambah(a4)
        data_inferensi.append((a4, z4))
        return data_inferensi

    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a