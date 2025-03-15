def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def IsInRange(number: number, min2: number, max2: number):
    global isInRange
    if Math.constrain(number, min2, max2) == number:
        isInRange = 1
    else:
        isInRange = 0

def on_button_pressed_b():
    global vyska_postava
    vyska_postava += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

sloupy_kolize: List[number] = []
VyskaMezery = 0
čas = 0
Char = ""
stavA = 0
isInRange = 0
hrac = ["{B10000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B01000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00100000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00010000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00001000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00000100, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00000010, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B00000001, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}"]
sloup = ["{B00011111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B10001111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B11000111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B11100011, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{B11110001, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
    "{111111000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}"]
zaSloupcuSloup = randint(4, 6)
max7219_matrix.setup(4,
    DigitalPin.P16,
    DigitalPin.P15,
    DigitalPin.P14,
    DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.CLOCKWISE, False)
vyska_postava = 8
max7219_matrix.display_custom_character(max7219_matrix.get_custom_character_array(hrac[vyska_postava]),
    0,
    True)

def on_forever():
    global stavA, Char, čas, vyska_postava, zaSloupcuSloup, VyskaMezery, sloupy_kolize
    stavA = 0
    Char = "B10000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000"
    čas = input.running_time()
    while True:
        if 500 < input.running_time() - čas:
            break
        elif input.button_is_pressed(Button.A):
            stavA = 1
        else:
            pass
    if stavA == 1:
        vyska_postava += 2
        if vyska_postava > 7:
            vyska_postava = 7
    vyska_postava += -1
    if vyska_postava < 0:
        vyska_postava = 0
    max7219_matrix.display_custom_character(max7219_matrix.get_custom_character_array(hrac[vyska_postava]),
        0,
        True)
    max7219_matrix.display_custom_character(max7219_matrix.get_custom_character_array(sloup[VyskaMezery]),
        zaSloupcuSloup,
        False)
    zaSloupcuSloup += -1
    if zaSloupcuSloup < 0:
        zaSloupcuSloup = randint(4, 6)
        VyskaMezery = randint(0, 5)
    sloupy_kolize = [0, 1, 0, 0, 0, 0]
basic.forever(on_forever)

