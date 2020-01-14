import time, copy, random, os
import sqlite3, pygame
from PIL import Image, ImageOps


def get_bg_main_window(size):
    bg_main_window = Image.open('images/bg_main_window.png')
    bg_main_window = bg_main_window.resize(size, Image.ANTIALIAS)

    mode = bg_main_window.mode
    data = bg_main_window.tobytes()
    bg_main_window = pygame.image.fromstring(data, size, mode)
    return bg_main_window


def get_bg_tool_bar_map(size):
    bg_tool_bar_map = Image.open('images/bg_tool_bar_map.png')
    bg_tool_bar_map = bg_tool_bar_map.resize(size, Image.ANTIALIAS)

    mode = bg_tool_bar_map.mode
    data = bg_tool_bar_map.tobytes()
    bg_tool_bar_map = pygame.image.fromstring(data, size, mode)
    return bg_tool_bar_map


def get_btn_exit_main(size):
    btn_exit_main = Image.open('images/btn_exit_main.png')
    btn_exit_main = btn_exit_main.resize(size, Image.ANTIALIAS)

    mode = btn_exit_main.mode
    data = btn_exit_main.tobytes()
    btn_exit_main = pygame.image.fromstring(data, size, mode)
    return btn_exit_main


def get_btn_exit_main_click(size):
    btn_exit_main = Image.open('images/btn_exit_main_click.png')
    btn_exit_main = btn_exit_main.resize(size, Image.ANTIALIAS)

    mode = btn_exit_main.mode
    data = btn_exit_main.tobytes()
    btn_exit_main = pygame.image.fromstring(data, size, mode)
    return btn_exit_main


def get_btn_start_main_click(size):
    btn_start_main_click = Image.open('images/btn_start_main_click.png')
    btn_start_main_click = btn_start_main_click.resize(size, Image.ANTIALIAS)

    mode = btn_start_main_click.mode
    data = btn_start_main_click.tobytes()
    btn_start_main_click = pygame.image.fromstring(data, size, mode)
    return btn_start_main_click


def get_btn_start_main(size):
    btn_start_main = Image.open('images/btn_start_main.png')
    btn_start_main = btn_start_main.resize(size, Image.ANTIALIAS)

    mode = btn_start_main.mode
    data = btn_start_main.tobytes()
    btn_start_main = pygame.image.fromstring(data, size, mode)
    return btn_start_main


def get_btn_save_map(size):
    btn = Image.open('images/btn_save_map.png')
    btn = btn.resize(size, Image.ANTIALIAS)

    mode = btn.mode
    data = btn.tobytes()
    btn = pygame.image.fromstring(data, size, mode)
    return btn


def get_btn_save_map_click(size):
    btn = Image.open('images/btn_save_map_click.png')
    btn = btn.resize(size, Image.ANTIALIAS)

    mode = btn.mode
    data = btn.tobytes()
    btn = pygame.image.fromstring(data, size, mode)
    return btn

def get_image_player_on_mao(size):
    image = Image.open('images/player_on_map.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_main_objectsbar(size):
    image = Image.open('images/main_objectsbar.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_main_btnbar(size):
    image = Image.open('images/main_btnbar.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_bg_for_inventory(size):
    image = Image.open('images/bg_for_inventiry.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_bg_for_thinks_in_inventory(size):
    image = Image.open('images/bg_for_thinks_in_inventory.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_bg_for_tasks(size):
    image = Image.open('images/bg_for_tasks.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_for_main_map_window(size):
    image = Image.open('images/btn_for_main_map_window.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_for_main_map_window_1(size):
    image = Image.open('images/btn_for_main_map_window_1.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_for_main_map_window_2(size):
    image = Image.open('images/btn_for_main_map_window_2.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_3(size):
    image = Image.open('images/btn_for_main_map_window_3.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_4(size):
    image = Image.open('images/btn_for_main_map_window_4.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_5(size):
    image = Image.open('images/btn_for_main_map_window_5.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_6(size):
    image = Image.open('images/btn_for_main_map_window_6.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_for_main_map_window_1(size):
    image = Image.open('images/btn_for_main_map_window_1.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_for_main_map_window_2(size):
    image = Image.open('images/btn_for_main_map_window_2.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_3(size):
    image = Image.open('images/btn_for_main_map_window_3.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_4(size):
    image = Image.open('images/btn_for_main_map_window_4.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_5(size):
    image = Image.open('images/btn_for_main_map_window_5.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window_6(size):
    image = Image.open('images/btn_for_main_map_window_6.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_new_start_main(size):
    image = Image.open('images/btn_new_start_main.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_bg_for_time(size):
    image = Image.open('images/bg_for_time.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_new_start_main_click(size):
    image = Image.open('images/btn_new_start_main_click.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_bg_for_function(size):
    image = Image.open('images/bg_for_function.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_image_btn_inventory_on_location(size):
    image = Image.open('images/btn_inventory_on_location.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_search(size):
    image = Image.open('images/btn_search.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_map(size, mod=0):
    map = Image.open('images/map.png')
    map = map.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return map
    mode = map.mode
    data = map.tobytes()
    map = pygame.image.fromstring(data, size, mode)
    return map

def get_mark_for_map(size, mod=0):
    image = Image.open('images/mark_for_map.png')
    image = image.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return image
    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def cat_image(img, border):
    img = ImageOps.crop(img, border)
    return img

def get_tasks_image(size):
    image = Image.open('images/bg_for_task.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image

def get_pygame_image(image):
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)


def resize_image(image, size):
    image = image.resize(size, Image.ANTIALIAS)
    return image


def get_free_image(name, size, mod=0):
    image = Image.open(name)
    image = image.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return image
    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


WHITE = (255, 255, 255)  # установка цветов
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
LIGHT_GREEN = (27, 65, 16)
BROWN = (74, 47, 4)
GRAY = (128, 128, 128)

width, height = 0, 0


def install_size(size):  # инициализация
    global width, height
    width, height = size


def open_file():  # открывает файл с сохранением игрока
    with open('data/SaveGame.txt', 'r') as f:
        read_data = f.read()
    return read_data


def change_parametrs(id):  # нужно для заполнения карты

    # id;(x,y);количество макс. поисков;радиация;множитель скорости
    # id:количество:износ; и повторять так же     это то что можно найти
    # ????????????    это то кто может напасть
    # id:количество:износ; и повторять так же     это то что лежит на локации
    if id[0] == 0:
        parametrs = '''0;(x,y);0;-1;1
            NONE
            NONE
            NONE'''
    elif id[0] == 1:
        parametrs = '''1;(x,y);1000;0;0.05
            1:10000:0
            NONE
            NONE'''
    elif id[0] == 2:
        parametrs = '''2;(x,y);15;0;0.90
                    2:75:0;3:15:0;70:10:0;1:2:0
                    NONE
                    NONE'''
    elif id[0] == 3:
        parametrs = '''3;(x,y);20;0;0.70
            2:80:0;3:20:0;70:40:0
            NONE
            NONE'''
    elif id[0] == 4:
        parametrs = '''4;(x,y);20;0;0.90
            70:15:0;3:20:0;71:140:0
            NONE
            NONE'''
    elif id[0] == 5:
        parametrs = '''5;(x,y);5;0;1
            70:5:0;3:1:0;71:5:0
            NONE
            NONE'''
    elif id[0] == 6:
        parametrs = '''6;(x,y);0;1;0.85
            2:75:0;3:15:0;70:10:0
            NONE
            NONE'''
    elif id[0] == 7:
        parametrs = '''7;(x,y);5;2;1
            70:5:0;3:1:0;71:5:0
            NONE
            NONE'''
    elif id[0] == 8:
        parametrs = '''8;(x,y);3;0;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 9:
        parametrs = '''9;(x,y);3;2;1.6
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 10:
        parametrs = '''10;(x,y);3;1;1.5
            71:15:0;3:1:0;65:1:0
            NONE
            NONE'''
    elif id[0] == 11:
        parametrs = '''11;(x,y);3;1;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 12:
        parametrs = '''12;(x,y);3;1;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 13:
        parametrs = '''13;(x,y);4;3;0.4
            13:1:0;21:8:0;43:2:0;9:16:0;10:16:0;1:2:0
            NONE
            NONE'''
    elif id[0] == 14:
        parametrs = '''14;(x,y);4;3;0.4
            43:12:0;44:20:0;26:1:0;1:2:0;4:40:0
            NONE
            NONE'''
    elif id[0] == 15:
        parametrs = '''15;(x,y);4;4;0.3
            1:20:0;33:8:720;28:1:39200;60:2:480;46:16:0;57:24:0
            NONE
            NONE'''
    elif id[0] == 16:
        parametrs = '''16;(x,y);3;4;0.6
            6:70002:0;33:3:720;1:6:0;67:1:0
            NONE
            NONE'''
    elif id[0] == 17:
        parametrs = '''17;(x,y);3;4;0.6
            6:70002:0;33:3:720;1:6:0;67:1:0
            NONE
            NONE'''
    elif id[0] == 18:
        parametrs = '''18;(x,y);4;4;0.3
            1:20:0;33:8:720;28:1:39200;60:2:480;46:16:0;57:24:0
            NONE
            NONE'''
    elif id[0] == 19:
        parametrs = '''19;(x,y);5;2;0.4
            1:50:0;25:1:100;57:15:0;21:1:0
            NONE
            NONE'''
    elif id[0] == 20:
        parametrs = '''20;(x,y);4;2;0.4
            1:40:0;25:1:100;57:12:0;21:20:0
            NONE
            NONE'''
    elif id[0] == 21:
        parametrs = '''21;(x,y);3;2;0.3
            2:15:0;70:3:0;43:1:0;3:3:0
            NONE
            NONE'''
    elif id[0] == 22:
        parametrs = '''22;(x,y);2;3;0.4
            57:10:0;43:1:0
            NONE
            NONE'''
    elif id[0] == 23:
        parametrs = '''23;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 24:
        parametrs = '''24;(x,y);3;4;0.5
            4:3:0;42:3:0;40:2:0;39:2:0;36:6:0;35:6:0
            NONE
            NONE'''
    elif id[0] == 25:
        parametrs = '''25;(x,y);3;4;0.5
            4:3:0;42:3:0;40:2:0;39:2:0;36:6:0;35:9:0
            NONE
            NONE'''
    elif id[0] == 26:
        parametrs = '''26;(x,y);1;3;1
            65:1:0
            NONE
            NONE'''
    elif id[0] == 27:
        parametrs = '''27;(x,y);3;4;0.7
            65:1:0;6:1500:0;10:546:0;26:2:0;45:333:0;9:543:0;3:3:0
            NONE
            NONE'''
    elif id[0] == 28:
        parametrs = '''28;(x,y);6;4;0.7
            65:1:0;6:3000:0;10:546:0;26:2:0;45:333:0;9:543:0;3:6:0
            NONE
            NONE'''
    elif id[0] == 29:
        parametrs = '''29;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 30:
        parametrs = '''30;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 31:
        parametrs = '''31;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 32:
        parametrs = '''32;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 33:
        parametrs = '''33;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 34:
        parametrs = '''34;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 35:
        parametrs = '''35;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 36:
        parametrs = '''36;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 37:
        parametrs = '''37;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 38:
        parametrs = '''38;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 39:
        parametrs = '''39;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 40:
        parametrs = '''40;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 41:
        parametrs = '''41;(x,y);3;2;1
            3:6:0;1:6:0
            NONE
            NONE'''
    elif id[0] == 42:
        parametrs = '''42;(x,y);2;0;0.8
            3:16:0;70:8:0
            NONE
            NONE'''
    elif id[0] == 43:
        parametrs = '''43;(x,y);2;2;0.8
            3:16:0;70:8:0
            NONE
            NONE'''
    elif id[0] == 44:
        parametrs = '''44;(x,y);5;0;0.25
            3:90:0;1:15:0
            NONE
            NONE'''
    elif id[0] == 45:
        parametrs = '''45;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    else:
        parametrs = '''0;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    return parametrs


def ps_height(percent):  # возрощает число процентов от высоты
    percent = percent / 100
    return int(height * percent)


def ps_width(percent):  # возрощает число процентов от ширены
    percent = percent / 100
    return int(width * percent)


class Sparks(pygame.sprite.Sprite):  # частицы
    def __init__(self, all_sparks, image, dx, dy):
        super().__init__(all_sparks)
        self.image = image
        self.rect = self.image.get_rect()
        self.dx = dx
        self.dy = dy

        self.velocity = [dx, dy]
        pos = (random.choice(range(0, ps_width(100))),
               random.choice(range(ps_height(80), ps_height(100))))
        self.rect.x, self.rect.y = pos
        self.gravity = 1

    def update(self):
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect((-1, -1, width + 1, height + 1)):
            pos = (random.choice(range(0, ps_width(100))),
                   random.choice(range(ps_height(80), ps_height(100))))
            self.rect.x, self.rect.y = pos
            self.velocity = [self.dx, self.dy]


class Object:  # любой граффический объект
    def __init__(self, canvas, image, x, y, width, height):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visibility = True

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def change_image(self, image):
        self.image = image

    def check_tip(self, x, y):  # проверка на принодлежность х и у в объекте
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self):  # отобразить
        if self.visibility:
            self.canvas.blit(self.image, (self.x, self.y))


class Text(Object):
    def __init__(self, canvas, x, y, text, font, color=WHITE):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = str(text)
        self.font = font
        self.visibility = True
        self.color = color
        self.height = len(str(self.text).split('\n')) * ps_height(2)

    def change_text(self, new_text):
        self.text = str(new_text)

    def show(self):  # отобразить построчно
        if not self.visibility:
            return
        texts = str(self.text).split('\n')
        for i in range(len(texts)):
            text = self.font.render(texts[i], 1, self.color)
            self.canvas.blit(text, (self.x, int(self.y + i * ps_height(2))))


class Button(Object):  # кнопка
    def __init__(self, canvas, image, x, y, width, height, function=None, image_animation=None):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = [function]
        self.image_animation = image_animation
        self.visibility = True
        self.status = False

    def add_function(self, function):  # добовляет функцию
        if self.function == [None]:
            self.function = [function]
        else:
            self.function.append(function)

    def get_function(self, function):  # устонавливает одну функцию
        self.function = [function]

    def del_function(self):  # удоляет все функции
        self.function = [None]

    def get_image_animation(self, image):  # установка анимации при нажатии
        self.image_animation = image

    def show_animation(self):  # отобразить анимацию
        if self.image_animation is not None:
            self.canvas.blit(self.image_animation, (self.x, self.y))
        else:
            self.canvas.blit(self.image, (self.x, self.y))

    def click(self, *args):  # запустить все функции
        if self.function == [None] or not self.visibility:
            return False
        for function in self.function:
            try:
                return function(args)
            except:
                print('не удалось запустить функцию')
                return False

    def show(self):  # отобразить
        if self.visibility:
            if self.status:
                self.show_animation()
                return
            self.canvas.blit(self.image, (self.x, self.y))


class Call:  # клетка
    def __init__(self, canvas, x, y, size, color=BLACK, parametrs=None):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.visibility = True

        if parametrs is None:  # установка параметров по умолчанию
            self.id = '0'
            self.cor = (x, y)
            self.count = 0
            self.rad = '-1'
            self.speed = 1
            self.can_find = 'NONE'
            self.can_attack = 'NONE'
            self.lies = 'NONE'
        else:
            parametrs = parametrs.split()
            self.id = parametrs[0].split(';')[0]
            self.cor = (x, y)
            self.count = int(parametrs[0].split(';')[2])
            self.rad = parametrs[0].split(';')[3]
            self.speed = parametrs[0].split(';')[4]
            self.can_find = parametrs[1]
            self.can_attack = parametrs[2]
            self.lies = parametrs[3]

    def find_things(self):  # произвести поиск на клетке
        if self.count == 0:
            return
        can_find = []
        lies = []
        all_things_ling = {}
        all_things_can_find = {}
        if 'NONE' in self.lies:
            all_things_ling = {}
        else:
            for thing in self.lies.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_ling[id] = [count, strength]

        if 'NONE' in self.can_find:
            all_things_can_find = {}
        else:
            for thing in self.can_find.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_can_find[id] = [count, strength]

        for i in all_things_can_find.keys():
            id, count, strength = i, *all_things_can_find[i]
            if id in all_things_ling:
                all_things_ling[id][0] += count // self.count
                all_things_can_find[i][0] -= count // self.count
            else:
                all_things_ling[id] = [count // self.count, strength]
                all_things_can_find[i][0] -= count // self.count

        for i in all_things_ling.keys():
            lies.append(f'{i}:{all_things_ling[i][0]}:{all_things_ling[i][1]}')
        for i in all_things_can_find.keys():
            can_find.append(f'{i}:{all_things_can_find[i][0]}:{all_things_can_find[i][1]}')

        self.count -= 1
        self.lies = ';'.join(lies)
        self.can_find = ';'.join(can_find)

    def change_parametrs(self, parametrs):
        parametrs = parametrs.split()
        self.id = parametrs[0].split(';')[0]
        self.count = parametrs[0].split(';')[2]
        self.rad = parametrs[0].split(';')[3]
        self.speed = parametrs[0].split(';')[4]
        self.can_find = parametrs[1]
        self.can_attack = parametrs[2]
        self.lies = parametrs[3]

    def get_text_for_save(self):
        text = f'''{self.id};({self.cor[0]},{self.cor[1]});{self.count};{self.rad};{self.speed}
{self.can_find}
{self.can_attack}
{self.lies}</>
'''
        return text

    def show_mark(self, image, x, y):
        if image is None:
            return
        self.canvas.blit(image, (x, y))

    def draw(self, x, y, font):
        if not self.visibility or x < 0 or y < 0 or x > 1700 or y > 1000:
            return
        pygame.draw.rect(self.canvas, self.color, (x, y, self.size, self.size), 1)
        if self.id != '0':
            text = font.render(self.id, 1, WHITE)
            self.canvas.blit(text, (x + 2, y + 4))


class Board:
    def __init__(self, canvas, width, height, font, cell_size=10, visibility=True, parametrs=None):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.font = font
        self.visibility = visibility
        if parametrs is not None:
            parametrs = parametrs.split('</>')

        self.board_with_marks = []
        self.board = []
        for j in range(height):
            self.board.append([])
            for i in range(width):
                param = None
                if parametrs is not None:
                    index = j * width + i
                    param = parametrs[index]
                self.board[j].append(Call(canvas, i, j, cell_size, parametrs=param))
                if self.board[j][i].lies != 'NONE':
                    self.board_with_marks.append(self.board[j][i])
        self.left = 0
        self.top = 0
        self.cell_size = cell_size
        self.image_mark = None

    def set_move(self, left, top):
        self.left = left
        self.top = top

    def change_size_call(self, new_size):
        self.cell_size = new_size
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].size = new_size

    def show_all_marks(self, size_call, left, top):
        for call in self.board_with_marks:
            x = call.x * size_call + left
            y = call.y * size_call + top
            call.show_mark(self.image_mark, x, y)

    def render(self):
        if not self.visibility:
            return
        for i in range(self.height):
            for j in range(self.width):
                x = j * self.cell_size + self.left
                y = i * self.cell_size + self.top
                self.board[i][j].draw(x, y, self.font)

    def made_unvisibility_call(self, x, y, width, height):
        for i in range(self.height):
            for j in range(self.width):
                if (i >= y and i <= y + height and j >= x and j <= x + width):
                    self.board[i][j].visibility = True
                else:
                    self.board[i][j].visibility = False

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return x, y

    def get_call_in_bord(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return self.board[y][x]


class Window(Object):
    def __init__(self, canvas, image, x, y, width, height, column_count):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.column_count = column_count
        self.visibility = True
        self.paging = False
        self.mod = True
        self.objects = []
        self.shift_y = y
        self.width_object = 70
        self.last_x, self.last_y = 0, 0

    def show_all(self):
        for object in self.objects:
            object.visibility = True

    def hide_all(self):
        for object in self.objects:
            object.visibility = False

    def delete_all_objects(self):
        self.objects = []

    def add_object(self, object):
        object.visibility = self.visibility

        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (
                self.width // self.column_count) + self.x
        if self.column_count != 1:
            y = (len(self.objects) // self.column_count) * object.height + self.shift_y
        else:
            y = sum(map(lambda x: x.height, self.objects)) + self.shift_y + (ps_height(2) * len(self.objects))
        object.move_to(x, y)
        self.objects.append(object)

    def check(self, event):
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Function):
                    object.group_buttons.check(event)

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

                if isinstance(object, Function):
                    object.group_buttons.check(event)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def pag(self, y):
        self.shift_y = y
        if self.mod:  # следующие действия делают так,
            # чтоб объекты не выходили за границы экрана
            if self.shift_y > self.y:
                self.shift_y = self.y
            if ((len(self.objects) // self.column_count) + 1) >= (
                    self.height // self.width_object):

                if self.shift_y < -((((len(self.objects) // self.column_count)) - (
                        self.height // self.width_object))) * self.width_object:
                    self.shift_y = -((((len(self.objects) // self.column_count)) - (
                            self.height // self.width_object))) * self.width_object
            else:
                self.shift_y = self.y

        for i in range(len(self.objects)):
            object = self.objects[i]
            if self.column_count != 1:
                y = (i // self.column_count) * self.objects[i].height + self.shift_y
            else:
                y = sum(map(lambda x: x.height, self.objects[:i])) + self.shift_y + (ps_height(2) * i)
            object.move_to(object.x, y)

    def render(self):
        if not self.visibility:
            return
        if self.image is not None:
            self.show()
        for object in self.objects:
            object.show()


class Group:
    def __init__(self):
        self.all_objects = []
        self.last_x, self.last_y = 0, 0
        self.visibility = True

    def add_objects(self, *objects):
        for object in objects:
            self.all_objects.append(object)

    def delete(self, *objects):
        if len(objects) == 0:
            self.all_objects = []
        for object in objects:
            del self.all_objects[self.all_objects.index(object)]

    def off_all(self):
        for object in self.all_objects:
            object.visibility = False

    def on_all(self):
        for object in self.all_objects:
            object.visibility = True

    def check(self, event):
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def show(self):
        for object in self.all_objects:
            object.show()


class Player:
    def __init__(self, canvas, x, y, game_time):
        self.canvas = canvas
        self.width = 50
        self.height = 50
        self.image = get_image_player_on_mao((self.width, self.height))
        self.x = x
        self.y = y
        self.end_x = x
        self.end_y = y
        self.start_x = x
        self.start_y = y
        self.game_time = game_time
        self.deathing = None

        self.elementary_speed = 10
        self.start_speed = self.elementary_speed
        self.speed = self.start_speed
        self.path_length = 0
        self.time_for_way = 0
        self.moving = False
        self.timer = time.time()

        self.max_heft = 50000
        self.hunger = 100
        self.water = 100
        self.energy = 100
        self.poison = 0
        self.exhaustion = 0
        self.radiation = 0
        self.temperature = 36.6
        self.bleeding = 0

        self.change_hunger = 3
        self.change_water = 5
        self.change_energy = 2
        self.change_poison = 0
        self.change_exhaustion = 0
        self.change_radiation = 0
        self.change_temperature = 0
        self.change_bleeding = 0

        self.armor = 0
        self.damage = 10
        self.xp_chemistry = 0
        self.xp_survival = 0
        self.xp_mechanics = 0
        self.xp_sewing = 0

        self.effect_radiation = 0
        self.effect_satiety = 0
        self.effect_energy = 0

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_parametrs(self, parametrs):
        parametrs = parametrs.split('</>')[0].split(';')

        self.exhaustion = int(parametrs[0])
        self.hunger = int(parametrs[1])
        self.water = int(parametrs[2])
        self.poison = int(parametrs[3])
        self.radiation = int(parametrs[4])
        self.energy = int(parametrs[5])
        self.bleeding = int(parametrs[6])
        self.temperature = float(parametrs[7])
        self.max_heft = int(parametrs[8])

        self.armor = int(parametrs[9])
        self.xp_chemistry = int(parametrs[10])
        self.xp_survival = int(parametrs[11])
        self.xp_mechanics = int(parametrs[12])
        self.xp_sewing = int(parametrs[13])
        self.x = int(parametrs[14])
        self.y = int(parametrs[15])

        self.change_exhaustion = float(parametrs[16])
        self.change_hunger = float(parametrs[17])
        self.change_water = float(parametrs[18])
        self.change_poison = float(parametrs[19])
        self.change_radiation = float(parametrs[20])
        self.change_energy = float(parametrs[21])
        self.change_bleeding = float(parametrs[22])
        self.change_temperature = float(parametrs[23])

        self.game_time.num_time = int(parametrs[24])
        self.game_time.update_time()

    def set_cor(self, x, y):
        self.x = x
        self.y = y

    def check_condition(self, call=None):
        if call is not None:
            self.change_radiation = float(call.rad)
        self.change_exhaustion = -0.5
        if self.hunger < 0:
            self.hunger = 0
            self.change_exhaustion += 0.6
        elif self.hunger > 100:
            self.hunger = 100

        if self.water < 0:
            self.water = 0
            self.change_exhaustion += 0.8
        elif self.water > 100:
            self.water = 100

        if self.energy < 0:
            self.stop()
            self.energy = 100
            self.game_time.skip_time(7, self)  # делать так чтоб игрок сразу ложился спать
            self.energy = 100
        elif self.energy > 100:
            self.energy = 100

        if self.poison > 70:
            self.change_exhaustion += 1.5
        elif self.poison > 40:
            self.change_exhaustion += 0.7
        elif self.poison < 0:
            self.poison = 0

        if self.radiation < 0:
            self.radiation = 0
        elif self.radiation > 60:
            self.change_exhaustion += 1
        elif self.radiation > 40:
            self.change_exhaustion += 0.7
        elif self.radiation > 15:
            self.change_exhaustion += 0.4

        if self.temperature > 38:
            self.change_exhaustion += 1
            self.change_temperature += 0.1
        elif self.temperature > 37:
            self.change_exhaustion += 0.5
            self.change_temperature += 0.1
        elif self.temperature < 35:
            self.change_exhaustion += 0.2
            self.change_temperature -= 0.1
        elif self.temperature < 36:
            self.change_exhaustion += 0.1
            self.change_temperature -= 0.05

        if self.bleeding < 0:
            self.bleeding = 0
        elif self.bleeding > 70:
            self.change_exhaustion += 2.5
        elif self.bleeding > 50:
            self.change_exhaustion += 2
        elif self.bleeding > 20:
            self.change_exhaustion += 1
        if self.bleeding > 0:
            self.change_exhaustion += 0.1
            self.change_bleeding -= 0.2

        if self.exhaustion > 100:
            self.deathing()
        if self.exhaustion < 0:
            self.exhaustion = 0
        if self.exhaustion > 40:
            self.change_exhaustion -= 0.3

    def change_all_parametrs(self, delte_t):
        self.hunger -= self.change_hunger * delte_t
        self.water -= self.change_water * delte_t
        self.energy -= self.change_energy * delte_t
        self.poison += self.change_poison * delte_t
        self.exhaustion += self.change_exhaustion * delte_t
        self.radiation += (self.change_radiation - 0.4) * delte_t
        self.temperature -= self.change_temperature * delte_t
        self.bleeding += self.change_bleeding * delte_t

    def move_to(self, x, y):
        if self.inventory.heft > self.max_heft:
            return
        self.end_x = int(x)
        self.end_y = int(y)
        self.start_x = self.x
        self.start_y = self.y
        self.path_length = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        self.length_x = abs(x - self.start_x)
        self.length_y = abs(y - self.start_y)

        self.passed_x = 0
        self.passed_y = 0

        #   self.time_for_way = self.path_length / self.speed
        self.game_time.start_thinktime()
        self.moving = True

    def stop(self):
        self.moving = False
        self.x = int(self.x)
        self.y = int(self.y)
        self.end_x = self.x
        self.end_y = self.y
        self.start_x = self.x
        self.start_y = self.y

    def made_step(self):
        delte_t = self.game_time.change_game_time() / 3600
        shift_x = (self.end_x - self.start_x) * (delte_t / (self.path_length / self.speed))
        shift_y = (self.end_y - self.start_y) * (delte_t / (self.path_length / self.speed))

        self.length_x -= abs(shift_x)
        self.length_y -= abs(shift_y)
        self.passed_x += shift_x
        self.passed_y += shift_y
        self.change_all_parametrs(delte_t)

        if self.length_x < 0 or self.length_y < 0:
            self.x = self.end_x
            self.y = self.end_y
            self.moving = False
            return

        self.x = self.start_x + self.passed_x
        self.y = self.start_y + self.passed_y

    def show(self, map_x_on_main_map=0, map_y_on_main_map=0, map_x=0, map_y=0, zoom=1):
        self.canvas.blit(self.image, ((self.x - map_x_on_main_map) * zoom + map_x - self.width // 2,
                                      (self.y - map_y_on_main_map) * zoom + map_y - self.height // 2))


class Thing(Button):
    def __init__(self, canvas, id, con, count, strength, w=ps_width(8.9),
                 font=None, inventory=None, location=None, my_inventory=None, call=None):
        self.canvas = canvas
        self.count = int(count)
        self.font = font
        self.inventory = inventory
        self.location = location
        self.my_inventory = my_inventory
        self.x = 0
        self.y = 0
        self.visibility = True
        self.text_visibility = True
        self.status = False
        self.selected = False
        self.call = call
        self.con = con

        cur = con.cursor()
        query = f'''SELECT * FROM things
            WHERE id = {id}'''
        result = cur.execute(query).fetchone()

        self.id = int(result[0])
        self.name = result[1]
        self.heft = int(result[2])
        self.type = int(result[3])
        self.start_strength = int(result[4])
        self.strength = int(strength)
        self.effect_hunger = int(result[5])
        self.effect_water = int(result[6])
        self.effect_energy = int(result[7])
        self.effect_poison = int(result[8])
        self.effect_bleeding = int(result[9])
        self.effect_exhaustion = int(result[10])
        self.effect_radiation = int(result[11])
        self.damage = int(result[12])
        self.armor = int(result[13])
        self.effect_satiety_ps = int(result[14])
        self.effect_energy_ps = int(result[15])
        self.effect_radiation_ps = int(result[16])
        self.effect_light = int(result[17])
        self.expenses = result[18]
        w = w
        h = w
        self.image = get_free_image(result[19], (w, h))
        self.width = w
        self.height = h

        self.speed = 0
        self.carrying_capacity = 0
        if self.name == 'велосепед':
            self.speed = 20
            self.carrying_capacity = 70000
        elif self.name == 'чемодан':
            self.carrying_capacity = 30000

        self.functions = Window(canvas, None, ps_width(51), ps_height(20), ps_width(46), ps_height(60), 1)
        self.functions.mod = False
        self.functions.visibility = False
        self.update_function()

    def update_text(self):
        expiration_text = '...'
        if self.type == 9 or self.type == 2 or self.type == 3:
            if self.strength != 0:
                expiration_text = f'испортится через {self.strength} часов'
            else:
                expiration_text = f'никогда не испортится'
        elif self.type == 4 or self.type == 6 or self.type == 7 or self.type == 11:
            if self.strength != 0:
                expiration_text = f'сломается через {self.strength} применений'
            else:
                expiration_text = f'продержется больше чем ваша жизнь!'

        text = f'{self.name}\nВес: {self.heft * self.count}г.\n{expiration_text}\n...'
        self.functions.objects[0].text = text

    def update_function(self):
        self.functions.delete_all_objects()

        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_width(1.5))
        text = Text(self.canvas, 0, 0, '\n\n\n', font)
        text.color = BLACK
        self.functions.add_object(text)
        self.update_text()

        function_mod = 1
        if self.my_inventory == self.inventory:
            function_mod = 2

        if self.type != 11:
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(20)
            function = Function(self.canvas, x, y, w, h, self, self.inventory, self.location,
                                self.my_inventory, call=self.call, function_mod=function_mod,
                                button_size=70)
            function.set_bg_image()
            self.functions.add_object(function)

        if self.type == 9:
            function_mod = 3
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(31)
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

        if self.type == 2:
            function_mod = 4
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(31)
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

        if self.type == 3:
            function_mod = 5
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(31)
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

        if self.type == 7:
            function_mod = 6
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(31)
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

            function_mod = 7
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

        if self.type == 10:
            function_mod = 8
            x, y = ps_width(51), ps_height(20)
            w, h = ps_width(46), ps_height(31)
            function = Function(self.canvas, x, y, w, h, self, self.inventory,
                                self.location,
                                self.my_inventory, call=self.call,
                                function_mod=function_mod,
                                button_size=70)
            function.set_bg_image('images/bg_for_function_9.png')
            self.functions.add_object(function)

    def open_functions(self):
        self.functions.visibility = True
        self.functions.show_all()

    def close_functions(self):
        self.functions.visibility = False
        self.functions.hide_all()

    def change_call(self, call):
        self.call = call
        for fun in self.functions.objects:
            fun.call = call

    def get_text_for_saving(self, sep=';'):
        return f'{self.id}{sep}{self.count}{sep}{self.strength}'

    def click(self, *args):
        try:
            self.my_inventory.hide_all_function()
            self.open_functions()
        except:
            print('не удалось запустить функцию')
            return False

    def show(self):
        self.functions.render()
        pygame.draw.rect(self.canvas, BROWN, (self.x, self.y, self.width, self.height), ps_height(0.6))

        self.canvas.blit(self.image, (self.x, self.y))
        if self.font is not None:
            if self.text_visibility:
                text = self.font.render(str(self.count), 1, BLACK)
                self.canvas.blit(text, (self.x + self.width - ps_width(4),
                                        self.y + self.height - ps_height(4.3)))


class Inventory:
    def __init__(self, canvas, bg_image, player, mod=1):
        self.canvas = canvas
        self.bg_image = bg_image
        self.bg_for_thinks = get_bg_for_thinks_in_inventory((width, ps_height(83.2)))
        self.con = sqlite3.connect("item_base.db")
        self.heft = 0
        self.player = player
        self.mod = mod
        if mod == 1:
            player.set_inventory(self)

        self.visibility = False
        self.all_thinks = None
        self.groupe_for_thinks = Group()
        self.showing_thinks = None
        self.last_call = None
        self.BOARD_MAP = None

        self.window = None

        x = ps_width(50.5)
        y = ps_height(10)
        w = ps_width(50.1)
        h = ps_height(20)
        self.cane_find_window = Window(canvas, None, x, y, w, h, 6)
        self.cane_find_window.width_object = ps_width(5)

    def initialization(self, parameters, inventory, location, call=None, BOARD_MAP=None):
        self.last_call = call
        self.inventory = inventory
        self.location = location
        self.BOARD_MAP = BOARD_MAP
        separator = ';'
        if parameters is None:
            all_thinks = []
        elif self.mod == 1:
            all_thinks = parameters.split('</>')[1].split(', ')
            if all_thinks == ['\n']:
                all_thinks = []
        else:
            if 'NONE' in parameters.split('\n')[3]:
                all_thinks = []
            else:
                all_thinks = parameters.split('\n')[3].split(';')
                separator = ':'

        self.all_thinks = self.convert_thinks_to_object(all_thinks, separator,
                                                        ps_width(8.9), inventory, location, call=call)
        self.showing_thinks = self.all_thinks

        x = ps_width(2) + 2
        y = ps_height(28.51)
        w = ps_width(44.1)
        h = ps_height(56.8)

        self.window = Window(self.canvas, None, x, y, w, h, 5)
        self.window.visibility = True
        self.window.width_object = ps_width(8.9)
        for think in self.showing_thinks:
            self.window.add_object(think)

    def convert_thinks_to_object(self, all_thinks, sep=';', w=50, inventory=None,
                                 location=None, call=None):
        if any(map(lambda x: x is None, (inventory, location))):
            inventory = self.inventory  # если хотя бы один равен None
            location = self.location
            if any(map(lambda x: x is None, (inventory, location))):
                return  # если хотя бы один равен None
        ready_thinks = []
        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', int(w // 3.5))
        self.heft = 0
        for think in all_thinks:
            if 'NONE' not in think:
                id, count, strength = think.split(sep)
                if int(count) > 0:
                    if sep == ':':
                        strength = strength.split('</>')[0]
                    think = Thing(self.canvas, id, self.con, count, strength, w, font,
                                  inventory, location, self, call=call)
                    self.heft += think.heft * int(count)
                    self.groupe_for_thinks.add_objects(think.functions)

                    ready_thinks.append(think)
        return ready_thinks

    def update_call(self, call):
        self.last_call = call
        for i in range(len(self.window.objects)):
            self.window.objects[i].change_call(call)
        self.showing_thinks = self.all_thinks

    def update_cane_find(self, call):
        self.cane_find_window.objects = []
        can_find = call.can_find
        if 'NONE' in can_find:
            return
        for think in self.convert_thinks_to_object(call.can_find.split(';'), ':', ps_width(5), call=call):
            think.text_visibility = False
            self.cane_find_window.add_object(think)

    def update_thinks(self, all_thinks):
        self.all_thinks = all_thinks
        self.showing_thinks = all_thinks
        self.window.objects = []
        for think in self.showing_thinks:
            self.window.add_object(think)

    def find_think(self, think):
        for my_think in self.all_thinks:
            if think.id == my_think.id and think.strength == my_think.strength:
                return my_think
        return False

    def append_think(self, think, my_think, count):
        if my_think not in self.all_thinks:
            if count != 0:
                w = ps_width(8.9)
                font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', int(w // 3.5))

                my_think = Thing(self.canvas, think.id, self.con, count, think.strength, w,
                                 font, self.inventory, self.location, self, call=self.last_call)
                self.groupe_for_thinks.add_objects(think.functions)

                self.all_thinks.append(my_think)
                self.showing_thinks = self.all_thinks
                self.window.add_object(my_think)
        else:
            my_think.count += count
            self.showing_thinks = self.all_thinks
        self.heft += think.heft * count
        for think in self.all_thinks:
            think.update_text()

    def delete_think(self, think, my_think, count):
        if count == int(my_think.count):
            self.heft -= my_think.heft * count
            del self.all_thinks[self.all_thinks.index(my_think)]
            self.showing_thinks = self.all_thinks
            self.window.delete_all_objects()
            for think in self.showing_thinks:
                self.window.add_object(think)
        else:
            self.heft -= think.heft * count
            my_think.count -= count

        for think in self.all_thinks:
            think.update_text()

    def change_thinks(self, think, count, call):
        if think.count <= 0:
            return
        my_think = self.find_think(think)
        think = copy.copy(think)

        if count > 0:
            self.append_think(think, my_think, count)
        elif count < 0:
            self.delete_think(think, my_think, -count)
        if self.mod != 1:
            was = call.lies
            call.lies = self.get_text_for_saving(';')
            if call.lies != 'NONE' and was == 'NONE':
                self.BOARD_MAP.board_with_marks.append(call)
            elif was != 'NONE' and call.lies == 'NONE':
                del self.BOARD_MAP.board_with_marks[self.BOARD_MAP.board_with_marks.index(call)]

    def get_text_for_saving(self, sep=', '):
        if sep == ';':
            all_thinks = list(map(lambda x: x.get_text_for_saving(':'), self.all_thinks))
        else:
            all_thinks = list(map(lambda x: x.get_text_for_saving(), self.all_thinks))
        all_thinks = sep.join(all_thinks)
        if sep == ', ':
            text = all_thinks + '</>'
        else:
            text = all_thinks
            if text == '':
                text = 'NONE'
        return text

    def get_ps_of_load(self):
        ps = int(100 * self.heft / self.player.max_heft)
        if ps > 999:
            ps = 999
        return ps

    def check(self, event):
        if self.visibility:
            self.window.check(event)
            self.groupe_for_thinks.check(event)
            self.check_all_buttons_of_function(event)

    def check_all_buttons_of_function(self, event):
        for think in self.window.objects:
            think.functions.check(event)

    def hide_all_function(self):
        for think in self.window.objects:
            think.close_functions()

    def show(self):
        if self.visibility:
            self.canvas.blit(self.bg_image, (0, ps_height(5.6)))
            self.window.render()
            self.cane_find_window.render()
            self.canvas.blit(self.bg_for_thinks, (0, ps_height(5.6)))


class Function:
    def __init__(self, canvas, x, y, w, h, thing, inventory, location,
                 my_inventory, function_mod=1, button_size=50, call=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.height = h
        self.visibility = True
        self.thing = thing
        self.bg_image = None
        self.inventory = inventory
        self.location = location
        self.my_inventory = my_inventory
        self.button_size = button_size
        self.call = call

        self.group_buttons = Group()

        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_width(1.7))
        self.title_text = Text(self.canvas, self.x + ps_height(0.5),
                               self.y + ps_height(0.5), '', font)

        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_width(1.3))
        self.description_text = Text(self.canvas, self.x + ps_width(0.5),
                                     self.y + ps_height(5.5), '', font)

        self.change_function(function_mod)

    def set_bg_image(self, name=None):
        if name is None:
            self.bg_image = get_image_bg_for_function((self.w, self.h))
        else:
            self.bg_image = get_free_image(name, (self.w, self.h))

    def change_function(self, function_mod):
        # 1 - подобрать предмет
        # 2 - скинуть предмет
        # 3 - выпить
        # 4 - съесть
        # 5 - применить
        # 6 - одеть
        # 7 - снять
        # 8 - открыть

        name_buttons = []
        name = 'images/action_button_'
        if function_mod == 1:
            self.title_text.text = f'Поднять предмет'
            self.description_text.text = 'поднять 1/10/100/все'

            name_buttons = ('1', '10', '100', 'all')
            for i in range(len(name_buttons)):
                x = self.x + self.w // len(name_buttons) * i
                y = self.y + self.h - self.button_size
                image = get_free_image(name + name_buttons[i] + '.png', (self.button_size, self.button_size))
                button = Button(self.canvas, image, x, y, self.button_size, self.button_size)
                if i == 0:
                    button.add_function(self.pick_up_an_item_1)
                elif i == 1:
                    button.add_function(self.pick_up_an_item_10)
                elif i == 2:
                    button.add_function(self.pick_up_an_item_100)
                else:
                    button.add_function(self.pick_up_an_item_all)
                self.group_buttons.add_objects(button)

        if function_mod == 2:
            self.title_text.text = f'Сбросить предмет'
            self.description_text.text = 'сбросить 1/10/100/все'

            name_buttons = ('1', '10', '100', 'all')
            for i in range(len(name_buttons)):
                x = self.x + self.w // len(name_buttons) * i
                y = self.y + self.h - self.button_size
                image = get_free_image(name + name_buttons[i] + '.png', (self.button_size, self.button_size))
                button = Button(self.canvas, image, x, y, self.button_size, self.button_size)
                if i == 0:
                    button.add_function(self.drop_item_1)
                elif i == 1:
                    button.add_function(self.drop_item_10)
                elif i == 2:
                    button.add_function(self.drop_item_100)
                else:
                    button.add_function(self.drop_item_all)
                self.group_buttons.add_objects(button)

        if function_mod == 3:
            self.title_text.text = f'Попить'

            if self.thing.effect_radiation < 0:
                t_1 = f'увеличение радиации на {-self.thing.effect_radiation}'
            else:
                t_1 = f'уменьшение радиации на {self.thing.effect_radiation}'
            if self.thing.effect_poison < 0:
                t_2 = f'повышение отравления на {-self.thing.effect_poison}'
            else:
                t_2 = f'уменьшение отравления на {self.thing.effect_poison}'

            self.description_text.text = f'''выпить {self.thing.name} и получить эффекты
удаление жажды на {self.thing.effect_water}
{t_1}
удаление голода на {self.thing.effect_hunger}
{t_2}
востановление энергии на {self.thing.effect_energy}
так же измениться истощение на сколько-то'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2, self.button_size)
            button.add_function(self.eating)
            self.group_buttons.add_objects(button)

        if function_mod == 4:
            self.title_text.text = f'Поесть'

            if self.thing.effect_radiation < 0:
                t_1 = f'увеличение радиации на {-self.thing.effect_radiation}'
            else:
                t_1 = f'уменьшение радиации на {self.thing.effect_radiation}'
            if self.thing.effect_poison < 0:
                t_2 = f'повышение отравления на {-self.thing.effect_poison}'
            else:
                t_2 = f'уменьшение отравления на {self.thing.effect_poison}'

            self.description_text.text = f'''съесть {self.thing.name} и получить эффекты
удаление голода на {self.thing.effect_hunger}
{t_1}
удаление жажды на {self.thing.effect_water}
{t_2}
востановление энергии на {self.thing.effect_energy}
так же измениться истощение на сколько-то'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (
                self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2,
                            self.button_size)
            button.add_function(self.eating)
            self.group_buttons.add_objects(button)

        if function_mod == 5:
            self.title_text.text = f'Применить'
            if self.thing.effect_radiation < 0:
                t_1 = f'увеличение радиации на {-self.thing.effect_radiation}'
            else:
                t_1 = f'уменьшение радиации на {self.thing.effect_radiation}'
            if self.thing.effect_poison < 0:
                t_2 = f'повышение отравления на {-self.thing.effect_poison}'
            else:
                t_2 = f'уменьшение отравления на {self.thing.effect_poison}'

            self.description_text.text = f'''съесть {self.thing.name} и получить эффекты
{t_1}
{t_2}
уменьшение кровотечения на {self.thing.effect_bleeding}
востановление энергии на {self.thing.effect_energy}
так же измениться истощение на сколько-то'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (
                self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2,
                            self.button_size)
            button.add_function(self.eating)
            self.group_buttons.add_objects(button)

        if function_mod == 6:
            self.title_text.text = f'Надеть'
            t_1 = ''
            t_2 = ''
            t_3 = ''
            t_4 = ''
            t_5 = ''
            t_6 = ''
            t_7 = ''

            if self.thing.armor != 0:
                t_1 = f'защита: {self.thing.armor}\n'
            if self.thing.damage != 0:
                t_2 = f'урон: {self.thing.damage}\n'
            if self.thing.speed != 0:
                t_6 = f'скорость: {self.thing.speed // 2} км/ч\n'
            if self.thing.effect_satiety_ps != 0:
                t_3 = f'эффект сытности: {self.thing.effect_satiety_ps}\n'
            if self.thing.effect_radiation_ps != 0:
                t_4 = f'защита от радиации: {self.thing.effect_radiation_ps}\n'
            if self.thing.effect_light != 0:
                t_5 = f'повышение освещённости: {self.thing.effect_light}\n'
            if self.thing.carrying_capacity != 0:
                t_7 = f'повышение грузоподъёмности: на {self.thing.carrying_capacity // 1000} кг.\n'

            self.description_text.text = f'''одеть {self.thing.name} и получить такие параметры
{t_1}{t_2}{t_6}{t_7}{t_3}{t_4}{t_5}'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (
                self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2,
                            self.button_size)
            button.add_function(self.clothe)
            self.group_buttons.add_objects(button)

        if function_mod == 7:
            self.title_text.text = f'Снять'
            t_1 = ''
            t_2 = ''
            t_3 = ''
            t_4 = ''
            t_5 = ''
            t_6 = ''
            t_7 = ''

            if self.thing.armor != 0:
                t_1 = f'защита: 0\n'
            if self.thing.damage != 0:
                t_2 = f'урон: 0\n'
            if self.thing.speed != 0:
                t_6 = f'скорость: {self.my_inventory.player.elementary_speed // 2} км/ч\n'
            if self.thing.effect_satiety_ps != 0:
                t_3 = f'эффект сытности: 0\n'
            if self.thing.effect_radiation_ps != 0:
                t_4 = f'защита от радиации: 0\n'
            if self.thing.effect_light != 0:
                t_5 = f'повышение освещённости: 0\n'
            if self.thing.carrying_capacity != 0:
                t_7 = f'понижение грузоподъёмности: на {self.thing.carrying_capacity // 1000} кг.\n'

            self.description_text.text = f'''снять {self.thing.name} и получить такие параметры
{t_1}{t_2}{t_6}{t_7}{t_3}{t_4}{t_5}'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (
                self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2,
                            self.button_size)
            button.add_function(self.take_off)
            self.group_buttons.add_objects(button)

        if function_mod == 8:
            self.title_text.text = f'Открыть'

            self.description_text.text = f'''открыть {self.thing.name} и получить:
 * спички Х 20
 * шашлык Х 2
 * чемодан Х 1
 * вода(чистая) Х 25
 * инструменты Х 1
 * лопата Х 1
 * порох Х 500'''

            x = self.x + self.w // 2 - self.button_size
            y = self.y + self.h - self.button_size
            image = get_free_image('images/action_button_1.png', (
                self.button_size * 2, self.button_size))
            button = Button(self.canvas, image, x, y, self.button_size * 2,
                            self.button_size)
            button.add_function(self.take_think)
            self.group_buttons.add_objects(button)

    def take_think(self, *args):
        think = Thing(self.canvas, 21, self.thing.con, 20, 0, font=self.thing.font,
                      inventory=self.inventory, location=self.location, my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 20, self.thing.call)

        think = Thing(self.canvas, 54, self.thing.con, 2, 0, font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 2, self.thing.call)

        self.my_inventory.player.game_time.skip_time(0.5, self.my_inventory.player)

        think = Thing(self.canvas, 67, self.thing.con, 1, 0,
                      font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 1, self.thing.call)

        think = Thing(self.canvas, 33, self.thing.con, 25, 0,
                      font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 25, self.thing.call)

        think = Thing(self.canvas, 25, self.thing.con, 1, 0,
                      font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 1, self.thing.call)

        think = Thing(self.canvas, 23, self.thing.con, 1, 0,
                      font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 1, self.thing.call)

        think = Thing(self.canvas, 11, self.thing.con, 500, 0,
                      font=self.thing.font,
                      inventory=self.inventory, location=self.location,
                      my_inventory=self.location,
                      call=self.thing.call, w=ps_width(8.9))
        self.location.change_thinks(think, 500, self.thing.call)

        self.my_inventory.change_thinks(self.thing, -1, self.call)

    def clothe(self, *args):
        if self.my_inventory == self.location or self.thing.selected:
            return
        self.thing.selected = True
        self.my_inventory.player.max_heft += self.thing.carrying_capacity
        self.inventory.heft -= self.thing.heft
        if self.thing.speed != 0:
            self.my_inventory.player.start_speed = self.thing.speed
        if self.thing.armor != 0:
            self.my_inventory.player.armor = self.thing.armor
        if self.thing.damage != 0:
            self.my_inventory.player.damage = self.thing.damage
        if self.thing.effect_satiety_ps != 0:
            self.my_inventory.player.effect_satiety = self.thing.effect_satiety_ps
        if self.thing.effect_radiation_ps != 0:
            self.my_inventory.player.effect_radiation = self.thing.effect_radiation_ps

    def take_off(self, *args):
        if not self.thing.selected:
            return
        self.inventory.heft += self.thing.heft
        self.my_inventory.player.max_heft -= self.thing.carrying_capacity
        self.thing.selected = False
        if self.thing.speed != 0:
            self.my_inventory.player.start_speed = self.my_inventory.player.elementary_speed
        if self.thing.armor != 0:
            self.my_inventory.player.armor = 0
        if self.thing.damage != 0:
            self.my_inventory.player.damage = 10
        if self.thing.effect_satiety_ps != 0:
            self.my_inventory.player.effect_satiety = 0
        if self.thing.effect_radiation_ps != 0:
            self.my_inventory.player.effect_radiation = 0

    def eating(self, *args):
        self.my_inventory.player.game_time.skip_time(0.2, self.my_inventory.player)
        self.my_inventory.change_thinks(self.thing, -1, self.call)
        self.my_inventory.player.hunger += self.thing.effect_hunger
        self.my_inventory.player.water += self.thing.effect_water
        self.my_inventory.player.poison -= self.thing.effect_poison
        self.my_inventory.player.radiation -= self.thing.effect_radiation
        self.my_inventory.player.energy += self.thing.effect_energy
        self.my_inventory.player.bleeding += self.thing.effect_bleeding
        self.my_inventory.player.exhaustion -= self.thing.effect_exhaustion
        self.my_inventory.player.check_condition()

    def pick_up_an_item_1(self, *args):
        self.location.change_thinks(self.thing, -1, self.call)
        self.inventory.change_thinks(self.thing, 1, self.call)

    def pick_up_an_item_10(self, *args):
        if 10 > self.thing.count:
            return
        self.location.change_thinks(self.thing, -10, self.call)
        self.inventory.change_thinks(self.thing, 10, self.call)

    def pick_up_an_item_100(self, *args):
        if 100 > self.thing.count:
            return
        self.location.change_thinks(self.thing, -100, self.call)
        self.inventory.change_thinks(self.thing, 100, self.call)

    def pick_up_an_item_all(self, *args):
        self.location.change_thinks(self.thing, -self.thing.count, self.call)
        self.inventory.change_thinks(self.thing, self.thing.count, self.call)

    def drop_item_1(self, *args):
        if self.thing.selected:
            return
        self.location.change_thinks(self.thing, 1, self.call)
        self.inventory.change_thinks(self.thing, -1, self.call)

    def drop_item_10(self, *args):
        if 10 > self.thing.count or self.thing.selected:
            return

        self.location.change_thinks(self.thing, 10, self.call)
        self.inventory.change_thinks(self.thing, -10, self.call)

    def drop_item_100(self, *args):
        if 100 > self.thing.count or self.thing.selected:
            return
        self.location.change_thinks(self.thing, 100, self.call)
        self.inventory.change_thinks(self.thing, -100, self.call)

    def drop_item_all(self, *args):
        if self.thing.selected:
            return
        self.location.change_thinks(self.thing, self.thing.count, self.call)
        self.inventory.change_thinks(self.thing, -self.thing.count, self.call)

    def move_to(self, x, y):
        self.height = self.h
        self.x, self.y = x, y
        self.title_text.x = x + ps_height(0.5)
        self.title_text.y = y + ps_height(1.5)
        self.description_text.x = x + ps_width(0.5)
        self.description_text.y = y + ps_height(6)

        for i in range(len(self.group_buttons.all_objects)):
            button = self.group_buttons.all_objects[i]
            x = self.x + self.w // len(self.group_buttons.all_objects) * i
            y = self.y + self.h - self.button_size
            button.move_to(x, y)

    def show(self):
        if not self.visibility:
            return
        if self.bg_image is not None:
            self.canvas.blit(self.bg_image, (self.x, self.y))
        self.title_text.show()
        self.description_text.show()
        self.group_buttons.show()


class GameTime:
    def __init__(self, t, canvas):
        self.bg = get_bg_for_time((width, height))
        self.num_time = t
        self.canvas = canvas
        self.time = time.localtime(t)
        self.timer = 0
        self.expectation_timer = 0

        self.real_timer = time.time()
        self.font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_width(1.4))

    def start_thinktime(self):
        self.timer = time.time()

    def update_time(self):
        self.time = time.localtime(self.num_time)

    def skip_time(self, expectation, player):
        self.expectation_timer = time.time()
        t_game = 0

        all_sparks = pygame.sprite.Group()
        image = get_free_image('images\explotion.png', (ps_height(2), ps_height(2)))
        for _ in range(25):
            dx = random.choice(range(-30, 30))
            dy = random.choice(range(-10, 20))
            Sparks(all_sparks, image, dx, dy)

        clock = pygame.time.Clock()
        while expectation >= 0:
            clock.tick(100)
            self.canvas.fill(BLACK)
            all_sparks.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                if event.type == pygame.MOUSEMOTION:
                    pass

            delte_t = time.time() - self.expectation_timer
            self.expectation_timer = time.time()
            self.num_time += delte_t * 3600

            self.canvas.blit(self.bg, (0, 0))

            t_real = abs(int(expectation + 1))
            t_game += delte_t * 60

            player.change_all_parametrs(delte_t)
            text = self.font.render(f'{t_real} сек.', 1, WHITE)
            self.canvas.blit(text, (ps_width(45), ps_height(35)))
            text = self.font.render(f'{int(t_game)} мин.', 1, WHITE)
            self.canvas.blit(text, (ps_width(45), ps_height(67)))
            all_sparks.draw(self.canvas)

            expectation -= delte_t

            pygame.display.flip()
        self.time = time.localtime(self.num_time)
        player.check_condition()

    def change_game_time(self, timer=None):
        if timer is None:
            delte_t = time.time() - self.timer
        else:
            delte_t = time.time() - timer
        self.num_time += delte_t * 3600
        self.time = time.localtime(self.num_time)
        self.timer = time.time()
        return delte_t * 3600

    def update_time_on_real_time(self):
        delte_t = time.time() - self.real_timer
        self.num_time += delte_t
        self.time = time.localtime(self.num_time)
        self.real_timer = time.time()
        return delte_t

    def get_string_of_time(self):
        hour = str(self.time.tm_hour).rjust(2, '0')
        min = str(self.time.tm_min).rjust(2, '0')
        sec = str(self.time.tm_sec).rjust(2, '0')
        string = f'''{self.time.tm_mday}.{self.time.tm_mon}.{self.time.tm_year
        } {hour}:{min}:{sec}'''
        return string

    def show(self):
        text = self.font.render(self.get_string_of_time(), 1, LIGHT_GREEN)
        self.canvas.blit(text, (ps_width(44), ps_height(91)))


class Tasks:
    def __init__(self, canvas, bg_image):
        self.canvas = canvas
        self.bg_image = bg_image
        self.con = sqlite3.connect("data/tasks_base.db")
        self.visibility = False
        self.text_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(2.3))

    def show(self):
        if self.visibility:
            self.canvas.blit(self.bg_image, (0, ps_height(5.6)))

    def show_all_tasks(self):
        self.x = ps_width(2.5)
        self.y = ps_height(10.7)
        self.width = ps_width(26.1)
        self.height = ps_height(6.3)
        self.story_task_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3.5))
        self.side_task_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3))
        self.con = sqlite3.connect("data/tasks_base.db")
        self.get_actual_story_tasks()
        # self.get_actual_side_tasks()

    def get_actual_story_tasks(self):
        count = 0
        cur = self.con.cursor()
        actual_tasks = cur.execute("SELECT * from tasks WHERE progress IN(1) AND type_id IN(1)").fetchall()
        for elem in actual_tasks:
            if count < 11:
                self.id = id
                self.type_id = elem[1]
                self.name = elem[2]
                self.text = elem[3]
                self.completed = elem[4]

                pygame.draw.rect(self.canvas, BROWN, (self.x, self.y, self.width, self.height), ps_height(0.6))

                text1 = self.story_task_font.render(self.name, 1, BLACK)
                self.canvas.blit(text1, (self.x + ps_width(0.4), self.y + ps_height(0.14)))

                self.y += ps_height(6.3)
                count += 1
            else:
                break

    # def get_actual_side_tasks(self):
    #    cur = self.con.cursor()
    #    past_tasks = cur.execute("SELECT * from tasks WHERE progress IN(1) AND type_id IN(2)").fetchall()
    #    for elem in past_tasks:
    #        self.id = id
    #        self.type_id = elem[1]
    #        self.name = elem[2]
    #        self.text = elem[3]
    #        self.completed = elem[4]
    #
    #        pygame.draw.rect(self.canvas, BROWN, (self.x, self.y, self.width, self.height), ps_height(0.6))
    #
    #        text1 = self.side_task_font.render(self.name, 1, BLACK)
    #        self.canvas.blit(text1, (self.x + ps_width(0.4), self.y + ps_height(0.14)))
    #
    #        self.y += ps_height(6.3)
    #   названия побочных квестов должны были выводиться в конце и быть меньшего размера


def exit(*args):  # завершает программу
    global running
    running = False


def the_end():  # выполняется при смерти игрока
    start_new_game()
    opening_main_window()


def start_new_game(*args):  # обнуляет все сохранения
    description_map = open('map/description_map.txt', 'w')
    with open('map/start_description_map.txt', 'r') as f:
        text = f.read()
    description_map.write(text)
    description_map.close()

    description_player = open('data/SaveGame.txt', 'w')
    text = '''0;100;100;0;0;100;0;36.6;50000;0;0;0;0;0;700;500;0;1.5;3;-0.5;0;4;0;0;622080000</>
21;30;0, 33;5;720, 26;2;0, 25;1;0, 28;1;19000, 4;40;0</>'''
    description_player.write(text)
    description_player.close()
    show_starting_slides(10, "png")
    # ставит все квесты в начальное положение
    tasks_connect = sqlite3.connect("data/tasks_base.db")
    tasks_cursor = tasks_connect.cursor()
    tasks_cursor.execute("UPDATE tasks SET progress = 0")
    tasks_cursor.execute("UPDATE tasks SET progress = 1 WHERE id IN(1)")
    tasks_connect.commit()

    start()


def show_starting_slides(number, format):  # отображает слайды предистории
    count = 2
    image = get_free_image("images\start_slides\start_slide_1." + format, (width, height))
    start_slide = Object(screen, image, 0, 0, width, height)
    all_sparks = pygame.sprite.Group()

    image = get_free_image('images\explotion.png', (ps_height(2), ps_height(2)))
    for _ in range(25):
        dx = random.choice(range(-30, 30))
        dy = random.choice(range(-10, 20))
        Sparks(all_sparks, image, dx, dy)

    while count <= number + 1:
        clock.tick(FPS)
        screen.fill(BLACK)
        all_sparks.update()

        for event in pygame.event.get():
            if 1 in pygame.key.get_pressed() or event.type == pygame.MOUSEBUTTONDOWN:
                if count <= number:
                    slide_name = "images\start_slides\start_slide_" + str(count) + "." + format
                    image = get_free_image(slide_name, (width, height))
                    start_slide.change_image(image)
                    #start_slide = Object(screen, image, 0, 0, width, height)
                count += 1

        start_slide.show()
        all_sparks.draw(screen)
        pygame.display.flip()


def continue_game(*args):  # запускает игру с текущими сохранениями
    if os.path.exists('map/description_map.txt'):
        start()
    else:
        start_new_game()


def searching_on_call(*args):  # ищит предметы на локации
    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    was = call.lies
    call.find_things()
    location.update_thinks(location.convert_thinks_to_object(call.lies.split(';'), ':', ps_width(8.9), call=call))
    t = random.choice(range(3, 23))
    game_time.skip_time(t / 10, player)
    location.update_cane_find(call)
    if call.lies != 'NONE' and was == 'NONE':
        BOARD_MAP.board_with_marks.append(call)


def save():  # сохраняет текущии данные
    description_player = open('data/SaveGame.txt', 'w')
    text = ''
    text += str(int(player.exhaustion)) + ';'
    text += str(int(player.hunger)) + ';'
    text += str(int(player.water)) + ';'
    text += str(int(player.poison)) + ';'
    text += str(int(player.radiation)) + ';'
    text += str(int(player.energy)) + ';'
    text += str(int(player.bleeding)) + ';'
    text += str(player.temperature) + ';'
    text += str(50000) + ';'

    text += str(player.armor) + ';'
    text += str(player.xp_chemistry) + ';'
    text += str(player.xp_survival) + ';'
    text += str(player.xp_mechanics) + ';'
    text += str(player.xp_sewing) + ';'

    text += str(int(player.x)) + ';'
    text += str(int(player.y)) + ';'

    text += str(player.change_exhaustion) + ';'
    text += str(player.change_hunger) + ';'
    text += str(player.change_water) + ';'
    text += str(player.change_poison) + ';'
    text += str(player.change_radiation) + ';'
    text += str(player.change_energy) + ';'
    text += str(player.change_bleeding) + ';'
    text += str(player.change_temperature) + ';'

    text += str(int(game_time.num_time)) + '</>\n'
    text += inventory.get_text_for_saving()

    description_player.write(text)
    description_player.close()

    description_map = open('map/description_map.txt', 'w')
    text = ''
    for i in range(BOARD_MAP.height):
        for j in range(BOARD_MAP.width):
            description_call = BOARD_MAP.board[i][j].get_text_for_save()
            text = text + description_call
    description_map.write(text)
    description_map.close()


def start(*args):  # запуск игры
    global type_window, inventory, location, BOARD_MAP, tasks, selected_task, tasks_connect

    objects_main.off_all()
    main_map.visibility = True
    player.set_parametrs(open_file())

    inventory = Inventory(screen, None, player)
    inventory.bg_image = get_bg_for_inventory((width, ps_height(83.2)))

    tasks = Tasks(screen, None)
    tasks.bg_image = get_bg_for_tasks((width, ps_height(83.2)))
    selected_task = 0
    tasks_connect = sqlite3.connect("data/tasks_base.db")
    # открывает и загружает сохранения
    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    location = Inventory(screen, None, player, mod=2)
    location.bg_image = get_bg_for_inventory((width, ps_height(83.2)))

    inventory.initialization(open_file(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)
    location.initialization(call.get_text_for_save(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)

    update_map()
    update_image_map()

    type_window = 'main'


def show_and_change_all_options():  # обновляет все пораметры игрока
    texts_of_options_player[0].change_text(int(player.exhaustion))
    texts_of_options_player[1].change_text(int(player.hunger))
    texts_of_options_player[2].change_text(int(player.water))
    texts_of_options_player[3].change_text(int(player.poison))
    texts_of_options_player[4].change_text(int(player.radiation))
    texts_of_options_player[5].change_text(int(player.energy))
    texts_of_options_player[6].change_text(inventory.get_ps_of_load())
    texts_of_options_player[7].change_text(int(player.bleeding))
    texts_of_options_player[8].change_text(player.temperature)

    for text in texts_of_options_player:
        text.show()  # отображение всех пораметров игрока


def opening_inventory(*args):  # функция одной из кнопок навигации
    # меняет тип окна на инвентарь и закрывает всё лишнее
    global type_window
    inventory.visibility = True
    location.visibility = False
    inventory.hide_all_function()
    location.hide_all_function()

    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    if 'NONE' not in call.lies:
        location.update_thinks(
            location.convert_thinks_to_object(call.lies.split(';'), ':', ps_width(8.9), call=call))
    else:
        location.update_thinks(location.convert_thinks_to_object([], call=call))

    player.stop()
    type_window = 'inventory'


def opening_tasks(*args):  # функция одной из кнопок навигации
    # меняет тип окна на задания и закрывает всё лишнее
    global type_window
    tasks.visibility = True
    location.visibility = False
    player.stop()
    type_window = 'tasks'


def change_num_task(*args):  # определяет описание какой задачи нужно вывести
    global selected_task
    last_selected_task = selected_task
    con = sqlite3.connect("data/tasks_base.db")
    cur = con.cursor()
    result = cur.execute("SELECT id from tasks WHERE progress IN(1) AND type_id IN(1)").fetchall()
    x, y = pygame.mouse.get_pos()
    num = ((y - ps_height(10.5)) // ps_height(6.3))
    if num < len(result):
        selected_task = result[num][0]
    else:
        selected_task = last_selected_task


def show_info_from_task(selected_task):  # выводит описание выбранной задачи
    if selected_task != 0:
        con = sqlite3.connect("data/tasks_base.db")
        cur = con.cursor()
        actual_tasks = cur.execute("SELECT text, name from tasks WHERE id IN(?)", (selected_task,)).fetchone()
        name_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 48)
        text_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 24)
        name = Text(screen, ps_width(30.5), ps_height(11.2), actual_tasks[1], name_font, color=BLACK)
        text = Text(screen, ps_width(30.5), ps_height(22.4), actual_tasks[0], text_font, color=BLACK)
        name.show()
        text.show()


def check_tasks(x, y):  # Проверяет выполнение задач и начинает новые
    global tasks_connect, selected_task
    tasks_cursor = tasks_connect.cursor()
    start_tasks_coords = tasks_cursor.execute(
        "Select start_x, start_y, id from tasks where progress IN(0)").fetchall()
    end_tasks_coords = tasks_cursor.execute("Select end_x, end_y, id from tasks where progress IN(1)").fetchall()
    # print(round(int(x), -1), round(int(y), -1))
    for elem in end_tasks_coords:
        if (round(int(x), -1), round(int(y), -1)) == (round(elem[0], -1), round(elem[1], -1)):
            tasks_cursor.execute("UPDATE tasks SET progress = 2 WHERE id IN(?) AND progress IN(1)", (elem[2],))
            tasks_connect.commit()
            selected_task = 0
            opening_tasks()
    for elem in start_tasks_coords:
        if (round(int(x), -1), round(int(y), -1)) == (round(elem[0], -1), round(elem[1], -1)):
            tasks_cursor.execute("UPDATE tasks SET progress = 1 WHERE id IN(?) AND progress IN(0)", (elem[2],))
            tasks_connect.commit()
            selected_task = elem[2]
            opening_tasks()


def change_inventory_type_to_location(*args):  # одна из кнопок навигации
    # открывает описание локации и закрывает всё лишнее
    global type_window
    player.stop()
    type_window = 'inventory'
    inventory.visibility = False
    inventory.hide_all_function()

    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    location.update_cane_find(call)
    if 'NONE' not in call.lies:
        location.update_thinks(location.convert_thinks_to_object(call.lies.split(';'), ':', ps_width(8.9), call=call))
    else:
        location.update_thinks(location.convert_thinks_to_object([], call=call))
    location.visibility = True
    location.hide_all_function()


def opening_statistics(*args):  # одна из кнопок навигации
    # открывает статистику и закрывает всё лишнее
    global type_window
    player.stop()
    type_window = 'statistics'


def opening_main_window(*args):  # одна из кнопок навигации
    # открывает главное меню старта
    global type_window
    player.stop()
    save()
    objects_main.on_all()
    main_map.visibility = False
    type_window = 'main_window'


def open_map(*args):  # одна из кнопок навигации
    # открывает основное окно
    global type_window
    inventory.visibility = False
    tasks.visibility = False
    type_window = 'main'


def update_map():  # сдвинуть отображаемую облость карты
    global image_map, zoom_images, map_x_on_main_map, map_y_on_main_map

    last_map_x, last_map_y = map_x_on_main_map, map_y_on_main_map

    if player.x > width_map / 2:
        if player.x > 3906 - width_map / 2:
            map_x_on_main_map = 3906 - width_map
        else:
            map_x_on_main_map = player.x - width_map // 2
    else:
        map_x_on_main_map = 0

    if player.y > height_map / 2:
        if player.y > 2047 - height_map / 2:
            map_y_on_main_map = 2047 - height_map
        else:
            map_y_on_main_map = player.y - height_map // 2
    else:
        map_y_on_main_map = 0

    if last_map_x == map_x_on_main_map and last_map_y == map_y_on_main_map:
        return

    image_map = cat_image(main_image_map,
                          (map_x_on_main_map, map_y_on_main_map,
                           3906 - width_map - map_x_on_main_map,
                           2047 - height_map - map_y_on_main_map))
    zoom_images = [None for i in range(6)]
    update_image_map()


def update_image_map():  # меняет зум карты и сохраняет его
    global zoom_images
    if zoom_images[zoom] is not None:
        image = zoom_images[zoom][0]
    else:
        new_zoom = 2
        for i in range(zoom):
            new_zoom *= zoom_plus
        image = resize_image(image_map,
                             (int(width_map * new_zoom), int(height_map * new_zoom)))
        image = get_pygame_image(image)

        zoom_images[zoom] = (image, size_cell * new_zoom, new_zoom)
    BOARD_MAP.image_mark = get_mark_for_map((int(zoom_images[zoom][1]), int(zoom_images[zoom][1])))
    main_map.change_image(image)


def create_all_objects():  # определяет все объекты
    global main_map, BOARD_MAP, parametrs, tool_bar_map, zoom_images, player
    global texts_of_options_player, btn_searching

    image = get_bg_main_window(size)
    bg_main_window = Object(screen, image, 0, 0, *size)

    image = get_free_image('images/btn_exit_main_2.png', (ps_height(37), ps_height(5)))
    image_2 = get_free_image('images/btn_exit_main_click_2.png', (ps_height(37), ps_height(5)))
    btn_exit_main = Button(screen, image, ps_width(68), ps_height(55), ps_height(37), ps_height(5), exit, image_2)

    image = get_free_image('images/btn_start_main_2.png', (ps_height(37), ps_height(5)))
    image_2 = get_free_image('images/btn_start_main_click_2.png', (ps_height(37), ps_height(5)))
    btn_continue_game_main = Button(screen, image, ps_width(68), ps_height(37),
                           ps_height(37), ps_height(5), continue_game, image_2)

    image = get_free_image('images/btn_new_start_main_2.png', (ps_height(37), ps_height(5)))
    image_2 = get_free_image('images/btn_new_start_main_click_2.png', (ps_height(37), ps_height(5)))
    btn_start_new_main = Button(screen, image, ps_width(68), ps_height(28),
                            ps_height(37), ps_height(5), start_new_game, image_2)

    image = get_pygame_image(image_map)
    main_map = Object(screen, image, map_x, map_y, 3906 * zoom, 2047 * zoom)
    main_map.visibility = False

    objects_main.add_objects(bg_main_window, btn_exit_main,
                             btn_continue_game_main, btn_start_new_main)

    main_objects_bar = Object(screen, get_image_main_objectsbar(
        (width, ps_height(5.6))), 0, 0, width, ps_height(5.6))
    main_btn_bar = Object(screen, get_image_main_btnbar(
        (width, ps_height(11.2))), 0, ps_height(88.8), width, ps_height(11.2))

    objects_map.add_objects(main_btn_bar, main_objects_bar)

    image = get_image_btn_for_main_map_window_1((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, 0, ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_main_window)
    objects_map.add_objects(btn)

    image = get_image_btn_for_main_map_window_2((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(14.2), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_tasks)
    objects_map.add_objects(btn)

    image = get_image_btn_for_main_map_window_3((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(28.6), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_statistics)
    objects_map.add_objects(btn)

    image = get_image_btn_for_main_map_window_6((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(85.8), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(open_map)
    objects_map.add_objects(btn)

    image = get_image_btn_for_main_map_window_5((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(71.6), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(change_inventory_type_to_location)
    objects_map.add_objects(btn)

    image = get_image_btn_for_main_map_window_4((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(57.4), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_inventory)
    objects_map.add_objects(btn)

    btn_tasks_x = ps_width(2.5)
    btn_tasks_y = ps_height(10.7)
    btn_tasks_width = ps_width(26.1)
    btn_tasks_height = ps_height(6.3)
    for i in range(11):
        image = get_tasks_image((btn_tasks_width, btn_tasks_height))
        btn = Button(screen, image, btn_tasks_x, btn_tasks_y, btn_tasks_width, btn_tasks_height)
        btn.add_function(change_num_task)
        objects_tasks.add_objects(btn)
        btn_tasks_y += ps_height(6.3)

    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    zoom_images = [None for i in range(6)]

    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    inventory.initialization(open_file(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)
    location.initialization(call.get_text_for_save(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)

    texts_of_options_player = []
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_width(1.7))

    text = Text(screen, ps_width(10), 15, player.exhaustion, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(19.5), 15, player.hunger, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(29), 15, player.water, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(39), 15, player.poison, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(49), 15, player.radiation, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(58), 15, player.energy, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(68), 15, inventory.get_ps_of_load(), font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(78.3), 15, player.bleeding, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(87.7), 15, player.temperature, font)
    texts_of_options_player.append(text)

    image = get_image_btn_inventory_on_location((ps_width(7.5), ps_height(17.9)))
    btn = Button(screen, image, ps_width(0.7), ps_height(8), ps_width(7.5), ps_height(17.9))
    btn.add_function(opening_inventory)
    objects_inventory.add_objects(btn)

    image = get_free_image('images/btn_location_on_location.png', (ps_width(7.5), ps_height(17.9)))
    btn = Button(screen, image, ps_width(40), ps_height(8), ps_width(7.5), ps_height(17.9))
    btn.add_function(change_inventory_type_to_location)
    objects_inventory.add_objects(btn)

    image = get_image_btn_search((ps_width(14), ps_height(5)))
    btn_searching = Button(screen, image, ps_width(68), ps_height(78), ps_width(14), ps_height(5))
    btn_searching.add_function(searching_on_call)

    image = get_free_image('images/bg_for_tasks.png', (width, ps_height(83.2)))
    object = Object(screen, image, 0, ps_height(5.6), width, height)
    objects_statistics.add_objects(object)


FPS = 100
ratio = 3 / 5  # отношение сторон окна приложения
zoom = 2
zoom_plus = 1.2
timer_between_clicks = 0
size_cell = 10
old_mouse_x, old_mouse_y = 0, 0
map_x, map_y = 0, 0
BOARD_MAP = None

player_x, player_y = 0, 0
width_map, height_map = 900, 900

if player_x > width_map / 2:
    map_x_on_main_map = player_x - width_map // 2
else:
    map_x_on_main_map = 0
if player_y > height_map / 2:
    map_y_on_main_map = player_y - height_map // 2
else:
    map_y_on_main_map = 0

main_map = None

main_image_map = get_map((3906, 2047), 1)
image_map = cat_image(main_image_map, (map_x_on_main_map, map_y_on_main_map,
                      3906 - width_map - map_x_on_main_map,
                      2047 - height_map - map_y_on_main_map))

objects_main = Group()  # создания груп для всех разделов
objects_map = Group()
objects_inventory = Group()
objects_tasks = Group()
objects_statistics = Group()

type_window = 'main_window'  # опредиление типа окна

pygame.init()

display = pygame.display.Info()  # установка окна прриложения в нужном месте под
# любой физический размер экрана
width, height = display.current_w - 75, display.current_h - 75
if width * ratio <= height:
    height = int(width * ratio)
else:
    width = int(height / ratio)
size = width, height
print(size)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)
install_size(size)  # инсталяция итоговых размеров окна для дальнейшей работы

game_time = GameTime(0, screen)  # установка игрового времени
player = Player(screen, player_x, player_y, game_time)  # создание игрока
player.deathing = the_end
inventory = Inventory(screen, None, player)
location = Inventory(screen, None, player)

create_all_objects()
update_image_map()

running = True
moving_map = False
clock = pygame.time.Clock()
x, y = 0, 0

while running:
    clock.tick(FPS)  # поддержка фпс
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            save()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if type_window == 'main_window':  # проверка нажатия всех необходимых типов окна
                objects_main.check(event)
            if type_window != 'main_window':
                objects_map.check(event)
            if type_window == 'inventory':
                objects_inventory.check(event)
                inventory.check(event)
                location.check(event)
                if location.visibility and btn_searching.check_tip(x, y):
                    btn_searching.status = True
            if type_window == 'tasks':
                objects_tasks.check(event)

            if type_window == 'main':
                if event.button == 1:
                    moving_map = True
                    old_mouse_x, old_mouse_y = x, y

                if event.button == 5:  # скрол вниз
                    zoom -= 1
                    if zoom < 0:
                        zoom = 0
                    else:
                        update_image_map()

                if event.button == 4:  # скрол вверх
                    zoom += 1
                    if zoom > len(zoom_images) - 1:
                        zoom = len(zoom_images) - 1
                    else:
                        update_image_map()
                if event.button == 1:  # левое нажатие мыши
                    if time.time() - timer_between_clicks < 0.3:  # проверка на двойное нажатие
                        new_x = ((x - map_x) / zoom_images[zoom][2]) + map_x_on_main_map
                        new_y = ((y - map_y) / zoom_images[zoom][2]) + map_y_on_main_map
                        player.move_to(new_x, new_y)

                    timer_between_clicks = time.time()

            if type_window == 'inventory':
                if event.button == 5:  # скрол вниз
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.pag(inventory.window.shift_y - 50)
                if event.button == 5:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.pag(location.window.shift_y - 50)

                if event.button == 4:  # скрол вниз
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.pag(inventory.window.shift_y + 50)
                if event.button == 4:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.pag(location.window.shift_y + 50)

                if event.button == 1:  # левое нажатие мыши
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.paging = True
                if event.button == 1:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.paging = True

            if type_window == 'tasks':
                pass

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos  # проверка отпускания клавиш всех необходимых типов окна
            if type_window == 'main_window':
                objects_main.check(event)
            if type_window != 'main_window':
                objects_map.check(event)
            if type_window == 'inventory':
                objects_inventory.check(event)
                inventory.check(event)
                location.check(event)
                if location.visibility and btn_searching.check_tip(x, y):
                    btn_searching.click()
                    btn_searching.status = False
            if type_window == 'tasks':
                objects_tasks.check(event)

            inventory.window.paging = False
            location.window.paging = False
            moving_map = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos  # проверка движения всех необходимых типов окна
            shift_x = old_mouse_x - x
            shift_y = old_mouse_y - y
            old_mouse_x, old_mouse_y = x, y

            if moving_map:  # сдвиг игровой карты
                map_x = map_x - shift_x
                map_y = map_y - shift_y
                if map_x > 0:
                    map_x = 0
                if map_y > 0:
                    map_y = 0
                image_size = main_map.image.get_size()
                if map_x < -image_size[0] + width:
                    map_x = -image_size[0] + width
                if map_y < -image_size[1] + height:
                    map_y = -image_size[1] + height

                main_map.move_to(map_x, map_y)
            if type_window == 'inventory':
                inventory.check(event)
                location.check(event)

            if inventory.window.paging:
                inventory.window.pag(inventory.window.shift_y - shift_y)
            if location.window.paging:
                location.window.pag(location.window.shift_y - shift_y)

    if type_window == 'main_window':
        objects_main.show()

    if type_window == 'main':
        main_map.show()
        BOARD_MAP.show_all_marks(zoom_images[zoom][1], map_x - (map_x_on_main_map * zoom_images[zoom][2]),
                                 map_y - (map_y_on_main_map * zoom_images[zoom][2]))
        player.show(map_x_on_main_map, map_y_on_main_map, map_x, map_y, zoom_images[zoom][2])

        if player.moving:  # сдвигает игрока на расчитаные по времени координаты
            player.made_step()
            call = BOARD_MAP.get_call_in_bord((player.x, player.y))
            check_tasks(player.x, player.y)
            if call is not None:
                player.speed = player.start_speed * float(call.speed)
                player.check_condition(call)

                if not player.moving:
                    # выполняется если игрок остановился после
                    # своего последнего шага
                    player_x_on_map = player.x - map_x_on_main_map
                    player_y_on_map = player.y - map_y_on_main_map
                    if (player_x_on_map < 50 or player_y_on_map < 50 or
                            player_x_on_map > width_map - 150 or player_y_on_map > height_map - 150):
                        update_map()
                    location.update_call(call)
                    inventory.update_call(call)

    if type_window == 'inventory':  # отображение необходимого типа окна
        inventory.show()
        location.show()
        objects_inventory.show()
        if location.visibility:
            btn_searching.show()

    if type_window == 'tasks':
        global selected_task
        tasks.show()
        tasks.show_all_tasks()
        objects_tasks.show()
        show_info_from_task(selected_task)

    if type_window == 'statistics':
        objects_statistics.show()

    if type_window != 'main_window':
        objects_map.show()

        show_and_change_all_options()
        game_time.show()
        game_time.update_time_on_real_time()

    pygame.display.flip()  # обновление экрана

pygame.quit()

