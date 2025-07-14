import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from default_gui_standars import Ui_Dialog
from tabla_materiales import Ui_Dialog as UiTablaMateriales
from tabla_presiones_hidrostaticas import Ui_Dialog as UiTablaPresionesHidrostaticas

class GUI(QMainWindow,Ui_Dialog):  # Cambiar la herencia a QMainWindow
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.config_widgets()
        
    def config_widgets(self):
        #self.config_entrys()
        self.config_botones()

    def config_botones(self):
        self.pb_material.clicked.connect(self.abrir_tabla_materiales)
        self.pb_tipo_presion.clicked.connect(self.seleccionar_presion)
        self.pb_tipo_recipiente.clicked.connect(self.seleccionar_recipiente)
        self.pb_orientacion_recipiente.clicked.connect(self.seleccionar_orientacion)
        self.pb_eficiencia_soldadura.clicked.connect(self.seleccionar_eficiencia_soldadura)
        self.pb_presiones_hidrostaticas.clicked.connect(self.abrir_tabla_presiones_hidrostaticas)

    def abrir_tabla_presiones_hidrostaticas(self):
        self.tabla_presiones_hidrostaticas = QMainWindow()
        self.ui_tabla_presiones_hidrostaticas = UiTablaPresionesHidrostaticas()
        self.ui_tabla_presiones_hidrostaticas.setupUi(self.tabla_presiones_hidrostaticas)
        self.tabla_presiones_hidrostaticas.show()

    def abrir_tabla_materiales(self):
        self.tabla_materiales = QMainWindow()
        self.ui_tabla_materiales = UiTablaMateriales()
        self.ui_tabla_materiales.setupUi(self.tabla_materiales)
        self.tabla_materiales.show()

    def seleccionar_eficiencia_soldadura(self):
        if self.pb_eficiencia_soldadura.text() == "1":
            self.pb_eficiencia_soldadura.setText("0.7")
        elif self.pb_eficiencia_soldadura.text() == "0.7":
            self.pb_eficiencia_soldadura.setText("0.85")
        else:
            self.pb_eficiencia_soldadura.setText("1")
        
    def seleccionar_presion(self):
        if self.pb_tipo_presion.text() == "Interna":
            self.pb_tipo_presion.setText("Externa")
        else:
            self.pb_tipo_presion.setText("Interna")

    def seleccionar_recipiente(self):
        if self.pb_tipo_recipiente.text() == "Cilíndrico":
            self.pb_tipo_recipiente.setText("Esférico")
        else:
            self.pb_tipo_recipiente.setText("Cilíndrico")
            
    def seleccionar_orientacion(self):
        if self.pb_orientacion_recipiente.text() == "Vertical":
            self.pb_orientacion_recipiente.setText("Horizontal")
        else:
            self.pb_orientacion_recipiente.setText("Vertical")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = GUI()
    mainWindow.show()
    sys.exit(app.exec_())