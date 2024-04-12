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
        self.GenerateNames(10)
        self.GenerateTickets(5)
        students = self.students.traverse()
        tickets = self.tickets.traverse()
        self.FillTables(students, [], self.tbStudents)
        self.FillTables(tickets, [],self.tbTicket)

    def pbGiveTickets_click(self):
        print("Give Tickets")

    def GenerateNames(self, length):
        names = ["Андрій", "Ярослав", "Олександр", "Михайло", "Богдан", "Олена", "Катерина", "Марія", "Анна", "Наталія"]
        surnames = ["Шевченко", "Петренко", "Кравчук", "Іваненко", "Коваленко", "Степаненко", "Сидоренко", "Поліщук", "Бордар", "Ткаченко"]
        for i in range(length):
            if i == 0:
                self.students.addToEmpty(f"{random.choice(names)} {random.choice(surnames)}")
            else:
                self.students.addAtEnd(f"{random.choice(names)} {random.choice(surnames)}")
    
    def GenerateTickets(self, length):
        for i in range(length):
            if i == 0:
                self.tickets.addToEmpty(random.randint(1000, 10000))
            else:
                self.tickets.addAtEnd(random.randint(1000, 10000))

    def FillTables(self, data1, data2, table):
        if table == self.tbStudents or self.tbTicket:
            table.setRowCount(len(data1))
            table.setColumnCount(1)
            table.horizontalHeader().hide()
            table.horizontalHeader().setStretchLastSection(True)
            for i in range(len(data1)):
                table.setItem(i, 0, QTableWidgetItem(str(data1[i])))

def main():
    app = QApplication(sys.argv)
    window = Ui()
    app.exec()

main()