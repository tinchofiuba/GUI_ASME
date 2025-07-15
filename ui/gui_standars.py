import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import platform

from PyQt5.QtWidgets import QApplication, QMainWindow

from default_gui_standars import Ui_Dialog as UiMain
from tabla_materiales import Ui_Dialog as UiTablaMateriales
from tabla_presiones_hidrostaticas import Ui_Dialog as UiTablaPresionesHidrostaticas

from model import Model
from envolvente import Envolvente
from cabezales import CabeSup, CabeInf
from datos_disenio import DatosDisenio
from p_hidrostatica import PresionesHidrostaticas

class GUI(QMainWindow,UiMain): 
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.config_widgets()
        self.model = Model()

    def config_widgets(self):
        self.config_botones()
        self.config_entrys()
        
    def config_entrys(self):
        #cambios en datos de envolvente
        self.le_diametro_int_envolvente.textChanged.connect(self.model.calcular_espesor_envolvente)
        self.le_altura_envolvente.textChanged.connect(self.model.calcular_espesor_envolvente)
        
        #cambios en datos de materiales
        self.le_max_tens_adm.textChanged.connect(self.model.calcular_espesores)
        
        #cambios en datos de características de diseño
        self.le_presion.textChanged.connect(self.model.calcular_espesor_envolvente)
        self.le_corrosion_int.textChanged.connect(self.model.calcular_espesores)
        self.le_corrosion_ext.textChanged.connect(self.model.calcular_espesores)
        self.le_diametro_cab_inf.textChanged.connect(self.model.calcular_espesor_cabezal)
        

    def botones_envolvente(self):
        #cambios en botones de envolvente
        self.pb_tipo_recipiente.clicked.connect(self.seleccionar_recipiente)
        self.pb_orientacion_recipiente.clicked.connect(self.seleccionar_orientacion)
        self.pb_eficiencia_soldadura.clicked.connect(self.seleccionar_eficiencia_soldadura)
        self.pb_presiones_hidrostaticas.clicked.connect(self.abrir_tabla_presiones_hidrostaticas)
        self.pb_material.clicked.connect(self.abrir_tabla_materiales)
        
    def botones_cabezales(self):
        self.pb_tipo_cabezal_sup.clicked.connect(lambda: self.seleccionar_cabezal(self.pb_tipo_cabezal_sup))
        self.pb_tipo_cabezal_inf.clicked.connect(lambda: self.seleccionar_cabezal(self.pb_tipo_cabezal_inf))

    def config_botones(self):
        self.botones_envolvente()
        self.botones_cabezales()
        
    def config_iniciales_tabla_hidrostaticas(self):
        self.ui_tabla_presiones_hidrostaticas.l_altura_envolvente.setText(str(self.le_altura_envolvente.text()))

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
        self.model.calcular_espesor_envolvente()
        if self.pb_eficiencia_soldadura.text() == "1":
            self.pb_eficiencia_soldadura.setText("0.7")
        elif self.pb_eficiencia_soldadura.text() == "0.7":
            self.pb_eficiencia_soldadura.setText("0.85")
        else:
            self.pb_eficiencia_soldadura.setText("1")

    def seleccionar_recipiente(self):
        self.model.calcular_espesor_envolvente()
        if self.pb_tipo_recipiente.text() == "Cilíndrico":
            self.pb_tipo_recipiente.setText("Esférico")
        else:
            self.pb_tipo_recipiente.setText("Cilíndrico")
            
    def seleccionar_orientacion(self):
        self.model.calcular_espesor_envolvente()
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