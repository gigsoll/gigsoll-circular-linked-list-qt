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
        self.cbList.addItems({"Учні", "Білети"})

        self.pbAdd.clicked.connect(self.pbAdd_click)
        self.pbDelete.clicked.connect(self.pbDelete_click)
        self.pbFind.clicked.connect(self.pbFind_click)
        self.pbGenerate.clicked.connect(self.pbGenerate_click)
        self.pbGiveTickets.clicked.connect(self.pbGiveTickets_click)

        self.students = CircularLinkedList()
        self.tickets = CircularLinkedList()

    def pbAdd_click(self):
        print("Add")

    def pbDelete_click(self):
        print("Delete")

    def pbFind_click(self):
        print("Find")

    def pbGenerate_click(self):
        print("Generate")

    def pbGiveTickets_click(self):
        print("Give Tickets")

    def GenerateNames(self, length):
        names = ["Андрій", "Ярослав", "Олександр", "Михайло", "Богдан", "Олена", "Катерина", "Марія", "Анна", "Наталія"]
        surnames = ["Шевченко", "Петренко", "Кравчук", "Іваненко", "Коваленко", "Степаненко", "Сидоренко", "Поліщук", "Бордар", "Ткаченко"]
        for i in range(length):
            if i == 0:
                self.students.addToEmpty(f"{random.choice(names)} {surnames}")
            else:
                self.students.addAtEnd(f"{random.choice(names)} {random.choice(surnames)}")
    
    def GenerateTickets(self, length):
        for i in range(length):
            if i == 0:
                self.tickets.addToEmpty(random.randint(1000, 10000))
            else:
                self.tickets.addAtEnd(random.randint(1000, 10000))
            
app = QApplication(sys.argv)
window = Ui()
app.exec()