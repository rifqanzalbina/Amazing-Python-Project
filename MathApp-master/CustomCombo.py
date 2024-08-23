from PyQt5.QtWidgets import (
    QComboBox,
)

def custom_combo(self):
    """
    ! Membuat sebuah customize QComboBox baru widget dengan daftar warna yang telah ditentukan.
    ! Args:
      ! self: The parent widget. / Induk dari widget class

    ! Returns:
        ! QComboBox : Sebuah QComboBox widget yang telah diisi dengan opsi warna yang telah ditentukan..
    """

    # ! Membuat sebuah instance QComboBox baru dan menetapkan widget induknya
    custom_combo = QComboBox(self)

    # ! Mendefinisikan daftar nama warna untuk mengisi combo box baru
    colors = ["black", "blue", "gray", "green", "magenta",
              "orange", "pink", "red", "violet", "yellow"]
    
    # ! Menambahkan semua nama warna ke daftar item combo box baru
    custom_combo.addItems(colors)

    # ! Menetapkan lebar dan tinggi combo box secara fix agar tampilan teratur
    custom_combo.setFixedWidth(150)
    custom_combo.setFixedHeight(28)

    # ! Mengembalikan instance QComboBox baru
    return custom_combo