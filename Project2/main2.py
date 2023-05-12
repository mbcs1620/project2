from controller2 import *

def main():

    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Project 2')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()