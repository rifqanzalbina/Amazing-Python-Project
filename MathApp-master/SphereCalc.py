import math

class Sphere:
    """
    ! Class ini mempresentasikan sebuah bola dan menyediakan metode untuk menghitung !
    ! Propertti seperti luas permukaan, volume, dan deskripsi string informatif !
    ! Attributes:
        ! radius (float): Radius dari bola dalam cm.
    """
    
    def __init__(self, radius):
        """
        # ! Menginisialisasi sebuah objel bola

        ! Args:
            ! radius (float): Radius dari bola dalam satuan cm.

        ! Raises:
            ! TypeError : Jika radius bukan angka.
            ! ValueError: Jika radius tidak bernilai positif.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius hanya berupa sebuah angka..")
        if radius <= 0:
            raise ValueError("Radius hanya berupa sebuah angka positif.")
        self.radius = radius

    def surface_area(self):
        """
        ! Menghitung dan mengembalikan luas permukaan bola.

        ! Formula : Luas permukaan * 4 * pi * radius^2

        ! Returns:
           ! float: Luas permukaan bola dalam square centimeters, dibulatkan ke 5 angka di belakang koma.
        """
        surface_area = 4 * math.pi * pow(self.radius,2)
        return round(surface_area,5)
    
    def volume(self):
        """
        ! Menghitung dan mengembalikan volume bola.

        ! Formula / Rumus = 4/3 * pi * radius^3 

        Returns:
            ! float : Volume dari bulat  dalam bentuk cubic centimeters dan dibulatkan ke 5 angka di belakang koma.
        """
        volume = (4.0 / 3.0) * math.pi*pow(self.radius, 3) 
        return round(volume,5)

    def get_description(self):
        """
        ! Mengembalikan sebuah tuple yang berisi dua string yang menjelaskan luas permukaan dan volume.! 

        ! Returns
            ! tuple[str, str] : Sebuah tuple yang berisi dua string yang menjelaskan luas permukaan dan volume dari bola.
            ! di sebuah format yang mudah dimengerti.
        """
        surface_area_info = "Sphere dengan radius {} cm memiliki luas permukaan {:.3f} cm2.".format(self.radius, round(self.surface_area(),3))
        volume_info = "Sphere dengan radius {} cm memiliki volume. {:.3f} cm3.".format(self.radius, round(self.volume(),3))
        return(surface_area_info, volume_info)

# help(Sphere)
