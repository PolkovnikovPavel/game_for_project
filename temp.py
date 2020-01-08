import pygame
import os, random
from System import *
from images.images import *


def exit(*args):
    global running
    running = False


def the_end():
    start_new_game()
    opening_main_window()


def start_new_game(*args):
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
    show_starting_slides(3, "bmp")
    start()

def show_starting_slides(number, format):
    count = 2
    image = get_free_image("images\start_slides\start_slide_1." + format, (width, height))
    start_slide = Object(screen, image, 0, 0, width, height)
    start_slide.show()
    pygame.display.flip()
    while count <= number + 1:
        for event in pygame.event.get():
            if 1 in pygame.key.get_pressed() or event.type == pygame.MOUSEBUTTONDOWN:
                if count <= number:
                    slide_name = "images\start_slides\start_slide_" + str(count) + "." + format
                    image = get_free_image(slide_name, (width, height))
                    start_slide = Object(screen, image, 0, 0, width, height)
                    start_slide.show()
                count += 1
            pygame.display.flip()

def continue_game(*args):
    if os.path.exists('map/description_map.txt'):
        start()
    else:
        start_new_game()


def searching_on_call(*args):
    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    was = call.lies
    call.find_things()
    location.update_thinks(location.convert_thinks_to_object(call.lies.split(';'), ':', ps_width(8.9), call=call))
    t = random.choice(range(3, 23))
    game_time.skip_time(t / 10, player)
    location.update_cane_find(call)
    if call.lies != 'NONE' and was == 'NONE':
        BOARD_MAP.board_with_marks.append(call)

def save():
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


def start(*args):
    global type_window, inventory, location, BOARD_MAP, tasks, selected_task

    objects_main.off_all()
    main_map.visibility = True
    player.set_parametrs(open_file())

    inventory = Inventory(screen, None, player)
    inventory.bg_image = get_bg_for_inventory((width, ps_height(83.2)))

    tasks = Tasks(screen, None)
    tasks.bg_image = get_bg_for_tasks((width, ps_height(83.2)))
    selected_task = 1

    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
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

def show_and_change_all_options():
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
        text.show()


def opening_inventory(*args):
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


def opening_tasks(*args):
    global type_window
    tasks.visibility = True
    location.visibility = False
    player.stop()
    type_window = 'tasks'


def change_num_task(*args):
    global selected_task
    x, y = pygame.mouse.get_pos()
    selected_task = ((y - 75) // 45) + 1


def show_info_from_task(num):
    con = sqlite3.connect("data/tasks_base.db")
    cur = con.cursor()
    actual_tasks = cur.execute("SELECT text, name from tasks WHERE id IN(?)", (num,)).fetchone()
    name_font = pygame.font.SysFont('arial', 48)
    text_font = pygame.font.SysFont('arial', 24)
    name = Text(screen, 350, 80, actual_tasks[1], name_font, color=BLACK)
    text = Text(screen, 350, 160, actual_tasks[0], text_font, color=BLACK)
    name.show()
    text.show()


def change_inventory_type_to_location(*args):
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

def opening_quests(*args):
    global type_window
    player.stop()
    type_window = 'quests'


def opening_statistics(*args):
    global type_window
    player.stop()
    type_window = 'statistics'


def opening_main_window(*args):
    global type_window
    player.stop()
    save()
    objects_main.on_all()
    main_map.visibility = False
    type_window = 'main_window'


def open_map(*args):
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


def update_image_map():
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


def create_all_objects():
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

    cur = sqlite3.connect("data/tasks_base.db").cursor()
    n = cur.execute("SELECT COUNT(id) FROM tasks").fetchone()
    btn_tasks_x = 28
    btn_tasks_y = 74
    btn_tasks_width = 302
    btn_tasks_height = 45
    for i in range(1, n[0] + 1):
        image = get_tasks_image((btn_tasks_width, btn_tasks_height))
        btn = Button(screen, image, btn_tasks_x, btn_tasks_y, btn_tasks_width, btn_tasks_height)
        btn.add_function(change_num_task)
        objects_tasks.add_objects(btn)
        btn_tasks_y += 45

    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    zoom_images = [None for i in range(6)]

    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    inventory.initialization(open_file(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)
    location.initialization(call.get_text_for_save(), inventory, location, call=call, BOARD_MAP=BOARD_MAP)

    texts_of_options_player = []
    font = pygame.font.Font(None, ps_width(2.5))

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

    image = get_free_image('images/bg_for_tasks.png', (width, height))
    object = Object(screen, image, 0, 0, width, height)
    objects_statistics.add_objects(object)

FPS = 100
ratio = 3 / 5
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

objects_main = Group()
objects_map = Group()
objects_inventory = Group()
objects_tasks = Group()
objects_statistics = Group()

type_window = 'main_window'

pygame.init()

display = pygame.display.Info()
width, height = display.current_w - 75, display.current_h - 75
if width * ratio <= height:
    height = int(width * ratio)
else:
    width = int(height / ratio)
size = width, height
print(size)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)
install_size(size)

game_time = GameTime(0, screen)
player = Player(screen, player_x, player_y, game_time)
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
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            save()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if type_window == 'main_window':
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
                    if time.time() - timer_between_clicks < 0.3:
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
            x, y = event.pos
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
            x, y = event.pos
            shift_x = old_mouse_x - x
            shift_y = old_mouse_y - y
            old_mouse_x, old_mouse_y = x, y

            if moving_map:
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

    if type_window == 'statistics':
        objects_statistics.show()

    if type_window == 'inventory':
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

    if type_window != 'main_window':
        objects_map.show()

        show_and_change_all_options()
        game_time.show()
        game_time.update_time_on_real_time()

    pygame.display.flip()

pygame.quit()
