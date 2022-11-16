import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QColor
from Interface import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Переменная отвечающая за цвет шашек чей ход в данный момент (сначала белый т.к. белые ходят первые)
        self.current_color = 'white'

        # Пусть следующая переменная содержит кортеж (x, y) клетки, которую выбрал игрок (если соответствует правилам)
        self.selected = tuple()
        # Координаты последней съевшей фигуры
        self.selected1 = tuple()
        # Список labels вне доски
        self.out = [self.box_1, self.box_2, self.box_3, self.box_4, self.box_5, self.box_6, self.box_7, self.box_8,
                    self.box_9, self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15,
                    self.box_16, self.box_17, self.box_18, self.box_19, self.box_20, self.box_21, self.box_22,
                    self.box_23, self.box_24]

        self.white_count = 12
        self.black_count = 12

        # Pixmap доски, шашек и т.д.
        self.boardPix = QPixmap('Textures\\BoardCheckers2.png')
        self.white = QPixmap('Textures\\WhiteFig.png')
        self.black = QPixmap('Textures\\BlackFig.png')
        self.whiteQueen = QPixmap('Textures\\WhiteFigQueen.png')
        self.blackQueen = QPixmap('Textures\\BlackFigQueen.png')
        self.win_black = QPixmap('Textures\\black_won.png')
        self.win_white = QPixmap('Textures\\white_won.png')

        # Стиль кнопки "сдаюсь" и скрывание кнопки из меню выигрыша
        self.play_again_button.hide()
        self.giveupButton.setStyleSheet('QPushButton {background-color: #e5e3fb;'
                                        'border-style: outset;'
                                        'border-width: 2px;'
                                        'border-radius: 5px;'
                                        'border-color: #706f87;'
                                        'min-width: 4em;}')

        # Переменная отвечающая за возможность хода, если 1, то можно ходить, иначе нельзя
        # Она нужна, чтобы нельзя было сходить во время меню выигрыша
        self.available = 1

        # задаем доску как массив и 8 строк с 8 ячейками
        self.board = [[None for i1 in range(8)] for i in range(8)]
        # Заполняем доску фигурами (шашками черного и белого цвета в три ряда с краев доски на черных клетках)
        # Пусть ячейка (0, 7) массива (0 строка, 7 ячейка) - это клетка а1 доски
        for i in range(3):
            if i % 2 != 0:
                for j in range(0, 7, 2):
                    self.board[i][j] = Figure('white')
            else:
                for j in range(1, 8, 2):
                    self.board[i][j] = Figure('white')
        for i in range(7, 4, -1):
            if i % 2 != 0:
                for j in range(0, 7, 2):
                    self.board[i][j] = Figure('black')
            else:
                for j in range(1, 8, 2):
                    self.board[i][j] = Figure('black')
        self.board_render()

        # Если нажата клавиша "сдаюсь": запустить функция "сдаюсь"
        self.giveupButton.clicked.connect(self.give_up)

    def board_render(self):
        self.resize(1300, 800)
        # Текстура шахматной доски
        # Важно чтобы доска была под шашками, такая опция есть в QtDesigner

        self.boardLabel.setPixmap(self.boardPix)
        self.boardLabel.move(95, 95)
        self.boardLabel.resize(610, 610)

        # выстраиваем label'ы которые будем применять для отображения шашек в том же порядке что и массив
        # то есть клетка а1 на позиции (0, 7) и так далее
        self.labels = [[self.h1, self.g1, self.f1, self.e1, self.d1, self.c1, self.b1, self.a1],
                       [self.h2, self.g2, self.f2, self.e2, self.d2, self.c2, self.b2, self.a2],
                       [self.h3, self.g3, self.f3, self.e3, self.d3, self.c3, self.b3, self.a3],
                       [self.h4, self.g4, self.f4, self.e4, self.d4, self.c4, self.b4, self.a4],
                       [self.h5, self.g5, self.f5, self.e5, self.d5, self.c5, self.b5, self.a5],
                       [self.h6, self.g6, self.f6, self.e6, self.d6, self.c6, self.b6, self.a6],
                       [self.h7, self.g7, self.f7, self.e7, self.d7, self.c7, self.b7, self.a7],
                       [self.h8, self.g8, self.f8, self.e8, self.d8, self.c8, self.b8, self.a8],
                       ]

        # проходимся по доске и рисуем шашки там где они есть в зависимости от цвета
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    if self.board[i][j].get_color() == 'white':
                        self.labels[i][j].setPixmap(self.white)
                    else:
                        self.labels[i][j].setPixmap(self.black)
        for i in self.labels:
            for j in i:
                j.resize(75, 75)

        # отображаем цвет хода белых
        self.step.setPixmap(self.white)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton and self.available:
            if not self.selected:
                # Если шашка не выбрана, то запустим функцию нажатия с координатами клика
                self.press(event.x(), event.y())
            else:
                # Если шашка выбрана, то если она может двигаться, self.press() вернет кортеж координат
                # клетки в которой шашка и клетки куда двигать
                # Для удобства разделим функции проверки хода и самого хода
                self.move_figure(self.can_move(event.x(), event.y()))

    def paintEvent(self, event):
        # Фон за доской (просто заливка цветом)
        painter = QPainter(self)
        painter.drawRect(0, 0, 800, 800)
        painter.fillRect(0, 0, self.width(), self.height(), QColor(98, 82, 68))

    def press(self, x, y):
        x = (x - 100) // 75
        y = (y - 100) // 75
        # Проверяем есть ли шашка на поле (x, y) и совпадает ли ее цвет с цветом ходящего
        # Если да, то переменную отвечающую за
        if 0 <= x <= 7 and 0 <= y <= 7:
            if self.board[y][x] is not None and self.current_color == self.board[y][x].get_color():
                self.selected = (x, y)
                # Если клик пришелся по шашке врага, то мы забываем шашку съевшего последним
                self.selected1 = tuple()

            # Если игрок кликнул на пустое место и есть шашка, которая только что съела
            # то если игрок кликнул на клетку, чтобы съесть чужую фигуру, то мы разрешим ему это сделать
            # это функция съедания несколько раз в шашках
            # Если игрок не может съесть, то фигура не сходит, если игрок не заметил или решил не ходить, то как только
            # мышь кликнет на шашку другого игрока, вернуть будет ничего нельзя, игрок пропустил возможность
            elif self.board[y][x] is None and self.selected1:
                self.selected = self.selected1
                can_eat = self.can_only_eat(x, y)
                if can_eat:
                    self.current_color = 'white' if self.current_color == 'black' else 'black'
                    self.selected1 = tuple()
                    self.move_figure(can_eat)

    def can_move(self, x_to, y_to):
        # Даем переменные координатам шашки и координатам клетки, куда хочет сходит игрок

        x_from = self.selected[0]
        y_from = self.selected[1]
        x_to = (x_to - 100) // 75
        y_to = (y_to - 100) // 75

        # находим изменение координат по x и y
        delta_x = x_to - x_from
        delta_y = y_to - y_from

        # Обнуляем выбранную шашку, т.к. после того как мы проведем над ней операцию (сдвинем, либо ничего не сделаем)
        # она больше не понадобится, если игрок сходил неправильно, то лучше будет если дать ему выбрать шашку заново
        # и попробовать снова
        self.selected = tuple()

        # Проверим возможность хода (цвет уже проверен)

        # Ходим ли мы по диагонали
        if abs(delta_x) != abs(delta_y):
            return False

        # Не ходим ли мы за пределы доски
        elif x_to > 7 or 0 > x_to or y_to > 7 or 0 > y_to:
            return False

        # Теперь мы знаем что ходим в пределах доски, проверим нет ли фигуры на клетке, на которую мы идем
        # Если мы ходим в ту же клетку, то это условие отклонит ход
        elif self.board[y_to][x_to] is not None:
            return False

        if self.board[y_from][x_from].get_status() == 'casual':
            # Не ходим ли мы назад (только если |delta| == 1, то есть игрок не делает попытку съесть фигуру)
            if abs(delta_y) == abs(delta_x) == 1:
                if self.board[y_from][x_from].get_color() == 'white' and delta_y < 0:
                    return False
                elif self.board[y_from][x_from].get_color() == 'black' and delta_y > 0:
                    return False

            # Если пытается съесть
            elif abs(delta_y) == abs(delta_x) == 2:
                if self.board[y_from + delta_y // 2][x_from + delta_x // 2] is None:
                    return False
                elif self.board[y_from + delta_y // 2][x_from + delta_x // 2].get_color() == \
                        self.board[y_from][x_from].get_color():
                    return False
        # Для дамки
        else:
            # Дамка может ходить только за одну либо 0 шашек врага
            count = 0
            directY = delta_y // abs(delta_y)
            directX = delta_x // abs(delta_x)
            for i in range(1, abs(delta_x)):
                if self.board[y_from + i * directY][x_from + i * directX] is not None:
                    count += 1
                if count == 2:
                    return False

        # Если все проверки пройдены (то есть нигде нет несовпадений с правилами), то мы возврращаем кортеж координат
        return x_from, y_from, x_to, y_to

    def move_figure(self, coords):
        # Если кортеж координат не пустой, то сдвинем фигуру
        # Если ход со смещением в 1, 1, то просто сдвинем
        # Если со смещением 2,2 то сдвинем нашу шашку и уберем ту, которая находится между клетками
        if coords:
            x_f = coords[0]
            y_f = coords[1]
            x_t = coords[2]
            y_t = coords[3]

            # перенесем шашку из начальной клетки в нужную с сохранением статуса и цвета
            self.board[y_t][x_t] = self.board[y_f][x_f]

            # Проверка на дамку и изменение статуса
            if self.board[y_t][x_t].get_status() == 'casual':
                if y_t == 7 and self.board[y_t][x_t].get_color() == 'white':
                    self.board[y_t][x_t].make_queen()
                elif y_t == 0 and self.board[y_t][x_t].get_color() == 'black':
                    self.board[y_t][x_t].make_queen()

            if self.board[y_t][x_t].get_status() == 'casual':
                self.labels[y_t][x_t].setPixmap(
                    self.white if self.board[y_t][x_t].get_color() == 'white' else self.black)
            else:
                self.labels[y_t][x_t].setPixmap(
                    self.whiteQueen if self.board[y_t][x_t].get_color() == 'white' else self.blackQueen)

            # Обнулим начальную клетку
            self.board[y_f][x_f] = None
            self.labels[y_f][x_f].clear()

            # Если съедаем
            # съеденная фигура:
            eaten_fig = None

            if abs(x_t - x_f) == 2 and self.board[y_t][x_t].get_status() == 'casual':
                # Запишем съеденную фигуру
                eaten_fig = self.board[y_f + (y_t - y_f) // 2][x_f + (x_t - x_f) // 2]

                self.board[y_f + (y_t - y_f) // 2][x_f + (x_t - x_f) // 2] = None
                self.labels[y_f + (y_t - y_f) // 2][x_f + (x_t - x_f) // 2].clear()
                self.selected1 = (x_t, y_t)

            # Дамка
            elif self.board[y_t][x_t].get_status() == 'queen' and abs(x_t - x_f) >= 2:
                directY = (y_t - y_f) // abs(y_t - y_f)
                directX = (x_t - x_f) // abs(x_t - x_f)
                for i in range(1, abs(x_t - x_f)):
                    if self.board[y_f + i * directY][x_f + i * directX] is not None:
                        # Запишем съеденную фигуру
                        eaten_fig = self.board[y_f + i * directY][x_f + i * directX]

                        self.board[y_f + i * directY][x_f + i * directX] = None
                        self.labels[y_f + i * directY][x_f + i * directX].clear()
                        break

                # Запишем координаты фигуры, которая съела последней
                self.selected1 = (x_t, y_t)

            if eaten_fig:
                if eaten_fig.get_color() == 'white':
                    chosen = random.choice(self.out[:self.white_count])
                    self.out.remove(chosen)
                    chosen.setPixmap(self.white if eaten_fig.get_status() != 'queen' else self.whiteQueen)
                    self.white_count -= 1
                else:
                    chosen = random.choice(self.out[self.white_count:])
                    self.out.remove(chosen)
                    chosen.setPixmap(self.black if eaten_fig.get_status() != 'queen' else self.blackQueen)
                    self.black_count -= 1
                if self.white_count * self.black_count == 0:
                    self.give_up()

            # Меняем цвет ходящих
            self.current_color = 'white' if self.current_color == 'black' else 'black'
            self.step.setPixmap(self.white if self.current_color == 'white' else self.black)

    def can_only_eat(self, x, y):
        # Эта функция нужна для проверки того, ест ли игрок, т.к. после того, как игрок съел, он может сходить только
        # в том случае, если ест
        # Эта функция частично копирует функция self.can_move() так как некоторые проверки совпадают

        # Даем переменные координатам шашки и координатам клетки, куда хочет сходит игрок

        x_from = self.selected[0]
        y_from = self.selected[1]
        x_to = x
        y_to = y

        # находим изменение координат по x и y
        delta_x = x_to - x_from
        delta_y = y_to - y_from

        # Обнуляем выбранную шашку, т.к. после того как мы проведем над ней операцию (сдвинем, либо ничего не сделаем)
        # она больше не понадобится, если игрок сходил неправильно, то лучше будет если дать ему выбрать шашку заново
        # и попробовать снова
        self.selected = tuple()

        # Ход по диагонали
        if abs(delta_x) != abs(delta_y):
            return False

        # Не ходим ли мы за пределы доски
        elif x_to > 7 or 0 > x_to or y_to > 7 or 0 > y_to:
            return False

        # Можно только есть
        if self.board[y_from][x_from].get_status() == 'casual':
            if abs(delta_x) != 2:
                return False

            elif abs(delta_x) == 2:
                if self.board[y_from + delta_y // 2][x_from + delta_x // 2] is None:
                    return False
                elif self.board[y_from + delta_y // 2][x_from + delta_x // 2].get_color() == \
                        self.board[y_from][x_from].get_color():
                    return False
        else:
            # Для дамки (она может есть если игрок ходит только за одну шашку врага (не за 2 и >))
            count = 0
            directY = delta_y // abs(delta_y)
            directX = delta_x // abs(delta_x)
            for i in range(1, abs(delta_x)):
                if self.board[y_from + i * directY][x_from + i * directX] is not None:
                    if self.board[y_from + i * directY][x_from + i * directX].get_color() == \
                            self.board[y_from][x_from].get_color():
                        return False
                    count += 1
                if count == 2:
                    return False
            if count == 0:
                return False

        # Если все проверки пройдены (то есть нигде нет несовпадений с правилами), то мы возврращаем кортеж координат
        return x_from, y_from, x_to, y_to

    def give_up(self):
        # Функция выигрыша одного из игроков, запускается если игрок нажал на кнопку "СДАЮСЬ"
        # либо чьи-то шашки кончились
        self.available = 0
        if isinstance(self.sender(), QPushButton):
            self.win_label.setPixmap(self.win_black if self.current_color == 'white' else self.win_white)
        else:
            self.win_label.setPixmap(self.win_black if self.current_color == 'black' else self.win_white)
        self.play_again_button.show()
        self.play_again_button.setStyleSheet('QPushButton {background-color: #312b67; color: #cfd1ff}'
                                             if self.current_color == 'white'
                                             else 'QPushButton {background-color: #e5e3fb}')
        self.play_again_button.clicked.connect(self.rerun)

    def rerun(self):
        self.win_label.clear()
        self.play_again_button.hide()

        self.available = 1
        self.selected1 = tuple()

        self.out = [self.box_1, self.box_2, self.box_3, self.box_4, self.box_5, self.box_6, self.box_7, self.box_8,
                    self.box_9, self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15,
                    self.box_16, self.box_17, self.box_18, self.box_19, self.box_20, self.box_21, self.box_22,
                    self.box_23, self.box_24]

        self.board = [[None for i1 in range(8)] for i in range(8)]
        # Заполняем доску фигурами (шашками черного и белого цвета в три ряда с краев доски на черных клетках)
        # Пусть ячейка (0, 7) массива (0 строка, 7 ячейка) - это клетка а1 доски
        for i in range(3):
            if i % 2 != 0:
                for j in range(0, 7, 2):
                    self.board[i][j] = Figure('white')
            else:
                for j in range(1, 8, 2):
                    self.board[i][j] = Figure('white')
        for i in range(7, 4, -1):
            if i % 2 != 0:
                for j in range(0, 7, 2):
                    self.board[i][j] = Figure('black')
            else:
                for j in range(1, 8, 2):
                    self.board[i][j] = Figure('black')
        for i in self.labels:
            for j in i:
                j.clear()

        for i in self.out:
            i.clear()

        self.white_count = self.black_count = 12

        self.step.setPixmap(self.white)
        self.current_color = 'white'

        self.board_render()


class Figure:
    def __init__(self, color):
        # переменная color - цвет шашки
        self.color = color
        # переменная status - статус, является она обычной шашкой, либо дамкой - queen
        self.status = 'casual'

    def get_color(self):
        return self.color

    def get_status(self):
        return self.status

    def make_queen(self):
        self.status = 'queen'

    def __repr__(self):
        return self.color


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
