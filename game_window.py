from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QFont, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from time import time
import calculator
import arithmetic


class RoundWindow(QMainWindow):

    def __init__(self, parent, operand_1=420, operand_2=69, operation='+'):

        super().__init__(parent)

        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operation = operation
        self.parent = parent

        self.expression = QLabel(str(operand_1) + ' ' +  operation + ' ' + str(operand_2))
        self.expression.setFont(QFont('Jokerman', 20))
        
        self.equals_sign = QLabel('=')
        self.equals_sign.setFont(QFont('Jokerman', 20))

        self.submission_field = QLineEdit()
        self.submission_field.setFixedWidth(80)
        self.submission_field.setFont(QFont('Jokerman', 15))
        self.submission_field.setValidator(QIntValidator())
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

        if self.submission_field.text().strip() != '':

            answer = eval(str(self.operand_1) + self.operation + str(self.operand_2))

            if int(self.submission_field.text()) == answer:

                self.parent.stop_time = time()
                self.parent.round_times.append(self.parent.stop_time - self.parent.start_time) 
                self.parent.round_counter += 1
                self.close()
                self.parent.next_round()


    def mousePressEvent(self, event):

        self.submission_field.setFocus()


class GameWindow(QMainWindow):

    def __init__(self, level=0):

        super().__init__()

        self.operations = ('+', '-', '*', '/')
        self.current_level = 0
        self.last_level = 2
        self.time_data = []
        self.round = QWidget()

        self.setWindowTitle('Level ' + str(level))
        self.setWindowIcon(QIcon('Icons/brain--plus.png'))

        self.round = QWidget()

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
        self.central_layout = QVBoxLayout()    
        self.central_layout.addWidget(self.round)
        self.central_layout.addWidget(self.button_row, alignment=Qt.AlignCenter)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        self.play_level()

    def show_calculator(self):

        self.round.submission_field.releaseKeyboard()
        self.calc_window = calculator.Interface()
        calculator.Controller(model=calculator.arithmetic, view=self.calc_window)
        self.calc_window.show()

    def quit(self):

        self.close()

    def next_round(self):

        if self.round_counter < 3:
            operation = arithmetic.choice(self.operations)

            x, y = arithmetic.int_selector(operation, self.current_level)

            print(x, operation, y)

            self.start_time = time()

            self.round = RoundWindow(parent=self, operand_1=x, operand_2=y, operation=operation)
            self.central_layout.insertWidget(0, self.round)
            self.round.submission_field.setFocus()
        
        else:
            self.current_level += 1
            self.play_level()

    def play_level(self):

        self.round_counter = 0
        self.round_times = []

        if self.current_level <= self.last_level:
            self.setWindowTitle('Level ' + str(self.current_level+1))
            self.next_round()

        else:
            self.round.setParent(None)
            del self.round

            self.button_row.setParent(None)

            self.sweet_victory = QLabel('Oh, Happy Day')
            self.sweet_victory.setFont(QFont('Jokerman', 25))

            self.reset_button = QPushButton('Play Again?')
            self.reset_button.clicked.connect(self.reset_game)

            self.central_layout.insertWidget(0, self.sweet_victory)
            self.central_layout.insertWidget(1, self.reset_button)
            self.central_layout.insertWidget(2, self.quit_button)

            self.setWindowTitle('Fin')

            self.central_widget.adjustSize()
            self.adjustSize()

    def reset_game(self):

        self.sweet_victory.setParent(None)
        del self.sweet_victory
        
        self.reset_button.setParent(None)
        del self.reset_button

        self.current_level = 0
        self.play_level()


def main():

    app = QApplication([])

    window = GameWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()