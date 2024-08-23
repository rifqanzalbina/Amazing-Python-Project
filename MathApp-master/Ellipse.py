import os

from PyQt5.QtWidgets import (
    QAction, 
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import (
    QValidator,
    QIcon,
    QRegExpValidator,
)

import matplotlib
matplotlib.use('Qt5Agg')


from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.patches import Ellipse

import EllipseCalc
import Canvas
import SaveFig
from Shape import *
from CustomCombo import *

class WindowEllipse(QWidget, ShapeFunctionality):
    """
    ! Class ini mempresentasikan jendela / window utama dari perhitungan aplikasi lingkaran

    ! Mengendalikan penampilan antarmuka pengguna, validasi masukan, logika perhitungan,
    ! dan interaksi dengan external library untuk plotting dan data export.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        ! Menginisialisasi antarmuka pengguna dari jendela / window.

        ! Metode ini mengatur tata letak jendela / window, widget, dan hubungan antar mereka.
        """
        # ! Membuat sebuah matplotlib canvas untuk menampilkan lingkaran
        sc = Canvas.MplCanvas(self, width=6, height=6, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))

        # ! Tombol untuk menyelesaikan dan melihat
        self.buttonplotEllipse = QPushButton('Solve and Plot')
        self.buttonplotEllipse.clicked.connect(lambda: self.plot_ellipse(sc, self.combo_color.currentText()))
        self.buttonplotEllipse.setToolTip("Solve and plot picture")

        # ! Tombol untuk mengekspor grafik sebagai gambar
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipse.png'))
        self.buttonPicture.setEnabled(False)

        # ! Tombol untuk mengekspor data sebagaike Excel
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel())
        self.buttonExport.setEnabled(False)

        # ! Tombol untuk menghapus semua input, hasil, dan grafik
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(lambda: self.clear_inputs(sc))
        self.buttonClear.setEnabled(False)

        # ! Tombol untuk menutup jendela / window
        self.buttonClose = QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        # ! Membuat sebuah toolbar untuk kegiatan yang sering digunakan
        toolbar = QToolBar()
        toolbar.setIconSize(QtCore.QSize(50, 50))

        # ! Mengatur ukuran jendela / window
        self.setFixedSize(850, 488)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotEllipse)
        hbox2.addWidget(self.buttonPicture)
        hbox2.addWidget(self.buttonExport)
        hbox2.addWidget(self.buttonClear)
        hbox2.addWidget(self.buttonClose)


        # ! Membuat layout dan group box untuk parameter input(masukkan)
        layout_param = QGridLayout()
        groupBoxParameters = QGroupBox("Parameters")
        groupBoxParameters.setLayout(layout_param)

        # ! Membaut layout dan group box untuk hasil perhitungan
        layout_res = QGridLayout()
        groupBoxResults = QGroupBox("Results")
        groupBoxResults.setLayout(layout_res)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(groupBoxParameters)
        vbox1.addWidget(groupBoxResults)
        vbox1.addStretch(1)

        # ! Membuat horizontal layout untuk grafik dan group box dengan input / hasil
        hbox1.addLayout(vbox1)
        hbox1.addWidget(sc)

        # ! Vertical box layout untuk : 
        # ! 1. Menu
        # ! 2. Horizontal box layout untuk vbox1 dengan groupboxes dan grafik
        # ! 3. Horizontal box layout dengan tombol
        vbox2 = QVBoxLayout()
        vbox2.setMenuBar(toolbar)
        vbox2.addLayout(hbox1)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)

        self.setLayout(vbox2)
        self.setWindowTitle('Ellipse')  

        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        
        # ! Membuat kolom input untuk titik pusat axis (a)
        self.label_axis_a = QLabel("Titik tepi axis (a):")
        self.label_axis_a.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_a.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_a,0,0)

        self.edit_axis_a = QLineEdit(self)
        self.edit_axis_a.setValidator(validator_possitive)
        self.edit_axis_a.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_a.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_a,0,1)

        self.label_dim_axis_a = QLabel("cm")
        self.label_dim_axis_a.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_a.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_a,0,2)

        # ! Membuat kolom input untuk titik pusat axis (b)
        self.label_axis_b = QLabel("Titik tepi axis (b):")
        self.label_axis_b.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_b.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_b,1,0)

        self.edit_axis_b = QLineEdit(self)
        self.edit_axis_b.setValidator(validator_possitive)
        self.edit_axis_b.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_b.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_b,1,1)

        self.label_dim_axis_b = QLabel("cm")
        self.label_dim_axis_b.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_b.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_b,1,2)

        # ! Membuat kolom input dari koordinat titik tepi x₀
        self.label_centerX = QLabel("X Koordinat (x₀):")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerX.setFixedWidth(150)
        layout_param.addWidget(self.label_centerX,2,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setValidator(validator_double)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerX.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerX,2,1)

        self.label_dim_x = QLabel("cm")
        self.label_dim_x.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_x.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_x,2,2)

        # ! Membuat kolom input dari koordinat titik tepi y₀
        self.label_centerY = QLabel("Y Koordinat (y₀):")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerY.setFixedWidth(150)
        layout_param.addWidget(self.label_centerY,3,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setValidator(validator_double)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerY.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerY,3,1)

        self.label_dim_y = QLabel("cm")
        self.label_dim_y.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_y.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_y,3,2)

        self.label_combo_color = QLabel("Warna Ellips : ")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,4,0)

        # ! Membuat kombinasi untuk warna ellips
        self.combo_color = custom_combo(self)
        layout_param.addWidget(self.combo_color,4,1)
         
        # ! Membuat kolom untuk hasil - keliling (c)
        self.label_perimeter = QLabel("Circumference (c):")
        self.label_perimeter.setAlignment(QtCore.Qt.AlignLeft)
        self.label_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_perimeter,0,0)

        self.label_res_perimeter = QLabel('0.0')
        self.label_res_perimeter.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_res_perimeter,0,1)

        self.label_dim_per = QLabel("cm")
        self.label_dim_per.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_per.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_per,0,2)

        # ! Membuat kolom untuk hasil - luas (A)
        self.label_area = QLabel("Area (A):")
        self.label_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_area.setFixedWidth(150)
        layout_res.addWidget(self.label_area,1,0)

        self.label_res_area = QLabel('0.0')
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)

        # ! Memecahkan dan menampilkan grafik lingkaran - tombol di toolbar atas
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Tentukan dan gambarkan grafik")
        self.exportPictAction.setIcon(QIcon('CalculateIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: self.plot_circle(sc, self.combo_color.currentText()))
        toolbar.addAction(self.exportPictAction)

        # ! Mengekspor grafik sebagai gambar PNG - tombol berada di toolbar atas
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Simpan grafik sebagai gambar")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Circle.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # ! Mengekspor input, hasil dan grafik ke dalam file excel - tombol berada di toolbar atas
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, results\nand graph into Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        self.exportXlsxAction.triggered.connect(self.export_excel)
        self.exportXlsxAction.setEnabled(False)
        toolbar.addAction(self.exportXlsxAction)

        # ! Menghapus semua input, hasil dan grafik - tombol di toolbar atas
        # ! Tombol di matikan, ketika hasil tidak bisa dihitung
        self.clearAction = QAction(self)
        self.clearAction.setToolTip("Clear all data and results")
        self.clearAction.setIcon(QIcon('ClearResultsIcon.svg'))
        self.clearAction.triggered.connect(lambda: self.clear_inputs(sc))
        self.clearAction.setEnabled(False)
        toolbar.addAction(self.clearAction)

        # ! Menutup Jendela - - tombol berada di atas toolbar
        self.closeAction = QAction(self)
        self.closeAction.setToolTip("Menutup Jendela")
        self.closeAction.setIcon(QIcon('CloseAppIcon.svg'))
        self.closeAction.triggered.connect(self.close)
        toolbar.addAction(self.closeAction)

        self.edit_axis_a.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_a.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_axis_a.textChanged.emit(self.edit_axis_a.text())

        self.edit_axis_b.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_b.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_axis_b.textChanged.emit(self.edit_axis_b.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.combo_color.currentIndexChanged.connect(lambda: self.clear_results(sc))


    def plot_ellipse(self, ellipse_plot, ellipse_color):
        
        ellipse_plot.axes.cla()
        ellipse_plot.draw()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")

        if self.edit_axis_a.text() == "0" or self.edit_axis_a.text() == "":
            self.custom_messagebox("Titik tepi axis (a) hanya berupa angka positif ! ")

        elif self.edit_axis_b.text() == "0" or self.edit_axis_b.text() == "":
            self.custom_messagebox("Titik tepi axis (b) hanya berupa angka positif : ")

        elif self.edit_centerX.text() == "":
            self.custom_messagebox("X Koordinat (x₀) tidak ditemukan!")

        elif self.edit_centerY.text() == "":
            self.custom_messagebox("Y coordinate (y₀) tidak ditemukan!")

        else:

            Drawing_colored_ellipse = Ellipse((float(self.edit_centerX.text()),(float(self.edit_centerY.text()))),2*float(self.edit_axis_a.text()),2*float(self.edit_axis_b.text()))
            Drawing_colored_ellipse.set_color(ellipse_color)

            minus_x = float(self.edit_centerX.text())-2*float(self.edit_axis_a.text())
            plus_x = float(self.edit_centerX.text())+2*float(self.edit_axis_a.text())
            minus_y = float(self.edit_centerY.text())-2*float(self.edit_axis_b.text())
            plus_y = float(self.edit_centerY.text())+2*float(self.edit_axis_b.text())

            ellipse_plot.axes.set_xlim(minus_x, plus_x)
            ellipse_plot.axes.set_ylim(minus_y, plus_y)

            ellipse_plot.axes.add_artist(Drawing_colored_ellipse)
            ellipse_plot.draw()

            self.fig = ellipse_plot.figure

            self.calculate_ellipse()
            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)

    def calculate_ellipse(self):

        axis_a = float(self.edit_axis_a.text())
        axis_b = float(self.edit_axis_b.text())
        myEllipse = EllipseCalc.Ellipse(axis_a, axis_b)
        ellipse_perimeter = round(myEllipse.circumference(),5)
        ellipse_area = round(myEllipse.area(),5)

        self.label_res_perimeter.setText(str(ellipse_perimeter))
        self.label_res_area.setText(str(ellipse_area))


    def clear_inputs(self, sc):
        """
        ! Menghapus semua masukkan , hasil , dan grafik.

        ! Metode ini mengatur ulang teks di kolom a, b, x koordinat, dan y
        ! Kolom input serta kolom hasil untuk keliling, dan luas."
        # ! Itu juga menghapus grafik di Matplotlib canvas.

        # ! Args:
            ! sc : Matplotlib canvas object digunakan untuk plotting.
        """
        sc.axes.cla()
        sc.draw()
        self.edit_axis_a.clear()
        self.edit_axis_b.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)

    def clear_results(self, sc):
        """
        ! Menghapus semua input, hasil dan juga grafik

        ! Metode ini menghapus text di kolom a axis, b axis, koordinat x, dan koordinat y.
        ! Kolom input serta kolom hasil untuk keliling, dan luas.
        
        ! Ini juga menghapus grafik di matplolib canvas.

        ! Args
            ! sc: The Matplotlib canvas objec digunakan untuk plotting.
        """
        sc.axes.cla()
        sc.draw()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)
    
    def export_excel(self):

        # ! Membuat filenama custom untuk pengguna
        file_name, _ = QFileDialog.getSaveFileName(self, 'Export ke Excel', os.path.join(os.getcwd(), 'Hasilnya', 'ellipse.xlsx'), 'Excel (*.xlsx)')

        if not file_name:
            return  # ! User membatalkan pilihan file dialog 

        try:
            # ! Importing necessary libraries

            # ! Membuaut pandas DataFrame Objects.
            data = {
            'Property': [self.label_axis_a.text(),
                        self.label_axis_b.text(),
                        self.label_centerX.text(),
                        self.label_centerY.text()],
            'Value': [float(self.edit_axis_a.text()),
                    float(self.edit_axis_b.text()), 
                    float(self.edit_centerX.text()),
                    float(self.edit_centerY.text())],
            'Unit': ['cm', 
                    'cm',
                    'cm',
                    'cm']
            }

            results = {
            'Result': [self.label_perimeter.text(),
                        self.label_area.text()],
            'Value': [float(self.label_res_perimeter.text()), 
                    float(self.label_res_area.text())],
            'Unit': ['cm', 
                    'cm^2']
            }
            
            df = pd.DataFrame(data)
            df_res = pd.DataFrame(results)

            # ! Membuat Penulis Excel dengan nama file custom 
            writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
            workbook = writer.book
            worksheet = workbook.add_worksheet('Ellipse Calculation')

            # ! Menulis data ke Excel
            df.to_excel(writer, sheet_name='Ellipse Calculation', startrow=0, startcol=0)
            df_res.to_excel(writer, sheet_name='Ellipse Calculation', startrow=6, startcol=0)

            # ! Menyimpan gambar (anggaplah self.fig itu sebuah Figur dari Matplotlib)
            self.fig.savefig(f'.\\Results\\ellipse_plot.png')  # ! Tambahkan path ke direktori jika diperlukan 
            worksheet.insert_image('F2', f'.\\Results\\ellipse_plot.png')  # ! Tambahkan cell koordinat untuk menyimpan 
            writer.close()

            QMessageBox.information(self, 'Sukses', 'Data berhasil diexport ke Excel')

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Terjadi sebuah kesalah ketika mengekspor data ke Excel, Error : {e}')