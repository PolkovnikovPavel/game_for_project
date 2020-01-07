
import sqlite3, time, copy
from images.images import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
LIGHT_GREEN = (27, 65, 16)
BROWN = (74, 47, 4)
width, height = 0, 0


def install_size(size):
    global width, height
    width, height = size


def open_file():
    with open('data/SaveGame.txt', 'r') as f:
        read_data = f.read()
    return read_data


def change_parametrs(id):
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
                    2:75:0;3:15:0;70:10:0
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
    elif id[0] ==25:
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
            3:90:0;1:15;0
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


def ps_height(percent):
    percent = percent / 100
    return int(height * percent)


def ps_width(percent):
    percent = percent / 100
    return int(width * percent)


class Object:
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

    def check_tip(self, x, y):
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self):
        if self.visibility:
            self.canvas.blit(self.image, (self.x, self.y))


class Text(Object):
    def __init__(self, canvas, x, y, text, font):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = str(text)
        self.font = font
        self.color = WHITE
        self.visibility = True
        self.height = len(str(self.text).split('\n')) * ps_height(2)

    def change_text(self, new_text):
        self.text = str(new_text)

    def show(self):
        if not self.visibility:
            return
        texts = str(self.text).split('\n')
        for i in range(len(texts)):
            text = self.font.render(texts[i], 1, self.color)
            self.canvas.blit(text, (self.x, int(self.y + i * ps_height(2))))


class Button(Object):
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

    def add_function(self, function):
        if self.function == [None]:
            self.function = [function]
        else:
            self.function.append(function)

    def get_function(self, function):
        self.function = [function]

    def del_function(self):
        self.function = [None]

    def get_image_animation(self, image):
        self.image_animation = image

    def show_animation(self):
        if self.image_animation is not None:
            self.canvas.blit(self.image_animation, (self.x, self.y))
        else:
            self.canvas.blit(self.image, (self.x, self.y))

    def click(self, *args):
        if self.function == [None] or not self.visibility:
            return False
        for function in self.function:
            try:
                return function(args)
            except:
                print('не удалось запустить функцию')
                return False

    def show(self):
        if self.visibility:
            if self.status:
                self.show_animation()
                return
            self.canvas.blit(self.image, (self.x, self.y))


class Call:
    def __init__(self, canvas, x, y, size, color=BLACK, parametrs=None):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.visibility = True

        if parametrs is None:
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

    def find_things(self):
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

        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (self.width // self.column_count) + self.x
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
        if self.mod:   # следующие действия делают так,
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
    def __init__(self, canvas,  x, y, game_time):
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

        self.elementary_speed = 100
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
            self.game_time.skip_time(7, self)   # делать так чтоб игрок сразу ложился спать
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
        self.radiation += self.change_radiation * delte_t
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
        text = f'{self.name}\nВес: {self.heft * self.count}г.\n...\n...'
        self.functions.objects[0].text = text

    def update_function(self):
        self.functions.delete_all_objects()

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
        font = pygame.font.Font(None, ps_width(1.8))
        text = Text(self.canvas, 0, 0, text, font)
        text.color = BLACK
        self.functions.add_object(text)


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
                                    self.y + self.height - ps_height(4)))


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

        #image = get_bg_for_thinks_in_inventory((w, h))
        self.window = Window(self.canvas, None, x, y, w, h, 5)
        self.window.visibility = True
        self.window.width_object = ps_width(8.9)
        for think in self.showing_thinks:
            self.window.add_object(think)

    def convert_thinks_to_object(self, all_thinks, sep=';', w=50, inventory=None,
                                 location=None, call=None):
        if any(map(lambda x: x is None, (inventory, location))):
            inventory = self.inventory   # если хотя бы один равен None
            location = self.location
            if any(map(lambda x: x is None, (inventory, location))):
                return   # если хотя бы один равен None
        ready_thinks = []
        font = pygame.font.Font(None, int(w // 2.7))
        self.heft = 0
        for think in all_thinks:
            if 'NONE' not in think:
                id, count, strength = think.split(sep)
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
            w = ps_width(8.9)
            font = pygame.font.Font(None, int(w // 2.7))

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
        ps =  int(100 * self.heft / self.player.max_heft)
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

        font = pygame.font.Font(None, ps_width(2.3))
        self.title_text = Text(self.canvas, self.x + ps_height(0.5),
                               self.y + ps_height(0.5), '', font)

        font = pygame.font.Font(None, ps_width(1.8))
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
        self.font = pygame.font.Font(None, ps_width(2))

    def start_thinktime(self):
        self.timer = time.time()

    def update_time(self):
        self.time = time.localtime(self.num_time)

    def skip_time(self, expectation, player):
        self.expectation_timer = time.time()
        t_game = 0
        while expectation >= 0:
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

