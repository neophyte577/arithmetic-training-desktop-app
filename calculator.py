
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from functools import partial


def arithmetic(expr):

    try:
        output = str(eval(expr))

    except Exception:
        output = 'WRONG'

    return output


class Controller:

    def __init__(self, model, view):

        self.compute = model
        self.view = view
        self.connexions()
        self.view.keyPressEvent = self.key_events

    def calc(self):

        answer = self.compute(expr=self.view.current_text())
        self.view.set_text(answer)

    def get_expr(self, expr):

        if self.view.current_text() == 'WRONG':
            self.view.clear_text()
        
        new_exp = self.view.current_text() + expr
        self.view.set_text(new_exp)

    def connexions(self):

        for key, button in self.view.button_dict.items():
            if key not in {'C', '='}:
                button.clicked.connect(partial(self.get_expr, key)) 

        self.view.button_dict['='].clicked.connect(self.calc)
        self.view.display.returnPressed.connect(self.calc)
        self.view.button_dict['C'].clicked.connect(self.view.clear_text)

    def key_events(self, event):
        keys = [str(n) for n in range(10)] + ['+','-','*','/','(',')','.']
        if event.text() in keys:
            self.get_expr(event.text())
        elif event.text() == 'c':
            self.view.display.clear()
        elif event.text() == 'w':
            self.view.close()


class Interface(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle('Calculadora')
        self.setWindowIcon(QIcon('Icons/calculator.png'))
        self.setFixedSize(350, 350)

         # Display

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        
        # Buttons

        self.button_dict = {}
        button_layout = QGridLayout()
        keypad = [ ['1','2','3','+','C'],
                   ['4','5','6','-','('],
                   ['7','8','9','*',')'],
                   ['0','00','.','/','='] ]
        
        for row, keys in enumerate(keypad):
            for col, key in enumerate(keys):
                self.button_dict[key] = QPushButton(key)
                self.button_dict[key].setFixedSize(60, 60)
                button_layout.addWidget(self.button_dict[key], row, col)

        # Central Layout

        self.central_layout = QVBoxLayout()
        self.central_layout.addWidget(self.display)
        self.central_layout.addLayout(button_layout)
        
        central_widget = QWidget(self)
        central_widget.setLayout(self.central_layout)
        
        self.setCentralWidget(central_widget)

    def set_text(self, text):

        self.display.setText(text)
        self.display.setFocus()

    def current_text(self):

        return self.display.text()
    
    def clear_text(self):

        self.set_text('')


def main():

    app = QApplication([])

    window = Interface()
    window.show()

    Controller(model=arithmetic, view=window)

    app.exec()

if __name__ == '__main__':

    main()
