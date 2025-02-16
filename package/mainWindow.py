from PyQt6.QtWidgets import (
    QMainWindow
)
from .app import CenterWidget


class ApitGui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ApitConnect")
        self.setFixedSize(350, 700)

        app = CenterWidget(self)
        self.setCentralWidget(app)
