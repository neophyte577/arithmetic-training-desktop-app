from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QDoubleValidator, QFont
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
import calculator
import arithmetic

class RoundWindow(QMainWindow):

    def __init__(self, operand_1=420, operand_2=69, operation='+'):

        super().__init__()

        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operation = operation

        self.expression = QLabel(str(operand_1) + ' ' +  operation + ' ' + str(operand_2))
        self.expression.setFont(QFont('Helvetica', 15))
        
        self.equals_sign = QLabel('=')
        self.equals_sign.setFont(QFont('Helvetic', 15))

        self.submission_field = QLineEdit()
        self.submission_field.setFixedWidth(80)
        self.submission_field.setFont(QFont('Helvetica', 15))
        self.submission_field.setValidator(QDoubleValidator())
        self.submission_field.grabKeyboard()
        self.submission_field.textChanged.connect(self.check_submission)

        self.submission_widget = QWidget()
        submission_layout = QHBoxLayout()
        submission_layout.addWidget(self.equals_sign)
        submission_layout.addWidget(self.submission_field)
        self.submission_widget.setLayout(submission_layout)

        self.spacer_widget = QLabel('See you, space cowboy')
        self.spacer_widget.setFont(QFont('Helvetica', 5))
        size_policy = QSizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.spacer_widget.setSizePolicy(size_policy)
        self.spacer_widget.hide()

        self.central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.spacer_widget)
        central_layout.addWidget(self.expression, alignment=Qt.AlignCenter)
        central_layout.addWidget(self.submission_widget, alignment=Qt.AlignCenter)
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)

    def check_submission(self):

        answer = str(eval(str(self.operand_1) + self.operation + str(self.operand_2)))

        if self.submission_field.text() == answer:

            print('alright')

    def mousePressEvent(self, event):

        self.submission_field.setFocus()


class GameWindow(QMainWindow):

    def __init__(self, level=0):

        super().__init__()

        self.setWindowTitle('Level ' + str(level))

        self.round_0 = RoundWindow()

        self.calculator_button = QPushButton('Show Calculator')
        self.calculator_button.clicked.connect(self.show_calculator)

        self.quit_button = QPushButton('Quit')
        self.quit_button.clicked.connect(self.quit)

        self.button_row = QWidget()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calculator_button)
        button_layout.addWidget(self.quit_button)
        self.button_row.setLayout(button_layout)

        self.central_widget = QWidget()
        central_layout = QVBoxLayout()    
        central_layout.addWidget(self.round_0)
        central_layout.addWidget(self.button_row, alignment=Qt.AlignCenter)
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)

    def show_calculator(self):

        self.round_0.submission_field.releaseKeyboard()
        self.calc_window = calculator.Interface()
        calculator.Controller(model=calculator.arithmetic, view=self.calc_window)
        self.calc_window.show()

    def quit(self):

        self.close()

def main():

    app = QApplication([])

    window = GameWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()