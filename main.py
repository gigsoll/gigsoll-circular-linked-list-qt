import sys
import random
from linkedList import Node
from linkedList import CircularLinkedList
from PyQt6.QtWidgets import *
from PyQt6 import uic

class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

app = QApplication(sys.argv)
window = Ui()
app.exec()