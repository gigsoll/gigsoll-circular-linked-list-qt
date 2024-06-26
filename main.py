import sys
import random
from linkedList import Node
from multimethod import multimethod
from linkedList import CircularLinkedList
from PyQt6.QtWidgets import *
from PyQt6 import uic

class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()
        self.cbList.addItems({"Учні", "Білети"})

        self.pbAddBefore.clicked.connect(self.pbAddBefore_click)
        self.pbAddAfter.clicked.connect(self.pbAddAfter_click)
        self.pbDelete.clicked.connect(self.pbDelete_click)
        self.pbFind.clicked.connect(self.pbFind_click)
        self.pbGenerate.clicked.connect(self.pbGenerate_click)
        self.pbGiveTickets.clicked.connect(self.pbGiveTickets_click)

        self.students = CircularLinkedList()
        self.tickets = CircularLinkedList()

    def GetTable(self):
        match self.cbList.currentText():
            case "Учні":
                return [self.students, self.tbStudents]
            case "Білети":
                return [self.tickets, self.tbTicket]

    def pbAddBefore_click(self):
        workWith = self.GetTable()
        data = self.leData.text()
        index = int(self.leIndex.text())     
        
        workWith[0].addBefore(data, index)
        self.FillTables(workWith[0].traverse(), workWith[1])

    def pbAddAfter_click(self):
        workWith = self.GetTable()
        data = self.leData.text()
        index = int(self.leIndex.text())

        workWith[0].addAfter(data, index)
        self.FillTables(workWith[0].traverse(), workWith[1])

    def pbDelete_click(self):        
        workWith = self.GetTable()
        index = int(self.leIndex.text())
        workWith[0].deleteNode(index)
        self.FillTables(workWith[0].traverse(), workWith[1])

    def pbFind_click(self):
        workWith = self.GetTable()
        data = self.leData.text()
        index = self.leIndex.text()

        if data != "" and index == "":
            searchResult = workWith[0].search(0, data, "key")
            if searchResult == None:
                self.leResult.setText(f"Елемент з зі значенням {data} не знайдено")
            else:
                self.leResult.setText(f"Елемент зі значенням {data} має індекс {searchResult}")
        elif data == "" and index != "":
            searchResult = workWith[0].search(int(index), 0, "index")
            if searchResult == None:
                self.leResult.setText(f"Елемент з індексом {index} не знайдено")
            else:
                self.leResult.setText(f"Елемент з індексом {index} має значення {searchResult}")
        elif data != "" and index != "":
            searchResult = workWith[0].search(int(index), data, "index and key")
            if searchResult == True:
                self.leResult.setText(f"Елемент з індексом {index} та значенням {data} знайдено")
            else:
                self.leResult.setText(f"Елемент з індексом {index} та значенням {data} не знайдено")

    def pbGenerate_click(self):
        self.GenerateNames(15)
        self.GenerateTickets(7)
        students = self.students.traverse()
        tickets = self.tickets.traverse()
        self.FillTables(students, self.tbStudents)
        self.FillTables(tickets, self.tbTicket)

    def pbGiveTickets_click(self):
        studentsStep = int(self.leStudentsStep.text())
        ticketsStep = int(self.leTicketsStep.text()) 

        students = self.students.traverseWithStep(studentsStep, self.students.getCount())
        tickets = self.tickets.traverseWithStep(ticketsStep, self.students.getCount())
        self.FillTables(students, tickets, self.tbResult, self.students.getCount())

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
                self.tickets.addToEmpty(str(random.randint(1000, 10000)))
            else:
                self.tickets.addAtEnd(str(random.randint(1000, 10000)))

    @multimethod
    def FillTables(self, data: list, table: QTableWidget):
            table.setRowCount(len(data))
            table.setColumnCount(1)
            table.horizontalHeader().hide()
            table.horizontalHeader().setStretchLastSection(True)
            for i in range(len(data)):
                table.setItem(i, 0, QTableWidgetItem(str(data[i])))

    @multimethod
    def FillTables(self, data1: list, data2: list, table: QTableWidget, rows):
        table.setRowCount(rows)
        table.setColumnCount(2)
        table.horizontalHeader().hide()
        table.horizontalHeader().setStretchLastSection(True)
        for i in range(rows):
            table.setItem(i, 0, QTableWidgetItem(str(data1[i])))
            table.setItem(i, 1, QTableWidgetItem(str(data2[i])))

def main():
    app = QApplication(sys.argv)
    window = Ui()
    app.exec()

main()