from machine import display as disp
from machine import Image

disp.on()
disp.show('ABC', delay=1000)  # delay 1ms 跑馬燈
disp.show(Image.ALL_ARROWS, delay=1000, wait=False, loop=True)
disp.show(Image.COW)
disp.show(Image.invert(Image.COW))

mixed_up_list = ["hello!", 1.234, Image.HAPPY]
disp.show(mixed_up_list, delay=1000, wait=False, loop=True)

disp.off()

disp.on()


'''Image.
ALL_ARROWS      ANGRY           ARROW_E         ARROW_N
ARROW_NE        ARROW_NW        ARROW_S         ARROW_SE
ARROW_SW        ARROW_W         ASLEEP          CONFUSED
COW             DIAMOND         DIAMOND_SMALL   FABULOUS
HAPPY           HEART           HEART_SMALL     MEH
MUSIC_CROTCHET  MUSIC_QUAVER    MUSIC_QUAVERS   NO
PITCHFORK       SAD             SILLY           SMILE
SQUARE          SQUARE_SMALL    SURPRISED       TARGET
TRIANGLE        TRIANGLE_LEFT   XMAS            
---- function
blit
copy            crop            fill            get_pixel
height          invert          set_pixel       shift_down
shift_left      shift_right     shift_up        width
'''
