class Cube:
    """
    ! Class ini mempresentasikan sebuah kubus 3D dan menyediakan metode untuk menghitung sifat - sifat geometrisny seperti luas permukaan dan volume.

    ! Attribut : 
        ! Panjang sisi (float) : Panjang sisi kubus dalam satuan cm. 
    """
    
    def __init__(self, side_length):
        """
        ! Menginitialisasi sebuah Objek Kubus

        ! Argumen : 
            ! Panjang sisi / side_length (float) : Panjang sisi kubus dalam satuan cm.
            
        ! Pengecualian
            ! TypeError : Jika side_length / panjang sisi bukanlah angka. 
            ! ValueError : Jika side_length / panjang sisi tidak positif. 
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length / panjang sisi harus berupa angka..")
        if side_length <= 0:
            raise ValueError("Side length / panjang sisi harus bilangan positif...")
        self.side_length = side_length

    def surface_area(self):
        """
        ! Menghitung dan mengembalikan total luas permukaan kubus dalam satuan kuadrat cm.
        
        !Formula / Rumus : luas permukaan = 6 * side_length^2 / panjang_sisi^2

        ! Mengembalikan
            ! float : Luas permukaan kubus dalam satuan kuadrat cm, dibulatkan ke 5 angka di belakang koma. 
        """
        surface_area = 6 * pow(self.side_length,2)
        return round(surface_area, 5)
    
    def volume(self):
        """
        ! Menghitung dan mengembalikan volume kubus dalam satuan kubik cm

        ! Rumus / Formula : volume * side_length^3 / panjang_sisi^3

        ! Mengembalikan
            ! float : Volume kubus dalam satuan kubik cm, dibulatkan ke 5 angka di belakang koma.
        """
        volume = pow(self.side_length, 3)
        return round(volume, 5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the cube's surface area and volume.
        ! Mengembalikan sebuah tuple yang berisi dua string yang menjelaskan luas permukaan dan volume kubus dalam satuan kuadrat dan kubik cm.

        ! Mengembalikan :
            ! tuple[str, str]: Sebuah tuple yang berisi dua string yang menjelaskan luas permukaan dan volume kubus dalam satuan kuadrat dan kubik cm.
        """
        surface_area_info = "Kubus dengan panjang sisi {} cm memiliki luas permukaan {} cm2.".format(self.side_length, round(self.surface_area(),3))
        volume_info = "Kubus dengan panjang sisi {} cm memiliki volume {} cm3.".format(self.side_length, round(self.volume(),3))
        return(surface_area_info, volume_info)

# help(Cube)