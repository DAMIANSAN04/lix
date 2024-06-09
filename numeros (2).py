import time
import board
import busio
import adafruit_ssd1306

# Configuración del bus I2C y del dispositivo SSD1306
SCL = board.GP17
SDA = board.GP16
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Lista de dibujos que quieres mostrar en el dispositivo
drawings = [
    [
        "        ****                                *                               ****             ",
        "      **    **                              *                             **    **           ",
        "     **      **                             *                            **      **          ",
        "    **        **                            *                           **        **         ",
        "   **          **                           *                          **          **        ",
        "  **            **                          *                         **            **       ",
        "  **            **                          *                         **            **       ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        " **              **                         *                        **              **      ",
        "  **            **                          *                         **            **       ",
        "  **            **                          *                         **            **       ",
        "   **          **                           *                          **          **        ",
        "    **        **                            *                           **        **         ",
        "     **      **                             *                            **      **          ",
        "      **    **                              *                             **    **           ",
        "        ****                                *                               ****             ",
    ],

    # Puedes agregar más dibujos aquí...
        [
        "         **                                 *                                **              ",
        "        ***                                 *                               ***              ",
        "       ****                                 *                              ****              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "         **                                 *                                **              ",
        "        ****                                *                               ****             ",
        "        ****                                *                               ****             ",
        "        ****                                *                               ****             ",
        "        ****                                *                                                ",
        "        ****                                *                               ****             ",
        "        ****                                *                               ****             ",
        "        ****                                *                               ****             ",
    ],
        [
        "      ******                                *                              *****             ",
        "    **********                              *                           **********           ",
        "   **        ***                            *                          **        ***         ",
        "               **                           *                                      **        ",
        "                **                          *                                       **       ",
        "                **                          *                                       **       ",
        "                **                          *                                      **        ",
        "               **                           *                                     **         ",
        "              **                            *                                    **          ",
        "             **                             *                                   **           ",
        "            **                              *                                  **            ",
        "           **                               *                                 **             ",
        "          **                                *                                **              ",
        "         **                                 *                               **               ",
        "        **                                  *                             **                 ",
        "       **                                   *                           **                   ",
        "      **                                    *                         **                     ",
        "     **                                     *                       **                       ",
        "    **                                      *                     **                         ",
        "   **                                       *                    **                          ",
        "  **                                        *                  **                            ",
        " **                                         *                 **                             ",
        " **                                         *                 **                             ",
        " **                                         *                 **                             ",
        " **                                         *                 **                             ",
        " **                                         *                 **                             ",
        " **                                         *                 **                             ",
        "  **                                        *                  **                            ",
        "   **                                       *                   **                           ",
        "    ***                                     *                    **                          ",
        "     *****************************          *                     ***************************",
        "       ****************************         *                        ************************",
        "                                            *                                                ",
    ],
 [
        "      ******************                    *          ******************                    ",
        "    **********************                  *        **********************                  ",
        "   ***                  ***                 *       ***                  ***                 ",
        "   ***                   ***                *       ***                   ***                ",
        "    ***                  ***                *        ***                  ***                ",
        "     ***                ***                 *         ***                ***                 ",
        "                       ***                  *                           ***                  ",
        "                      ***                   *                          ***                   ",
        "                    ***                     *                         ***                    ",
        "                  ***                       *                        ***                     ",
        "                ***                         *                       ***                      ",
        "              ***                           *                      ***                 ",
        "             ***                            *                       ***                 ",
        "               ***                          *                         ***               ",
        "                  ***                       *                           ***                 ",
        "                     ***                    *                            ***                   ",
        "                       ***                  *                             ***                     ",
        "                         ***                *                              ***                       ",
        "                           ***              *                               ***                         ",
        "                            ***             *                               ***                          ",
        "                            ***             *                               ***                            ",
        "                            ***             *                               ***                             ",
        "                            ***             *                               ***                             ",
        "     ***                    ***             *       ***                    ***                            ",
        "     ***                   ***              *       ***                   ***                             ",
        "      ***                 ***               *        ***                 ***                               ",
        "       ***              ***                 *         ***              ***                     ",
        "         **************                     *            **************                            ",
        "          ************                      *             ************                        ",
        "           ********                         *              ********                           ",
        "                                            *                                                 ",
        "                                            *                                                  ",
        "                                            *                                                ",
    ],
            [
        "                      **                    *                                **              ",
        "                     ***                    *                               ***              ",
        "                   *****                    *                             *****              ",
        "                 ***  **                    *                           ***  **              ",
        "                ***   **                    *                          ***   **              ",
        "              ***     **                    *                      ***       **              ",
        "            ***       **                    *                    ***         **              ",
        "          ***         **                    *                  ***           **              ",
        "         ***          **                    *                ***             **              ",
        "        ***           **                    *              ***               **              ",
        "       *********************                *              ************************           ",
        "       *********************                *              ************************             ",
        "       *********************                *              ************************            ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                      **                    *                                **              ",
        "                     ****                   *                               ****             ",
        "                     ****                   *                               ****             ",
        "                     ****                   *                               ****             ",
        "        ************************            *                    ************************    ",
        "        ************************            *                    ************************    ",
        "        ************************            *                    ************************    ",
        "                                            *                                                ",
    ],

]

# Función para mostrar un dibujo en el display
def show_drawing(draw):
    for i in range(len(draw)):
        for j in range(len(draw[i])):
            if draw[i][j] == "*":
                display.pixel(j, i, 1)
            else:
                display.pixel(j, i, 0)
    display.show()

# Bucle principal para cambiar continuamente el dibujo
while True:
    for drawing in drawings:
        show_drawing(drawing)
        time.sleep(1)  # Espera 1 segundo antes de cambiar al siguiente dibujo
