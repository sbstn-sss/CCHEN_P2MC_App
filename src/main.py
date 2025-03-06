import sys
import os

from PyQt5 import QtWidgets

from views.mainwindow import MainWindow


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# exec

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()
