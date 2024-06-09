import time
import board
import busio
import digitalio
from adafruit_ov7670 import OV7670, OV7670_SIZE_DIV16

# Configuración de la cámara OV7670
cam_bus = busio.I2C(board.GP21, board.GP20)
cam = OV7670(
    cam_bus,
    data_pins=[
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    ],
    clock=board.GP8,
    vsync=board.GP13,
    href=board.GP12,
    mclk=board.GP9,
    shutdown=board.GP15,
    reset=board.GP14,
)
cam.size = OV7670_SIZE_DIV16
cam.colorspace = 1

# Ajusta el tamaño de la imagen para que se ajuste a la consola
console_width = 80
console_height = 30

# Captura y muestra la imagen en la consola
buf = bytearray(2 * cam.width * cam.height)
while True:
    cam.capture(buf)

    # Convierte la imagen a caracteres ASCII y muestra en la consola
    for j in range(console_height):
        row = ""
        for i in range(console_width):
            pixel_index = int((i / console_width) * cam.width) + int((j / console_height) * cam.height) * cam.width
            pixel_color = buf[2 * pixel_index] << 8 | buf[2 * pixel_index + 1]
            row += " .:-=+*#%@ "[pixel_color // 256 // 32]
        print(row)

    time.sleep(0.1)  # Espera antes de capturar la siguiente imagen
