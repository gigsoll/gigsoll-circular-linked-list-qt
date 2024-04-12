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
        students = []
        for i in range(length):
            students.append(f"{random.choice(names)} {random.choice(surnames)}")
        return students
    
    def GenerateTickets(self, length):
        tickets = []
        for i in range(length):
            tickets.append(random.randint(1000, 10000))
        return tickets
    
app = QApplication(sys.argv)
window = Ui()
app.exec()