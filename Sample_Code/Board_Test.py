
'''To Do List  Test ePy+ Hardware
2022/12/3 define 

            Z
              \  
               \
              (8x8LED)acc --> X
                |
                |
                Y 
Key Pad A,B,C,D

    8x8 LED -- Display
    Acc --> axl.get_x()
    Speaker --> music play

    microphone / Light Sensor --> ADC read
    RGB LED

    BLE -- > UART AT CMD Test 
    Y,R,G,B LED show 

flow
1. Start test Key A
    1.1 music play a Tone
    1.2 get acc x,y,z , show status in 8x8 display 
2. Test Key B
    2.1 get Mic_L value and convent the value to show RGB 1 Color
    2.2 get Mic_R  show it tot RGB 2 Color
3. Test Key C
    3.1 get BLE Version and display to 8x8
    3.2 show Y,R,G,B LED toggle 
4. Test Key D
    4.1 test Light sensor , show the levevl to 8x8 LED 

'''
from machine import Pin, ADC, UART, Switch, LED
from machine import accelerometer as acc
import music
from machine import display as disp
import utime as time


def key_cb():
    print('--keypad_INT --')

# TEST ACC and 8x8 LED // Buzzer


def Test_Func1():
    disp.on()
    music.play(['C'])
    while not keyb.value() and not keyc.value() and not keyd.value():
        acc_x = int(acc.get_x()/256)+3
        acc_x = 7 if acc_x >= 8 else acc_x
        acc_x = 0 if acc_x <= 0 else acc_x
        acc_y = int(acc.get_y()/256)+3
        acc_y = 7 if acc_y >= 8 else acc_y
        acc_y = 0 if acc_y <= 0 else acc_y
        acc_z = int(acc.get_z() / 256)+3
        acc_z = 7 if acc_z >= 8 else acc_z
        acc_z = 0 if acc_z <= 0 else acc_z
        # print('x={:5} , y={:5} ,z={:5} '.format(acc_x, acc_y, acc_z))
        disp.clear()
        disp.set_pixel(acc_x, acc_y, 9)
        time.sleep(0.1)

# TEST Microphone L/R and RGB LED


def Test_Func2():
    disp.on()
    music.play(['D'])
    M_data = []
    times = 0
    while not keya.value() and not keyc.value() and not keyd.value():
        M_data.clear()
        [M_data.append(mic_l.read()) for i in range(50)]
        Lmic = sum(M_data) / 50 // 1000
        M_data.clear()
        [M_data.append(mic_r.read()) for i in range(50)]
        Rmic = sum(M_data) / 50 // 1000

        # print('L={:5} ,R={:5}'.format(Lmic, Rmic))
        # show RGB LED
        if Lmic == 0:
            rgb.rgb_write(1, 0, 0, 0)
        elif Lmic == 1:
            rgb.rgb_write(1, 255, 255, 0)
        elif Lmic == 2:
            rgb.rgb_write(1, 0, 255, 0)
        elif Lmic == 3:
            rgb.rgb_write(1, 0, 0, 255)
        elif Lmic == 4:
            rgb.rgb_write(1, 255, 0, 0)

        if Rmic == 0:
            rgb.rgb_write(2, 0, 0, 0)
        elif Rmic == 1:
            rgb.rgb_write(2, 255, 255, 0)
        elif Rmic == 2:
            rgb.rgb_write(2, 0, 255, 0)
        elif Rmic == 3:
            rgb.rgb_write(2, 0, 0, 255)
        elif Rmic == 4:
            rgb.rgb_write(2, 255, 0, 0)
        for x in range(times+1):
            for y in range(8):
                disp.set_pixel(x, y, 9)
        times += 1
        if times >= 8:
            times = 0
            time.sleep(0.2)
            disp.clear()
        time.sleep(0.04)

# TEST BLE and  y,r,g,b


def Test_Func3():
    disp.on()
    music.play(['G', 'E'])
    lens = ble_port.write('AT+VERSION\r\n')
    time.sleep_ms(100)
    msg = str(ble_port.read().strip(), 'utf-8').split(' ')
    if msg[0] == 'VERSION':
        disp.scroll(msg[1], 300, wait=False, loop=True)
    else:
        disp.scroll('Error', 300, wait=False, loop=True)
    while not keyb.value() and not keyd.value() and not keya.value():
        for Led in led:
            Led.on()
            time.sleep(0.2)
            Led.off()
            time.sleep(0.2)


# TEST Light Sensor
def Test_Func4():
    disp.on()
    music.play(['F'])
    while not keyb.value() and not keyc.value() and not keya.value():
        L = light_sens.read() // 512
        disp.clear()
        for x in range(L+1):
            for y in range(8):
                disp.set_pixel(x, y, 9)
            print(x)
        time.sleep(0.5)


keya = Switch('keya')
keyb = Switch('keyb')
keyc = Switch('keyc')
keyd = Switch('keyd')

led = [LED('ledr'), LED('ledy'), LED('ledg'), LED('ledb')]

mic_l = ADC(Pin.epy.AIN8)
mic_r = ADC(Pin.epy.AIN7)
light_sens = ADC(Pin.epy.AIN6)

ble_port = UART(1, 115200, timeout=50)

keya.callback(key_cb)
keyb.callback(key_cb)
# keyc.callback(key_cb)
keyd.callback(key_cb)

rgb = LED(LED.RGB)

while True:
    if keya.value():
        Test_Func1()
    if keyb.value():
        Test_Func2()
    if keyc.value():
        Test_Func3()
    if keyd.value():
        Test_Func4()
