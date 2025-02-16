from apit212 import Apit212
from package.mainWindow import ApitGui
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = ApitGui()
    mainWindow.show()
    app.exec()
