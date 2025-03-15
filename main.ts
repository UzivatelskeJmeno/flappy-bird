input.onButtonPressed(Button.A, function () {
	
})
function IsInRange (number: number, min2: number, max2: number) {
    if (Math.constrain(number, min2, max2) == number) {
        isInRange = 1
    } else {
        isInRange = 0
    }
}
input.onButtonPressed(Button.B, function () {
    vyska_postava += 1
})
let sloupy_kolize: number[] = []
let VyskaMezery = 0
let čas = 0
let Char = ""
let stavA = 0
let isInRange = 0
let hrac = [
"{B10000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B01000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00100000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00010000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00001000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00000100, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00000010, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B00000001, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}"
]
let sloup = [
"{B00011111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B10001111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B11000111, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B11100011, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{B11110001, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}",
"{111111000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}"
]
let zaSloupcuSloup = randint(4, 6)
max7219_matrix.setup(
4,
DigitalPin.P16,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.for_4_in_1_modules(
rotation_direction.clockwise,
false
)
let vyska_postava = 8
max7219_matrix.displayCustomCharacter(
max7219_matrix.getCustomCharacterArray(
hrac[vyska_postava]
),
0,
true
)
basic.forever(function () {
    stavA = 0
    Char = "B10000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000"
    čas = input.runningTime()
    while (true) {
        if (500 < input.runningTime() - čas) {
            break;
        } else if (input.buttonIsPressed(Button.A)) {
            stavA = 1
        } else {
        	
        }
    }
    if (stavA == 1) {
        vyska_postava += 2
        if (vyska_postava > 7) {
            vyska_postava = 7
        }
    }
    vyska_postava += -1
    if (vyska_postava < 0) {
        vyska_postava = 0
    }
    max7219_matrix.displayCustomCharacter(
    max7219_matrix.getCustomCharacterArray(
    hrac[vyska_postava]
    ),
    0,
    true
    )
    max7219_matrix.displayCustomCharacter(
    max7219_matrix.getCustomCharacterArray(
    sloup[VyskaMezery]
    ),
    zaSloupcuSloup,
    false
    )
    zaSloupcuSloup += -1
    if (zaSloupcuSloup < 0) {
        zaSloupcuSloup = randint(4, 6)
        VyskaMezery = randint(0, 5)
    }
    sloupy_kolize = [
    0,
    1,
    0,
    0,
    0,
    0
    ]
})
