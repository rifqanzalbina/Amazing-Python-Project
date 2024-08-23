from PyQt5.QtWidgets import (
    QAction,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import (
    QDoubleValidator,
    QIcon,
    QRegExpValidator,
)  

import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np
import EllipsoidCalc
import CanvasThreeD
import SaveFig
from Shape import *

class WindowEllipsoid(QWidget, ShapeFunctionality):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        ! Menginisialisasi tampilan pengguna dari jendela

        ! Metode ini mengatur tata letak jendela, widget, dan hubungan antar mereka / method
        """
        # ! Membuat sebuah 3D Matplolib canvas untuk memplot lingkaran
        sc = CanvasThreeD.MplCanvas(self, width=6, height=5, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))
        
        # ! Tombmo untuk menyelesaikan dan melihat lingkarannya
        self.buttonplotEllipsoid = QPushButton('Selesai dan  Gambarkan')
        self.buttonplotEllipsoid.clicked.connect(lambda: self.plot_ellipsoid(sc, self.combo_color.currentText()))
        self.buttonplotEllipsoid.setToolTip("Selesai and gambarkan ")

        # ! Tombol untuk mengekspor dan menyimpan gambar
        self.buttonPicture = QPushButton('Expor Grafik')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipsoid.png'))
        self.buttonPicture.setEnabled(False)

        # ! Tombol untuk mengekspor data ke Excel
        self.buttonExport = QPushButton('Expor exel')
        # self.buttonExport.clicked.connect(lambda: self.export_excel())
        self.buttonExport.setEnabled(False)

        # ! Tombol untuk menghapus semua input, hasil, dan grafik
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(lambda: self.clear_inputs(sc))

        # ! Tombol untuk menutup jendela aplikasi
        self.buttonClose = QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        # ! Membuat sebuah toolbar untuk action yang sering digunakan
        toolbar = QToolBar()
        toolbar.setIconSize(QtCore.QSize(50, 50))

        self.setFixedSize(850, 568)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotEllipsoid)
        hbox2.addWidget(self.buttonPicture)
        hbox2.addWidget(self.buttonExport)
        hbox2.addWidget(self.buttonClear)
        hbox2.addWidget(self.buttonClose)

        # ! Membuat layout dan group box untuk parameter input
        layout_param = QGridLayout()
        groupBoxParameters = QGroupBox("Parameters")
        groupBoxParameters.setLayout(layout_param)

        # ! Membuat layout dan group box untuk hasil
        layout_res = QGridLayout()
        groupBoxResults = QGroupBox("Results")
        groupBoxResults.setLayout(layout_res)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(groupBoxParameters)
        vbox1.addWidget(groupBoxResults)
        vbox1.addStretch(1)

        # ! Membuat layout horizontal untuk grafik dan groupbox dengan input / hasil
        hbox1.addLayout(vbox1)
        hbox1.addWidget(sc)

        # ! Vertical box layout untuk : 
        # ! 1. Menu
        # ! 2. Box layout horizontal untuk vbox1 dengan groupbox dan grafik
        # ! 3. Box layout horizontal dengan tombol
        vbox2 = QVBoxLayout()
        vbox2.setMenuBar(toolbar)
        vbox2.addLayout(hbox1)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)

        self.setLayout(vbox2)
        self.setWindowTitle('Ellipsoid')

        validator_double = QDoubleValidator(-10000000,10000000,5)
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        validator_double.setLocale(locale)
        validator_double.setNotation(QDoubleValidator.StandardNotation)

        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))

        # ! Membuat bagian input untuk titik tepi axis (a)
        self.label_axis_a = QLabel("Semi axis (a):")
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

        # ! Membuat bagian input untuk titik tepi axis (b)
        self.label_axis_b = QLabel("Semi axis (b):")
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

        # ! Membuat bagian input untuk titik tepi axis (c)
        self.label_axis_c = QLabel("Semi axis (c):")
        self.label_axis_c.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_c.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_c,2,0)

        self.edit_axis_c = QLineEdit(self)
        self.edit_axis_c.setValidator(validator_possitive)
        self.edit_axis_c.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_c.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_c,2,1)

        self.label_dim_axis_c = QLabel("cm")
        self.label_dim_axis_c.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_c.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_c,2,2)

        # ! Membuat bagian input untuk koordinat tengah x₀
        self.label_centerX = QLabel("X coordinate (x₀):")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerX.setFixedWidth(150)
        layout_param.addWidget(self.label_centerX,3,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setValidator(validator_double)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerX.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerX,3,1)

        self.label_dim_x = QLabel("cm")
        self.label_dim_x.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_x.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_x,3,2)

        # ! Membuat bagian input untuk koordinat tengah y₀
        self.label_centerY = QLabel("Y coordinate (y₀):")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerY.setFixedWidth(150)
        layout_param.addWidget(self.label_centerY,4,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setValidator(validator_double)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerY.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerY,4,1)

        self.label_dim_y = QLabel("cm")
        self.label_dim_y.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_y.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_y,4,2)

        # ! Membuat bagian input untuk koordinat tengah z₀
        self.label_centerZ = QLabel("Z coordinate (z₀):")
        self.label_centerZ.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.label_centerZ,5,0)

        self.edit_centerZ = QLineEdit(self)
        self.edit_centerZ.setValidator(validator_double)
        self.edit_centerZ.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerZ,5,1)

        self.label_dim_z = QLabel("cm")
        self.label_dim_z.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_z.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_z,5,2)

        self.label_combo_color = QLabel("Warna Sphere :")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,6,0)


        self.label_combo_color = QLabel("Warna Ellipso : ")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,6,0)


        self.combo_color = QComboBox(self)
        colors = ["black", 
                  "blue", 
                  "gray", 
                  "green", 
                  "magenta", 
                  "orange", 
                  "pink", 
                  "red", 
                  "violet", 
                  "yellow"]
        self.combo_color.addItems(colors)
        self.combo_color.setFixedWidth(150)
        self.combo_color.setFixedHeight(28)
        layout_param.addWidget(self.combo_color,6,1)

        # ! Membuat bagian untuk hasil - Volume (V)
        self.label_volume = QLabel("Ellipsoid Volume:")
        self.label_volume.setAlignment(QtCore.Qt.AlignLeft)
        self.label_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_volume,0,0)

        self.label_res_volume = QLabel('0.0')
        self.label_res_volume.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_res_volume,0,1)

        self.label_dim_vol = QLabel("cm<sup>3</sup>")
        self.label_dim_vol.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_vol.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_vol,0,2)

        # ! Membaut bagian untuk hasil - Permukaan (A)
        self.label_surface = QLabel("Ellipsoid Surface:")
        self.label_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_surface,1,0)

        self.label_res_surface = QLabel('0.0')
        self.label_res_surface.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_res_surface,1,1)

        self.label_dim_surface = QLabel("cm<sup>2</sup>")
        self.label_dim_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_surface.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_surface,1,2)

        # ! Pecahkan dan gambarkan - tombol di toolbar atas
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Solve and plot picture")
        self.exportPictAction.setIcon(QIcon('CalculateIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: self.plot_ellipsoid(sc, self.combo_color.currentText()))
        toolbar.addAction(self.exportPictAction)

        # ! Mengekspor grafik sebagai gambar - tombol di toolbar atas
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Save graph as picture")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipsoid.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # ! Mengekspor inputs, hasil dan grafik kedalam File Excel - tombol di toolbar atas
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, hasil\ndan grafik kedalam Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        # self.exportXlsxAction.triggered.connect(self.export_excel)
        self.exportXlsxAction.setEnabled(False)
        toolbar.addAction(self.exportXlsxAction)

        # ! Menghapus semua input, hasil, dan grafik - tombol di toolbar atas
        # ! Tombol dimatikan, ketika hasil tidak bisa dihitung
        self.clearAction = QAction(self)
        self.clearAction.setToolTip("Hapus semua data dan hasil")
        self.clearAction.setIcon(QIcon('ClearResultsIcon.svg'))
        self.clearAction.triggered.connect(lambda: self.clear_inputs(sc))
        self.clearAction.setEnabled(False)
        toolbar.addAction(self.clearAction)

        # ! Menutup jendel - - tombol ada di toolbar atas
        self.closeAction = QAction(self)
        self.closeAction.setToolTip("Tutup Jendela")
        self.closeAction.setIcon(QIcon('CloseAppIcon.svg'))
        self.closeAction.triggered.connect(self.close)
        toolbar.addAction(self.closeAction)

        self.edit_axis_a.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_a.textChanged.emit(self.edit_axis_a.text())

        self.edit_axis_b.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_b.textChanged.emit(self.edit_axis_b.text())

        self.edit_axis_c.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_c.textChanged.emit(self.edit_axis_c.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.edit_centerZ.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerZ.textChanged.emit(self.edit_centerZ.text())


    def plot_ellipsoid(self, sphere_plot, circle_color):
        
        sphere_plot.axes.cla()
        sphere_plot.draw()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        

        if self.edit_axis_a.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Titik Tepi (a) hanya dapat berupa bilangan positif : ")

        elif self.edit_axis_b.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Titik Tepi (b) hanya dapat berupa bilangan positif :")

        elif self.edit_axis_c.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Titik Tepi (c) hanya dapat berupa bilangan positif :")

        elif self.edit_centerX.text() in ["", "+", "-"]:
            self.custom_messagebox("X Koordinat (x₀) tidak ditemukan")

        elif self.edit_centerY.text() in ["", "+", "-"]:
            self.custom_messagebox("Y Koordinat (y₀) tidak ditemukan")

        elif self.edit_centerZ.text() in ["", "+", "-"]:
            self.custom_messagebox("Z Koordinat (z₀) tidak ditemukan")
 
        else:

            center_x = float(self.edit_centerX.text())
            center_y = float(self.edit_centerY.text())
            center_z = float(self.edit_centerZ.text())
            rx = float(self.edit_axis_a.text())
            ry = float(self.edit_axis_b.text())
            rz = float(self.edit_axis_c.text())

            u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
            
            x = rx * np.outer(np.cos(u), np.sin(v)) + center_x
            y = ry * np.outer(np.sin(u), np.sin(v)) + center_y
            z = rz * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z

            minus_x = float(self.edit_centerX.text())-1.5*float(self.edit_axis_a.text())
            plus_x = float(self.edit_centerX.text())+1.5*float(self.edit_axis_a.text())
            minus_y = float(self.edit_centerY.text())-2*float(self.edit_axis_b.text())
            plus_y = float(self.edit_centerY.text())+2*float(self.edit_axis_b.text())
            minus_z = float(self.edit_centerZ.text())-2*float(self.edit_axis_c.text())
            plus_z = float(self.edit_centerZ.text())+2*float(self.edit_axis_c.text())

            sphere_plot.axes.set_xlim(minus_x, plus_x)
            sphere_plot.axes.set_ylim(minus_x, plus_x)
            sphere_plot.axes.set_zlim(minus_x, plus_x)

            sphere_plot.axes.plot_wireframe(x, y, z, rstride=20, cstride=20, color=circle_color)
            sphere_plot.draw()

            self.fig = sphere_plot.figure

            self.calculate_ellipsoid()

            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)


    def calculate_ellipsoid(self):

        semi_axis_a = float(self.edit_axis_a.text())
        semi_axis_b = float(self.edit_axis_b.text())
        semi_axis_c = float(self.edit_axis_c.text())

        myEllipsoid = EllipsoidCalc.Ellipsoid(semi_axis_a, semi_axis_b, semi_axis_c)
        ellipsoid_volume = round(myEllipsoid.volume(),5)
        ellipsoid_surface = round(myEllipsoid.surface_area(),5)

        self.label_res_volume.setText(str(ellipsoid_volume))
        self.label_res_surface.setText(str(ellipsoid_surface))


    def clear_inputs(self, sc):
        sc.axes.cla()
        sc.draw()
        self.edit_axis_a.clear()
        self.edit_axis_b.clear()
        self.edit_axis_c.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.edit_centerZ.clear()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)

    
    def clear_results(self, sc):
        """
        ! Menghapus semua input, hasil, dan grafik - tombol di toolbar atas 

        ! Metode ini menghapus text di radius, koordinat x, dan koordinat y.
        ! Kolom sama seperti kolom hasil untuk diameter, keliling dan luas
        ! Dan juga menghapus ploting di Matplotlib Canvas.

        ! Args:
            ! sc: The Matplotlib canvas object digunakan untuk plotting.
        """
        sc.axes.cla()
        sc.draw()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)
        
      