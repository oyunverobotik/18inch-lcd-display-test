LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.draw_circle(80,
    64,
    45,
    LCD1IN8.Get_Color(LCD_COLOR.BLUE),
    DRAW_FILL.DRAW_EMPTY,
    DOT_PIXEL.DOT_PIXEL_2)
LCD1IN8.draw_rectangle(10,
    10,
    150,
    118,
    LCD1IN8.Get_Color(LCD_COLOR.GREEN),
    DRAW_FILL.DRAW_EMPTY,
    DOT_PIXEL.DOT_PIXEL_3)
LCD1IN8.LCD_Display()

def on_forever():
    LCD1IN8.draw_circle(80,
        64,
        40,
        LCD1IN8.Get_Color(LCD_COLOR.WHITE),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.dis_number(70,
        40,
        input.compass_heading(),
        LCD1IN8.Get_Color(LCD_COLOR.BROWN))
    LCD1IN8.dis_string(50, 75, "Temp:", LCD1IN8.Get_Color(LCD_COLOR.RED))
    LCD1IN8.dis_number(85,
        75,
        input.temperature(),
        LCD1IN8.Get_Color(LCD_COLOR.RED))
    LCD1IN8.LCD_DisplayWindows(50, 40, 120, 90)
basic.forever(on_forever)
