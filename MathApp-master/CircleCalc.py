import math

class Circle:
    """
    ! Class Ini mempresentasikan sebuah lingkaran dan menyediakan metode untuk menghitung
    ! Ini properti seperti keliling, luas, dan informasi  deskripsi.

    ! Attribut
        ! radius (float): Jari jari lingkaran dalam sentimeter.
    """
    
    def __init__(self, radius):
        """
        ! Inisialisasi sebuah objek lingkaran.

        ! Argumen : 
            ! radius (float): Radius dari lingkaran dalam satuan centimeter
            
        ! Pengecualian:
            ! TypeError : Jika radius bukanlah sebuah angka.
            ! ValueError : Jika radius bukanlah sebuah angka positif.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius harus merupakan angka.")
        if radius <= 0:
            raise ValueError("Radius harus berupa angka yang positif.")
        self.radius = radius

    def circumference(self):
        """
        ! Menghitung dan mengembalikan keliling lingkaran.

        ! Rumus atau formula : Keliling = 2 * pi * radius

        ! Mengembalikan:
            ! float : Keliling dari lingkaran dalam centimeter, dibulatkan menjadi 5 angka desimal.
        """
        circumference = 2 * math.pi * self.radius
        return round(circumference,5)
    
    def area(self):
        """
        ! Menghitung dan mengembalikan luas lingkaran.

        ! Rumus / Formula : area = pi * radius^2

        ! Mengembalikan::
            ! float : Area dari lingkaran dalam centimeter persegi, dibulatkan menjadi 5 angka desimal.
        """
        area = math.pi * pow(self.radius, 2)
        return round(area,5)

    def get_description(self):
        """
        ! Mengembalikan sebuah tuple yang berisi dua string yang diformat untuk menjelaskan keliling dan luas lingkaran.

        ! Mengembalikan:
            tuple[str, str]: A tuple containing strings that describe the circle's circumference 
            ! tuple[str, str] : Sebuah tuple yang berisi string yang menjelaskan keliling dan luas lingkaran dan area yang user dapat baca
        """
        info_circumference = "Lingkaran dengan radius {} cm memiliki keliling {:.3f} cm.".format(self.radius, round(self.circumference(), 3))
        info_area = "Lingkaran dengan radius {} cm memiliki luas {:.3f} cm2.".format(self.radius, round(self.area(), 3))
        return(info_circumference, info_area)

# help(Circle)
