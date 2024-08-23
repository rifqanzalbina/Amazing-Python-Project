import math

class Ellipse:
    """
    ! Class ini mempresentasikan sebuah ellipse dan menyediakan metode untuk menghitung karakteristiknya, seperti jari jari dan luas elips.

    ! Attribut : 
        # ! Titik tepi axis (float) : Panjang dari titik tepi dari ellipse dalam cm.
        # ! Titik tepi axis (float) : Panjang dari titik tepi dari ellipse dalam
    """
    
    def __init__(self, semi_major_axis, semi_minor_axis):
        """
        ! Menginisialisasi sebuah Objek Ellipse.

        ! Args
            ! semi_major_axis (float): Panjang titik tepi axis ellipse dalam cm..
            ! semi_minor_axis (float): Positif panjang dari titik tepi axis ellipse dalam cm..
            

        ! Raises:
            ! TypeError: Jika salah satu axis panjang bukanlah sebuah angka.
            ! ValueError: Jika salah satu axis panjang tidak positif..
        """
        if not isinstance(semi_major_axis, (int, float)):
            raise TypeError("Titip tepi axis harus berupa angka..")
        if semi_major_axis <= 0:
            raise ValueError("Titik tepi  axis length harus bilangan positif..")
        if not isinstance(semi_minor_axis, (int, float)):
            raise TypeError("Titik tepi axis harus berupa angka.")
        if semi_minor_axis <= 0:
            raise ValueError("Titik tepi  axis harus bilangan positif..")
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def circumference(self):
        """
        ! Menghitung dan mengembalikan jari jari ellipse dalam bentuk cm.

        ! Rumus / Formula : Jari jari lingkaran / ellipse = 2 * PI

        ! Returns:

            ! float: Keliling dari ellipse dalam cm, dibulatkan ke 5 angka di belakang koma..

        """
        circumference =  math.pi * math.sqrt(2*(math.pow(self.semi_major_axis, 2) + math.pow(self.semi_minor_axis, 2)))
        return round(circumference,5)
    
    def area(self):
        """
        ! Menghitung dan mengembalikan luas ellipse dalam bentuk cm^2.

        ! Formula / Rumus : area * PI * a * b

        ! Returns:
            ! float: Luas dari ellipse dalam cm^2, dibulatkan ke 5 angka di belakang koma..
        """
        area = math.pi * self.semi_major_axis * self.semi_minor_axis
        return round(area,5)

    def get_description(self):
        """
        ! Mengembalikan sebuah tuple yang berisi dua string yang menjelaskan keliling dan luas ellipse dalam cm dan cm^2

        ! Returns:
            ! tuple[str, str]: Sebuah tuple yang berisi dua string yang menjelaskan keliling dan luas ellipse dalam cm dan cm^2 dan luas cm .
        """
        info_circumference = "Ellipse dengan axis {} dan {} cm memiliki keliling {:.3f} cm.".format(self.semi_major_axis, self.semi_minor_axis, round(self.circumference(), 3))
        info_area = "Ellipse dengan axis {} a {} cm dan memiliki luas {:.3f} cm2.".format(self.semi_major_axis, self.semi_minor_axis, round(self.area(), 3))
        return(info_circumference, info_area)
