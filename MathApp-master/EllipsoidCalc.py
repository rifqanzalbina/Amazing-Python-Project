import math

class Ellipsoid:
    """  
    ! Class ini mempresentasikan sebuah ellipsoid dan menyediakan metode untuk menghitung karakteristik geometrisnya.
    ! Seperti luas permukaan dan volume tidak seperti ellipse sebuah ellipsoid tidak memiliki garis utama dan garis minor

    ! Attributes:
        ! semi_axis_a (float): Panjang dari titik tepi partama dari ellipsoid dalam cm.
        ! semi_axis_a (float): Panjang dari titik tepi kedua dari ellipsoid dalam cm.
        ! semi_axis_a (float): Panjang dari titik tepi ketiga dari ellipsoid dalam cm.
    """
    
    def __init__(self, semi_axis_a, semi_axis_b, semi_axis_c):
        """
        ! Menginisialisasi sebuah objek ellipsoid.

        ! Args:
            ! semi_axis_a (float): Positif panjang dari titik tepi pertama dari ellipsoid dalam cm.
            ! semi_axis_b (float): Positif panjang dari titik tepi kedua dari ellipsoid dalam cm.
            ! semi_axis_c (float): Positif panjang dari titik tepi ketiga dari ellipsoid dalam cm.

        ! Raises:
            ! TypeError: Jika salah satu sumbu semi bukan angka 
            ! ValueError: If any of the semi-axes are not positive.
        """
        if not isinstance(semi_axis_a, (int, float)):
            raise TypeError("Semi-axis a must be a number.")
        if semi_axis_a <= 0:
            raise ValueError("Semi-axis a must be positive.")
        if not isinstance(semi_axis_b, (int, float)):
            raise TypeError("Semi-axis b must be a number.")
        if semi_axis_b <= 0:
            raise ValueError("Semi-axis b must be positive.")
        if not isinstance(semi_axis_c, (int, float)):
            raise TypeError("Semi-axis c must be a number.")
        if semi_axis_c <= 0:
            raise ValueError("Semi-axis c must be positive.")
        self.semi_axis_a = semi_axis_a
        self.semi_axis_b = semi_axis_b
        self.semi_axis_c = semi_axis_c

    def surface_area(self):
        """
        ! Menghtiung dan mengembalikan luas permukaan dari ellipsoid

        ! Returns : 
            ! float: Luas permukan dari ellipsoid dalam cm^2.
        """
        surface_area = 4 * math.pi * pow((pow(self.semi_axis_a * self.semi_axis_b, 1.6075) + pow(self.semi_axis_a * self.semi_axis_c, 1.6075)
                                            + pow(self.semi_axis_b * self.semi_axis_c, 1.6075)) / 3, 1 / 1.6075);
        return round(surface_area, 5)
    
    def volume(self):
        """
        ! Menghitung dan mengembalikan volume dari ellipsoid dalma bentuk centimeters kuadrat.

        ! Formula / Rumus : 4 / 3 * PI * radius_a * radius_b * radius_c

        ! Mengembalikan
            ! Float : Volume dari ellipsoid di centimeters kuadrat, dibulatkan ke 5 angka di belakang koma.
            
        """
        volume = (4 / 3) * math.pi * self.semi_axis_a * self.semi_axis_b * self.semi_axis_c
        return round(volume, 5)

    def get_description(self):
        """
        ! Mengembalikan sebuah tuple yang berisi dua string yang menjelaskan keliling dan luas ellipse dalam cm dan cm^2

        ! Mengembalikan
            ! tuple[str, str]: Sebuah tuple yang berisik dua string yang menjelaskan keliling dan luas ellipse dan luas di centimer 
        """ 
        surface_area_info = "Surface area of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm2.".format(self.semi_axis_a, self.semi_axis_b, self.semi_axis_c, round(self.surface_area(), 3))
        volume_info = "Volume of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm3.".format(self.semi_axis_a, self.semi_axis_b, self.semi_axis_c, round(self.volume(), 3))
        return(surface_area_info, volume_info)