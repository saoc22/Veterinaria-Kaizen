#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
from demo_GUI import pantalla_formatos, grid

#initiallize GUI application
app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("Reportes Kaizen")
window.setWindowIcon(QtGui.QIcon("img/logo.png"))
window.setFixedWidth(700)
window.setMinimumHeight(900)
#place window in (x,y) coordinates
# window.move(2700, 200)
window.setStyleSheet("background: '#0D1F43';")

#display frame 1
pantalla_formatos()

window.setLayout(grid)

window.show()
sys.exit(app.exec()) #terminate the app
