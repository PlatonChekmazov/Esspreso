from PyQt5 import uic
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.print_data()
        self.data = ''

    def print_data(self):
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.drink = self.cur.execute('SELECT * from data').fetchall()
        self.data = ''
        for i in self.drink:
            self.data += f"ID {i[0]}, Название сорта {i[1]}, степень обжарки {i[2]}," \
                         f" {i[3]}, описание вкуса - {i[4]}, цена - {i[5]}, объем упаковки - {i[6]}\n"
        self.text.setPlainText(self.data)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())