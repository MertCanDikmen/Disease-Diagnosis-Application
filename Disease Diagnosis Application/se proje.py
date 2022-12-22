from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import Ui_seprojenew

class Pencere(QMainWindow, Ui_seprojenew.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
