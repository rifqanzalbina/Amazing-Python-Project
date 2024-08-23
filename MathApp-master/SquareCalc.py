class Square:
    """
    ! Class ini mempresentasikan sebuah kotak dan menyeediakan metode perhitungan , propertis seperti, perimeter, luas dan informasi deskripsi string.

    ! Attribut : 
        ! side_length (float): Panjang sisi dari kotak dalam cm.
    """
    
    def __init__(self, side_length):
        """
        ! Menginisialisasi sebuah Objek Kotak.

        ! Args:
            ! side_length (float) : Panjang sisi dari kotak dalam cm.

        ! Raises:
            ! TypeError: Jika panjang sisi bukanlah sebuah angka.
            ! ValueError: Jika panjang sisi bukan sebuah bilangan positif.
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("Panjang sisi haruslah berupa angka.")
        if side_length <= 0:
            raise ValueError("Panjang sisi harushlah berupa angka positif.")
        self.side_length = side_length

    def circumference(self):
        """
        ! Menghitung dan mengembalikan Keliling (perimeter) of the square. 

        ! Rumus : Keliling = 4 * sisi / side_length

        Returns:
            ! float: Keliling (parimeter) dari kotak dalam cm. dibulatkan ke angka 5 dibelakang koma. 
        """
        circumference = 4 * self.side_length
        return round(circumference,5)
    
    def area(self):
        """
        ! Menghitung dan mengembalikan luas (area) dari kotak.

        ! Formula  / Rumus = luas * sisi^2

        Returns:
            ! float: Luas dari kotak di kuadratkan menjadi  cm^2 dan dibulatkan menjadi 5 angka dibelakang koma. 
        """
        area = pow(self.side_length, 2)
        return round(area,5)

    def get_description(self):
        """
        ! Mengembalikan sebuah tuple yang berisi dua string yang menjelaskan kotak dengan panjang sisi tertentu. keliling dan luas secara bersamaan.

        Returns:
            tuple[str, str]: Sebuah tuple berisikan string mendeskripsikan keliling dan luas kotak dengan panjang sisi tertentu. dan luas di beberapa format yang mudah dimengerti.
        """
        info_circumference = "Square with side length {} cm has circumference {} cm.".format(self.side_length, round(self.circumference(), 3))
        info_area = "Square with side length {} cm has area {} cm2.".format(self.side_length, round(self.area(), 3))
        return(info_circumference, info_area)
    
# help(Square)
