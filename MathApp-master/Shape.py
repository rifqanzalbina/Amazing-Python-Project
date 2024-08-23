from PyQt5.QtWidgets import (
    QMessageBox,
)

from PyQt5.QtGui import (
    QValidator,
)

from PyQt5.QtGui import (
    QPixmap,
)

class ShapeFunctionality:

    def custom_messagebox(self, text="Error!"):
        messagebox = QMessageBox(QMessageBox.Warning, "Error", text, buttons = QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap('stop_writing.png'))
        messagebox.exec_()

    def check_state_and_set_color(self, sender):
        """
        ! Fungsi ini mengecek validasi state dari QLineEdit sender dan mengatur background color sesuai dengan state tersebut.

        ! Args:
            ! sender (QtWidgets.QLineEdit): QLineEdit widget yang peru diperiksa dan warna yang dibutuhkan untuk update..
        """
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        color = '#f6989d'  # Warna Sebelumnya  (red)

        if sender.text() == "":
            color = '#f6989d'  # ! Kolom kosong ditandain warna merah
        elif state == QValidator.Acceptable or sender.text() == "0":
            color = '#c4df9b'  # ! Input valid diwarnai hijau
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # ! Keadaan menengah berubah menjadi kuning

        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
    
    def check_state_rad_and_set_color(self, sender):
        """
        ! Fungsi ini mengecek validasi state dari QLineEdit sender dan mengatur background color sesuai dengan state

        Args:
        ! Args : 
            ! sender (QtWidgets.QLineEdit): The QLineEdit widget dengan state dan warna yang perlu diperbarui..
        """
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]

        if sender.text() == "0" or sender.text() == "":
            color = '#f6989d' # ! Kosong atau "0" kolom tetap merah
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # ! Nilai masukkan valid berubah hijau
        elif state == QValidator.Intermediate:
            color = '#fff79a' # Intermediate state turns yellow
            color = '#fff79a' # 
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)