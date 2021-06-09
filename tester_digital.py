#SW - Michal Basler
#https://github.com/Majklzbastlirny/Ethernet_Tester_Pi-Pico

#Importuje generic i custom knihovny
import machine
import utime
import time
import gc
from machine import *
from lcd_api import *
from pico_i2c_lcd import *

#V téhle části se nastaví základní parametry
led = Pin(25, Pin.OUT)
led.low()

#I2C nastavení
I2C_ADDR= 0x3F
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=4000000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.backlight_off()
lcd.clear()

#Tahle část říká, třeba že Pin 2 na PI Picu je v mém kódu označován jako out1 a tak dále pro další digitální Piny


out1 = Pin(2, Pin.OUT)
out2 = Pin(3, Pin.OUT)
out3 = Pin(4, Pin.OUT)
out4 = Pin(5, Pin.OUT)
out5 = Pin(6, Pin.OUT)
out6 = Pin(7, Pin.OUT)
out7 = Pin(8, Pin.OUT)
out8 = Pin(9, Pin.OUT)
in1 = Pin(11, Pin.IN)
in2 = Pin(12, Pin.IN)
in3 = Pin(13, Pin.IN)
in4 = Pin(14, Pin.IN)
in5 = Pin(15, Pin.IN)
in6 = Pin(16, Pin.IN)
in7 = Pin(17, Pin.IN)
in8 = Pin(18, Pin.IN)





#Zde se naprogramují často používané kousky kódu pro snadnější používání.
#Je to napsáno VELICE neefektivně. 



def get_1():
    global in_1
    out1.high()
    if in1.value() == 1:
        in_1 = 1
    elif in2.value() == 1:
        in_1 = 2
    elif in3.value() == 1:
        in_1 = 3
    elif in4.value() == 1:
        in_1 = 4
    elif in5.value() == 1:
        in_1 = 5
    elif in6.value() == 1:
        in_1 = 6
    elif in7.value() == 1:
        in_1 = 7
    elif in8.value() == 1:
        in_1 = 8
    else:
        in_1 = 0
    out1.low()
    print(in_1)

def get_2():
    global in_2
    out2.high()
    if in1.value() == 1:
        in_2 = 1
    elif in2.value() == 1:
        in_2 = 2
    elif in3.value() == 1:
        in_2 = 3
    elif in4.value() == 1:
        in_2 = 4
    elif in5.value() == 1:
        in_2 = 5
    elif in6.value() == 1:
        in_2 = 6
    elif in7.value() == 1:
        in_2 = 7
    elif in8.value() == 1:
        in_2 = 8
    else:
        in_2 = 0
    out2.low()
    print(in_2)
    
def get_3():
    global in_3
    out3.high()
    if in1.value() == 1:
        in_3 = 1
    elif in2.value() == 1:
        in_3 = 2
    elif in3.value() == 1:
        in_3 = 3
    elif in4.value() == 1:
        in_3 = 4
    elif in5.value() == 1:
        in_3 = 5
    elif in6.value() == 1:
        in_3 = 6
    elif in7.value() == 1:
        in_3 = 7
    elif in8.value() == 1:
        in_3 = 8
    else:
        in_3 = 0
    out3.low()
    print(in_3)

def get_4():
    global in_4
    out4.high()
    if in1.value() == 1:
        in_4 = 1
    elif in2.value() == 1:
        in_4 = 2
    elif in3.value() == 1:
        in_4 = 3
    elif in4.value() == 1:
        in_4 = 4
    elif in5.value() == 1:
        in_4 = 5
    elif in6.value() == 1:
        in_4 = 6
    elif in7.value() == 1:
        in_4 = 7
    elif in8.value() == 1:
        in_4 = 8
    else:
        in_4 = 0
    out4.low()
    print(in_4)
    
def get_5():
    global in_5
    out5.high()
    if in1.value() == 1:
        in_5 = 1
    elif in2.value() == 1:
        in_5 = 2
    elif in3.value() == 1:
        in_5 = 3
    elif in4.value() == 1:
        in_5 = 4
    elif in5.value() == 1:
        in_5 = 5
    elif in6.value() == 1:
        in_5 = 6
    elif in7.value() == 1:
        in_5 = 7
    elif in8.value() == 1:
        in_5 = 8
    else:
        in_5 = 0
    out5.low()
    print(in_5)

def get_6():
    global in_6
    out6.high()
    if in1.value() == 1:
        in_6 = 1
    elif in2.value() == 1:
        in_6 = 2
    elif in3.value() == 1:
        in_6 = 3
    elif in4.value() == 1:
        in_6 = 4
    elif in5.value() == 1:
        in_6 = 5
    elif in6.value() == 1:
        in_6 = 6
    elif in7.value() == 1:
        in_6 = 7
    elif in8.value() == 1:
        in_6 = 8
    else:
        in_6 = 0
    out2.low()
    print(in_6)
    
def get_7():
    global in_7
    out7.high()
    if in1.value() == 1:
        in_7 = 1
    elif in2.value() == 1:
        in_7 = 2
    elif in3.value() == 1:
        in_7 = 3
    elif in4.value() == 1:
        in_7 = 4
    elif in5.value() == 1:
        in_7 = 5
    elif in6.value() == 1:
        in_7 = 6
    elif in7.value() == 1:
        in_7 = 7
    elif in8.value() == 1:
        in_7 = 8
    else:
        in_7 = 0
    out7.low()
    print(in_7)

def get_8():
    global in_8
    out8.high()
    if in1.value() == 1:
        in_8 = 1
    elif in2.value() == 1:
        in_8 = 2
    elif in3.value() == 1:
        in_8 = 3
    elif in4.value() == 1:
        in_8 = 4
    elif in5.value() == 1:
        in_8 = 5
    elif in6.value() == 1:
        in_8 = 6
    elif in7.value() == 1:
        in_8 = 7
    elif in8.value() == 1:
        in_8 = 8
    else:
        in_8 = 0
    out8.low()
    print(in_8)


#zde už je hlavní část kódu.
#zde jde hlavně o měření, uložení a zobrazení hodnot
lcd.backlight_on()
lcd.putstr("Ethernet tester     ")
time.sleep(2)

lcd.clear()

lcd.putstr("Merim drat 1")
get_1()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 2")
get_2()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 3")
get_3()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 4")
get_4()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 5")
get_5()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 6")
get_6()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 7")
get_7()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Merim drat 8")
get_8()
time.sleep(0.75)

lcd.clear()

lcd.putstr("Zmereno")
led.toggle()      
utime.sleep(1)
led.toggle()
utime.sleep(0.2) 
led.toggle()
utime.sleep(1)
led.toggle()
utime.sleep(0.2)
lcd.clear()


#Zde už se bude porovnávat

#normal
if in_1 < in_2 < in_3 < in_4 < in_5 < in_5 < in_6 < in_7 < in_8:
    print("Vše ok")
    lcd.clear()
    lcd.putstr("Kabel OK -:)")
    time.sleep(10)
    lcd.clear()
    lcd.backlight_off()



#full crossover    
elif in_3 < in_6 < in_1 < in_7 < in_8 < in_2 < in_4 < in_5:
    print("full crossover")
    lcd.clear()
    lcd.putstr("Je to               crossover kabel.")
    time.sleep(10)
    lcd.clear()
    lcd.backlight_off()
          
#half crossover    
elif in_3 < in_6 < in_1 < in_4 < in_5 < in_2 < in_7 < in_8:
    print("half crossover")
    lcd.clear()
    lcd.putstr("Je to               crossover kabel.")
    time.sleep(10)
    lcd.clear()
    lcd.backlight_off()
    
#shorted
elif in_1 == in_2 == in_3 == in_4 == in_5 == in_5 == in_6 == in_7 == in_8:
    print("Šlus")
    lcd.clear()
    lcd.putstr("V kabelu je slus    nebo nezapojeno")
    time.sleep(10)
    lcd.clear()
    lcd.backlight_off()    
    
#oof
else:
    lcd.clear()
    print("undfnd")
    lcd.putstr("Kabel je vadny      :-(")
    time.sleep(10)
    lcd.clear()
    lcd.backlight_off()