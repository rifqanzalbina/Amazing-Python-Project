import os
import CheckCreateDirectory

from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
)


def save_fig(self, fig, name):
        """
        ! Menyimpan gambar saat ini sebagai file PNG.

        ! Metode ini meminta pengguna untuk memilih nama file dan lokasi penyimpana sebagai file PNGn
        """
        path = ".\\Results"
        CheckCreateDirectory.check_create_dir(path)

        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Figure', os.path.join(os.getcwd(), 'Results', name), 'PNG (*.png)')

        if file_name:
            try:
                fig.savefig(file_name)
                QMessageBox.information(self, 'Sukses', 'Gambar berhasil disimpan..')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Terjadi kesalahan saat menyimpan gambar: {e}')