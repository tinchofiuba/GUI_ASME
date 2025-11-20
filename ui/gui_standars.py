import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import platform

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QShortcut
from PyQt5.QtGui import QColor, QPalette, QKeySequence
from typing import Union
from default_gui_standars import Ui_Dialog as UiMain
from tabla_materiales import Ui_Dialog as UiTablaMateriales
from tabla_presiones_hidrostaticas import Ui_Dialog as UiTablaPresionesHidrostaticas

from model import Model
from datos_disenio import DatosDisenio
from p_hidrostatica import PresionesHidrostaticas

colores_usados = {
    "eficiencia_soldadura" : {
        "1": "#10B981",      # Verde intenso
        "0.7": "#6EE7B7",    # Verde claro
        "0.85": "#34D399"    # Verde medio
    },
    
    "presion_hidrostatica": "#66ccff" # Celeste clarito
}



class GUI(QMainWindow,UiMain): 
    
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.model = Model()
        self.configuraciones_iniciales()
        self.config_widgets()
        acciones_line_edits = {
        "le_diametro_int_envolvente": self.model.set_diametro,
        "le_altura_envolvente": self.model.set_altura_envolvente,
        "le_max_tens_adm": self.model.set_max_tens_adm,
        "le_presion": self.model.set_presion,
        "le_corrosion_int": self.model.set_corrosion_interna,
        "le_corrosion_ext": self.model.set_corrosion_externa,
        "le_diametro_cab_inf": self.model.cab.set_diametro('inf'),
        "le_diametro_cab_sup": self.model.cab.set_diametro('sup'),
        "le_radio_filete_cab_sup": self.model.cab.set_radio_filete('sup'),
        "le_radio_filete_cab_inf": self.model.cab.set_radio_filete('inf'),
        "le_radio_corona_cab_sup": self.model.cab.set_radio_corona('sup'),
        "le_radio_corona_cab_inf": self.model.cab.set_radio_corona('inf')
    }

    def configuraciones_iniciales(self):
        #se configuran algunos widgets según lo que uno quiera mostrar al inicio
        self.pb_eficiencia_soldadura.setStyleSheet(f"background-color: {colores_usados['eficiencia_soldadura']['1']};")
        self.pb_presiones_hidrostaticas.setStyleSheet(f"background-color: {colores_usados['presion_hidrostatica']};")
        
    def dummy(self):
        """Método dummy para evitar errores de sintaxis en el diccionario."""
        pass
        
    def validar_entry(self, entry):
        """Valida el texto del entry usando el un método del model."""
        texto = entry.text()
        if self.model.validar_numerico(texto):
            palette = entry.palette()
            palette.setColor(QPalette.Text, QColor("black"))
            entry.setPalette(palette)
        else:
            palette = entry.palette()
            palette.setColor(QPalette.Text, QColor("red"))
            entry.setPalette(palette)

    def config_widgets(self):
        # Lista de todos los QLineEdit que necesitan validación
        self.listas_line_edit = [
            "le_diametro_int_envolvente",
            "le_altura_envolvente",
            "le_MLNS_envolvente",
            "le_max_tens_adm",
            "le_presion",
            "le_temperatura",
            "le_corrosion_int",
            "le_corrosion_ext",
            "le_diametro_cab_inf",
            "le_radio_corona_cab_inf",
            "le_radio_filete_cab_inf",
            "le_diametro_cab_sup",
            "le_radio_filete_cab_sup",
            "le_radio_corona_cab_sup"
        ]
        self.config_botones()
        self.config_entrys()

        
    def config_entrys(self):
        for e in self.listas_line_edit:
            line_edit = getattr(self, e)
            line_edit.textChanged.connect(lambda text, le=line_edit: self.validar_entry(le))
        
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
        # Agregar borde celeste clarito para delimitar la ventana del fondo
        self.tabla_presiones_hidrostaticas.setStyleSheet(
            "QMainWindow { "
            f"border: 3px solid {colores_usados['presion_hidrostatica']}; "
            "background-color: white; "
            "}"
        )
        # Configurar atajo de teclado para cerrar con Esc
        esc_shortcut = QShortcut(QKeySequence("Esc"), self.tabla_presiones_hidrostaticas)
        esc_shortcut.activated.connect(self.tabla_presiones_hidrostaticas.close)
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
        str_eficiencia_soldadura = self.pb_eficiencia_soldadura.text()
        self.pb_eficiencia_soldadura.setStyleSheet(f"background-color: {colores_usados['eficiencia_soldadura'][str_eficiencia_soldadura]};")

    def hab_deshabilitar_le(self, line_edit:Union[QLineEdit,list[QLineEdit]], color : str):
        if isinstance(line_edit, list):
            for le in line_edit:
                if color == "gray":
                    le.setEnabled(False)
                else:
                    le.setEnabled(True)
                le.setStyleSheet(f"color: {color};")
        else:
            if color == "gray":
                line_edit.setEnabled(False)
            else:
                line_edit.setEnabled(True)
            line_edit.setStyleSheet(f"color: {color};")
        
    def hab_deshabilitar_label(self, label:Union[QLabel,list[QLabel]], color : str):
        if isinstance(label, list):
            for l in label:
                if color == "gray":
                    l.setEnabled(False)
                    l.setStyleSheet(f"color: {color};")
                else:
                    l.setEnabled(True)
                    l.setStyleSheet(f"color: {color};")
        else:
            if color == "gray":
                label.setEnabled(False)
            else:
                label.setEnabled(True)
            label.setStyleSheet(f"color: {color};")

    def seleccionar_recipiente(self):
        lista_line_edit_a_deshabilitar = [self.le_altura_envolvente,self.le_MLNS_envolvente]
        lista_labels_a_deshabilitar = [self.l_altura_envolvente,self.l_MLNS]

        self.model.calcular_espesor_envolvente()
        if self.pb_tipo_recipiente.text() == "Cilíndrico":
            self.pb_tipo_recipiente.setText("Esférico")
            self.pb_orientacion_recipiente.setEnabled(False)

            self.hab_deshabilitar_label(lista_labels_a_deshabilitar, "gray")
            self.hab_deshabilitar_le(lista_line_edit_a_deshabilitar, "gray")

        else:
            self.pb_tipo_recipiente.setText("Cilíndrico")
            self.pb_orientacion_recipiente.setEnabled(True)

            self.hab_deshabilitar_label(lista_labels_a_deshabilitar, "black")
            self.hab_deshabilitar_le(lista_line_edit_a_deshabilitar, "black")
            
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