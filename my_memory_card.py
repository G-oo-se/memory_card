#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.right_answer = right_answer
        self.question = question
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    text_up.setText(q.question)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    show_question()
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0, len(question_list) - 1)

    q = question_list[cur_question]
    ask(q)
def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def show_correct(res):
    result.setText(res)
    show_result()
def show_result():
    GroupBox.hide()
    GroupBox2.show()
    button.setText('Следующий вопрос')
def show_question():
    GroupBox2.hide()
    GroupBox.show()
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    RadioGroup.setExclusive(True)

app = QApplication([])
main_win = QWidget()
main_win.total = 0
main_win.score = 0
main_win.setWindowTitle('Memory Card')
main_win.resize(500,500)

text_up = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

question_list = []
question_list.append(Question('Какой цвет есть на флаге Бразилий?', 'Желтый', 'Черный', 'Фиолетовый', 'Красный'))
question_list.append(Question('Какой цвет есть на флаге Казахстана?', 'Синий', 'Красный', 'Зеленый', 'Черный'))
question_list.append(Question('Сколько будет 1 / 5 + 2 / 5?', '6 / 10', '0', '4 / 5', '1'))
question_list.append(Question('Сколько будет √25?', '5', '4', '2', '3'))
question_list.append(Question('Сколько будет (√121 + √16) / √9?', '5', '4', '1', '3'))
question_list.append(Question('Сколько будет 3² * 27?', '243', '244', '241', '242'))


#Групп бокс варианты ответов
GroupBox = QGroupBox('Варианты ответов')
r1 = QRadioButton('Энцы')
r2 = QRadioButton('Смурфы')
r3 = QRadioButton('Чулымцы')
r4 = QRadioButton('Алеуты')
answer = [r1, r2, r3, r4]
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(r1)
layout2.addWidget(r2)
layout3.addWidget(r3)
layout3.addWidget(r4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

GroupBox.setLayout(layout1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

#Групп бокс результатов
GroupBox2 = QGroupBox('Результат теста')
result = QLabel('Здесь Правильно/Не правильно')
layout_ans = QVBoxLayout()
layout_ans.addWidget(result, alignment = Qt.AlignCenter)
GroupBox2.setLayout(layout_ans)
GroupBox2.hide()

line = QVBoxLayout()
line.addWidget(text_up, alignment = Qt.AlignCenter)
line.addWidget(GroupBox)
line.addWidget(GroupBox2)
line.addWidget(button, alignment = Qt.AlignCenter)


main_win.setLayout(line)
button.clicked.connect(click_OK)
main_win.cur_question = -1
main_win.show()
next_question()
app.exec_()