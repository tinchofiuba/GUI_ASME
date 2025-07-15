import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import platform

from PyQt5.QtWidgets import QApplication, QMainWindow

from default_gui_standars import Ui_Dialog as UiMain
from tabla_materiales import Ui_Dialog as UiTablaMateriales
from tabla_presiones_hidrostaticas import Ui_Dialog as UiTablaPresionesHidrostaticas
from model import Model

class GUI(QMainWindow,UiMain): 
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.config_widgets()
        self.model = Model(self)
        
    def config_widgets(self):
        #self.config_entrys()
        self.config_botones()

    def botones_envolvente(self):
        self.pb_material.clicked.connect(self.abrir_tabla_materiales)
        self.pb_tipo_presion.clicked.connect(self.seleccionar_presion)
        self.pb_tipo_recipiente.clicked.connect(self.seleccionar_recipiente)
        self.pb_orientacion_recipiente.clicked.connect(self.seleccionar_orientacion)
        self.pb_eficiencia_soldadura.clicked.connect(self.seleccionar_eficiencia_soldadura)
        self.pb_presiones_hidrostaticas.clicked.connect(self.abrir_tabla_presiones_hidrostaticas)
        
    def botones_cabezales(self):
        self.pb_tipo_cabezal_sup.clicked.connect(lambda: self.seleccionar_cabezal(self.pb_tipo_cabezal_sup))
        self.pb_tipo_cabezal_inf.clicked.connect(lambda: self.seleccionar_cabezal(self.pb_tipo_cabezal_inf))

    def config_botones(self):
        self.botones_envolvente()
        self.botones_cabezales()
        
    def config_iniciales_tabla_hidrostaticas(self):
        self.ui_tabla_presiones_hidrostaticas.l_altura_envolvente.setText(str(self.model.le_))

    def abrir_tabla_presiones_hidrostaticas(self):
        self.tabla_presiones_hidrostaticas = QMainWindow()
        self.ui_tabla_presiones_hidrostaticas = UiTablaPresionesHidrostaticas()
        self.ui_tabla_presiones_hidrostaticas.setupUi(self.tabla_presiones_hidrostaticas)
        self.config_iniciales_tabla_hidrostaticas()
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
    
    def seleccionar_cabezal(self,objeto):
        if objeto.text() == "Semielíptico 2 : 1":
            objeto.setText("Semiesférico")
        elif objeto.text() == "Semiesférico":
            objeto.setText("Toiesférico")
        else:
            objeto.setText("Semielíptico 2 : 1")
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    if platform.system() == "Windows":
        app.setStyle("Fusion")
    mainWindow = GUI()
    mainWindow.show()
    sys.exit(app.exec_())