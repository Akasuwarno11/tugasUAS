from tkinter import Y
from unittest import result


def turun(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def naik(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

def sangat_rendah(y, ysr, yr):
    return (y - ysr) / (yr - ysr)


def rendah(y, yr, ys):
    return (y - yr) / (ys - yr)

def standar(y, ys, yt):
    return (y - ys) / (yt - ys)


def tinggi(y, yt, yst):
    return (y - yt) / (yst - yt)


def sangar_tinggi(y, yt, yst):
    return (y - yt) / (yst - yt)


class nilai_harian():
    minimum = 50
    maximum = 90

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


#sangat rendah =sr
#rendah = r
#standar = s
#tinggi = t
#sangat tinggi = s

class nilai_kelompok():
    sangat_rendah = 50
    rendah = 60
    standar = 70
    tinggi = 80
    atas = 90

    def sangat_rendah(self, y):
        if y >= self.rendah or y<= self.sangat_rendah:
            return 0
        elif self.sangat_rendah < y < self.rendah:
            return up(y, self.sangat_rendah, self.standar)

        else:
            return 1
    
    def rendah(self, y):
        if y >= self.standar or y<= self.rendah:
            return 0
        elif self.sangat_rendah < y < self.rendah:
            return up(y, self.sangat_rendah, self.standar)
        elif self.standar < y < self.tinggi:
            return down(y, self.standar, self.tinggi)
        else:
            return 1
    
    def standar(self, y):
       if y >= self.tinggi or y<= self.standar:
             return down(y, self.standar, self.tinggi)
        else:
            return 1
        

    
    def tinggi(self, y):
    if y >= self.tinggi or y<= self.standar:
            return down(y, self.standar, self.tinggi)
        else:
            return 1
            
    


class nilai_akhir():
    minimum = 50
    maximum = 90
  nilai_harian = 0
  nilai_kelompok = 0

    def _menurun(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _meningkat(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(self, nh=nilai_harian(), nk=nilai_kelompok()):
        result = []
        # [R1] JIKA nilai harian turun, dan nilai kelompok sangat rendah, MAKA
        # nilai akhir menurun.
        a1 = min(nh.turun(self.nilai_harian), nk.sangat_rendah(self.nilai_kelompok))
        z1 = self._menurun(a1)
        result.append((a1, z1))
        # [R2] JIKA nilai harian TURUN, dan nilai kelompok rendah, MAKA
        # nilai akhir menurun.
        a2 = min(nh.turun(self.nilai_harian), nk.rendah(self.nilai_kelompok))
        z2 = self._menurun(a2)
        result.append((a2, z2))
        # [R3] JIKA nilai harian TURUN, dan nilai kelompok standar, MAKA
        # nilai akhir menurun.
        a3 = min(nh.turun(self.nilai_harian), nk.standar(self.nilai_kelompok))
        z3 = self._menurun(a3)
        result.append((a3, z3))
          # [R4] JIKA nilai harian TURUN, dan nilai kelompok tinggi, MAKA
        # nilai akhir meningkat.
        a4 = min(nh.turun(self.nilai_harian), nk.tinggi(self.nilai_kelompok))
        z4 = self._meningkat(a4)
        result.append((a4, z4))
        # [R5] JIKA nilai harian TURUN, dan nilai kelompok sangat tinggi, MAKA
        # nilai akhir meningkat.
        a5 = min(nh.turun(self.nilai_harian), nk.sangat_tinggi(self.nilai_kelompok))
        z5 = self._meningkat(a5)
        result.append((a5, z5))
        # [R6] JIKA nilai harian naik, dan nilai kelompok sangat_rendah, MAKA
        # nilai akhir menurun.
        a6 = min(nh.naik(self.nilai_harian), nk.sangat_rendah(self.nilai_kelompok))
        z6 = self._menurun(a6)
         result.append((a6, z6))
         # [R7] JIKA nilai harian naik, dan nilai kelompok rendah, MAKA
        # nilai akhir menurun.
        a7 = min(nh.naik(self.nilai_harian), nk.rendah(self.nilai_kelompok))
        z7 = self.menurun(a7)
         result.append((a7, z7))
         # [R8] JIKA nilai harian naik, dan nilai kelompok standar, MAKA
        # nilai akhir bertambah.
        a8 = min(nh.naik(self.nilai_harian), nk.standar(self.nilai_kelompok))
        z8 = self.meningkat(a8)
        result.append((a8, z8))
         # [R9] JIKA nilai harian naik, dan nilai kelompok tinggi, MAKA
        # nilai akhir bertambah.
        a9 = min(nh.naik(self.nilai_harian), nk.tinggi(self.nilai_kelompok))
        z9 = self._bertambah(a9)
        result.append((a9, z9))
         # [R10] JIKA nilai harian naik, dan nilai kelompok sangat_tinggi, MAKA
        # nilai akhir bertambah.
        a10 = min(nh.naik(self.nilai_harian), nk.tinggi(self.nilai_kelompok))
        z10 = self._bertambah(a9)
        result.append((a10, z10))
        return data_inferensi:
        return result():
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4+a5*z5+α6∗z6+α7∗z7+α8∗z8+α9∗z9+a10*z10) / (α1+α2+α3+α4+a5+a6+a7+a8+a9+a10)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a