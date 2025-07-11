import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from default_gui_standars import Ui_Dialog as ui

class GUI(QMainWindow):  # Cambiar la herencia a QMainWindow
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.ui = ui()  # Instanciar la clase Ui_Dialog
        self.ui.setupUi(self)  # Configurar la interfaz en el QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = GUI()
    mainWindow.show()
    sys.exit(app.exec_())